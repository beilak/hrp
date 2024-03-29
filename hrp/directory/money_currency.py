from moneyed import Money as BaseMoney


class Money(BaseMoney):
    def __composite_values__(self):
        return self.amount, self.currency.code
