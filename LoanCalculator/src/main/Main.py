import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from decimal import *

class Loan():
    def __init__(self, principal: Decimal, rate: Decimal, payment: Decimal, period: int, startOn: int):
        self.principal = principal
        self.rate = rate
        self.payment = payment
        self.period = period
        self.startOn = startOn

class Account():
    def __init__(self, balance: Decimal, income: Decimal, period: int):
        self.balance = balance
        self.income = income
        self.period = period

class Strategy():
    def __init__(self, name: str, loan: Loan, account: Account):
        self.name = name
        self.loan = loan
        self.account = account

class PlotData():
    def __init__(self, principalData: [Decimal], interestData: [Decimal]):
        self.principalData = principalData
        self.interestData = interestData

def calcInterest(principal: Decimal, rate: Decimal):
    return principal*(rate/Decimal(365))

def populateData(principal: Decimal, rate: Decimal, payment: Decimal, recurr: int, startOn: int):
    i = 0
    principalData = []
    interestData = []
    totalInterestPaid = Decimal(0)
    while principal > 0:
        i += 1
        interestPaid = calcInterest(principal, rate)
        principal += interestPaid
        totalInterestPaid += interestPaid
        if i % (recurr - startOn) == 0 and i >= startOn:
            if principal < payment:
                principal = 0
            else:
                principal -= payment
        principalData.append(principal)
        interestData.append(totalInterestPaid)
    #print(f"_____principalData: {principalData}")
    #print(f"_____interestData: {interestData}")
    return PlotData(principalData, interestData)

def plotData(strategy):
    data = populateData(strategy.loan.principal, strategy.loan.rate, strategy.loan.payment, strategy.loan.period, strategy.loan.startOn)
    plt.plot(data.principalData, label = "Principal")
    plt.plot(data.interestData, label = "Interest Paid")

    plt.title(strategy.name)
    plt.ylabel('$ USD')
    plt.xlabel("Days")
    plt.legend()
    plt.show()

    return data  


if __name__ == "__main__":
    name = input("\nName your strategy: ")
    print("Enter Loan Information:")
    principal = Decimal(input("\tPrincipal = "))
    rate = Decimal(input("\tRate = "))
    if rate > 0:
        rate /= Decimal(100)
    payment = Decimal(input("\tPayment = "))
    loanPeriod = int(input("\tPayment Period (Days) = "))
    startOn = int(input("\tStarting on (Day) = "))
    loan = Loan(principal, rate, payment, loanPeriod, startOn)

    account = Account(0, 0, 0)
    data = plotData(Strategy(name, loan, account))

    print(f"Loan duration = {len(data.principalData)} days")
    print(f"Interest paid =  ${data.interestData[-1].quantize(Decimal('0.01'), ROUND_HALF_UP)}")
