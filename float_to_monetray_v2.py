# Converting Floating-Point Values to Monetary Amounts
# Version 2

class MoneyFmt:
    """ A class converting floating-point values to monetary amounts """

    def __init__(self, value=0.):
        """ Initialize the floating-point value with the given value """
        self.value = value

    def update(self, value=None):
        """ Update the floating-point value """
        self.value = value

    def __str__(self):
        """ Display the floating-point value as a monetary amount
        to two decimal places with the correct sign """
        if self.value > 0:
            ms = '$'
        else:
            ms = '-$'
        s = '{:.2f}'.format(round(abs(self.value) * 100) / 100)
        if len(s) > 6:
            n = len(s) - 6
            if n % 3 != 0:
                ms += s[0 : n % 3] + ','
            for i in range(n % 3, n, 3):
                ms += s[i: i + 3] + ','
            ms += s[-6:]
        else:
            ms += s
        return ms

    def __repr__(self):
        """ Return a string such that eval applied to the string
        recreates the instance """
        return "MoneyFmt({0:s})".format(str(self.value))

    def isnonzero(self):
        """ Check if the floating-point value is non-zero where a
        value with absolute value < 0.005 is regarded as zero """
        return abs(self.value) >= 0.005
