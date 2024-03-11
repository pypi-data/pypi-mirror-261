import time
import base64
import hmac
import hashlib
import re
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

FIVE_MINUTES = 5 * 60 * 1000

def make_secure_webhooks(get_signer, get_verifier):
    def sign(input_str, secret_or_private_key, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time() * 1000)
        signer = get_signer(secret_or_private_key)
        return f"v={timestamp},d={signer(input_str + str(timestamp))}"

    def verify(input_str, secret_or_public_key, signature, opts=None):
        if opts is None:
            opts = {}
        match = re.search(r'v=(\d+),d=(.*)', signature)
        if not match:
            return False

        poststamp = int(match.group(1))
        post_digest = match.group(2)

        timestamp = opts.get('timestamp', int(time.time() * 1000))
        timeout = opts.get('timeout', FIVE_MINUTES)

        difference = abs(timestamp - poststamp)
        if difference > timeout:
            return False

        verifier = get_verifier(secret_or_public_key)
        return verifier(input_str + str(poststamp), post_digest)

    return {"sign": sign, "verify": verify}

def symmetric_get_signer(secret):
    def signer(input_str):
        return hashlib.sha256(secret.encode() + input_str.encode()).hexdigest()
    return signer


def symmetric_get_verifier(secret):
    def verifier(input_str, digest):
        algo = hashlib.sha256
        hmac_instance = hmac.new(secret.encode(), digestmod=algo)
        hmac_instance.update(input_str.encode())
        print("digest")
        print(hmac_instance.hexdigest())
        print(digest)
        return hmac_instance.hexdigest() == digest
    return verifier

def asymmetric_get_signer(private_key):
    def signer(input_str):
        private_key_obj = load_pem_private_key(private_key.encode(), password=None)
        signature = private_key_obj.sign(
            input_str.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()
    return signer

def asymmetric_get_verifier(public_key):
    def verifier(input_str, digest):
        public_key_obj = load_pem_public_key(public_key.encode())
        try:
            public_key_obj.verify(
                base64.b64decode(digest),
                input_str.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False
    return verifier
