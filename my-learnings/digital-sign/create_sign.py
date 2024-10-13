import json
import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from utility.logger_setup import logger
from decouple import config
from datetime import datetime

PRIVATE_KEY=config('PRIVATE_KEY')

def sign(data:dict)->dict:
    try:
        # Convert the dictionary to a JSON string
        data_json = json.dumps(data, sort_keys=True).encode('utf-8')

        with open(PRIVATE_KEY, "rb") as key_file:
            private_key = serialization.load_pem_private_key(key_file.read(), password=None)

        # Sign the JSON string
        signature = private_key.sign(
            data_json,
            ec.ECDSA(hashes.SHA256())
        )

        # Encode the signature to Base64 for transmission
        signature_base64 = base64.b64encode(signature).decode('utf-8')

        # Prepare the API request payload
        api_payload = {
            "data": data,
            "signature": signature_base64,
            "signed_timestamp":int(datetime.timestamp(datetime.now()))
        }
        
        logger.info("data is signed")
        return api_payload

    except Exception as e:
        logger.error("sign | "+repr(e))
