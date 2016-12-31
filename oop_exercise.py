#!/usr/bin/env python
#-*- coding: utf-8 -*-
import credit_card

# Make classes like Pojos in Java to apply Dependency Ijection on getting objects
class Category():
    pass

class Entrie(object):
    # ID
    # Category Education / Health / Clothing / Taxes / Food
    # BuyDate
    # PaymentDate
    # Description
    # Type Expense / Credit
    pass

class MonthlyExpense():
    pass

def main():
    cc = CreditCard()
    cc.print_balance()

if __name__ == '__main__':
    main()
