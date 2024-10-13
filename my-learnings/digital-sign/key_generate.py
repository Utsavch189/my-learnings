from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import os
from utility.logger_setup import logger
from decouple import config

PUBLIC_KEY=config('PUBLIC_KEY')
PRIVATE_KEY=config('PRIVATE_KEY')


def generate_private_key(key)->None:
    try:
        with open(PRIVATE_KEY, "wb") as f:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        print("PRIVATE KEY IS GENERATED.....")
    except Exception as e:
        raise Exception(str(e))

def generate_public_key(key)->None:
    try:
        public_key = key.public_key()
        with open(PUBLIC_KEY, "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        print("PUBLIC KEY IS GENERATED.....")
    except Exception as e:
        raise Exception(str(e))


def generate_keypair()->None:
    try:
        private_key = ec.generate_private_key(ec.SECP256R1())

        # check private key exists or not
        if not os.path.exists(PRIVATE_KEY):
            generate_private_key(private_key)
            logger.info("private key is generated")

        # check public key exists or not
        if not os.path.exists(PUBLIC_KEY):
            generate_public_key(private_key)
            logger.info("public key is generated")

    except Exception as e:
        logger.error("generate_key_pair | "+repr(e))
        print(f"Error : {e}")
