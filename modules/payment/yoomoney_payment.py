from yoomoney import Quickpay


# Класс, который создает ссылку для перехода на yoomoney сервис
class YoomoneyPay:
    def __init__(self, reciever: str, sum: int = 2):
        self.reciever: str = reciever
        self.sum: int = sum

    def quickpay(self) -> str:
        quickpay = Quickpay(
                    receiver=self.reciever,
                    quickpay_form="shop",
                    targets="Поддержать меня 2р",
                    paymentType="SB",
                    sum=self.sum,
                    )
        return quickpay.redirected_url
