from decimal import Decimal

class SimpleInterestLoan:
    def __init__(self, principal: Decimal, payment: Decimal, paymentPeriod: int):
        self.principal = principal
        self.payment = payment
        self.paymentPeriod = paymentPeriod

    def makepPayment(self):
        self.principal -= self.payment

def calculateInterestGainedByDays(principal: Decimal, rate: Decimal, days: int):
    rate /= 100
    return principal*(rate/365)*days


def calculatePrincipalAfterDays(loan: SimpleInterestLoan, rate: Decimal, days: int, startOnDay: int = 0, returnFullList: bool = False):
    currentDay = days
    fullList = []
    while currentDay < days:
        # Could add more sophisticated checks based on payment time
        # to determine if interest should be calculated before or after payment
        # since this is designed for automatic recurring payments
        # I will proceed with the assumption that the interest is charged before
        loan.principal += calculateInterestGainedByDays(loan.principal, rate, 1)
        if currentDay == startOnDay or currentDay % (loan.paymentPeriod + startOnDay) == 0:
            loan.makePayment()
        if returnFullList:
            fullList.append(loan.principal)
        currentDay += 1
    if returnFullList:
        return fullList
    return loan.principal