from logger_setup import logger
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
import json,base64

def verify(signature:str,data:dict)->bool:
    try:
        with open("public_key.pem", "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())

        data_json = json.dumps(data, sort_keys=True).encode('utf-8')
        signature_bytes = base64.b64decode(signature)

        public_key.verify(
            signature_bytes,
            data_json,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception as e:
        logger.error("verify | "+str(e))
        return False