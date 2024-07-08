from yoomoney import Authorize
from dotenv import load_dotenv

from os import getenv


if __name__ == "__main__":
    load_dotenv()
    if not(client_id := getenv("CLIENT_ID")):
        print("client_id field must be in .env file")
        quit(1)
    client_id = str(client_id)
    Authorize(
        client_id=client_id,
        redirect_uri="https://test.ru",
        scope=["account-info",
            "operation-history",
            "operation-details",
            "incoming-transfers",
            "payment-p2p",
            "payment-shop",
            ]
        )
