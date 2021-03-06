# Converting Floating-Point Values to Monetary Amounts
# Version 1

class MoneyFmt:

    def __init__(self, value = 0.):
        self.value = value

    def update(self, value=None):
        self.value = value

    def __str__(self):
        return "${:,.2f}".format(self.value)

    def __repr__(self):
        return f"MoneyFmt({self.value})"

    def isnonzero(self):
        if abs(self.value) >= 0.005:
            print("True")
        else:
            print("False")
