from yoomoney import Quickpay

from dotenv import load_dotenv
from os import getenv

class YoomoneyPay:
    def __init__(self, reciever: str, sum: int = 2):
        self.reciever: str = reciever
        self.sum: int = sum

    def set_sum(self, sum: int):
        self.sum = sum

    def quickpay(self) -> str:
        quickpay = Quickpay(
                    receiver=self.reciever,
                    quickpay_form="shop",
                    targets="Поддержать меня 2р",
                    paymentType="SB",
                    sum=self.sum,
                    )
        return quickpay.redirected_url

if __name__ == "__main__":
    # testing
    load_dotenv()
    if not(card_id := getenv("CARD_ID")):
        print("CARD_ID must be in .env file!")
        quit(1)
    card_id = str(card_id)

    payment = YoomoneyPay(reciever=card_id)
    print(payment.quickpay())

