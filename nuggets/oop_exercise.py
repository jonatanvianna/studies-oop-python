#!/usr/bin/env python
#-*- coding: utf-8 -*-
import credit_card


# Make classes like Pojos in Java to apply Dependency Ijection on getting objects
class Category(object):
    def __init__(self):
        pass

class Entry(object):

    def __init__(self, _id):
        self._id = _id

    # Empty constructor must be the last one listed
    def __init__(self):
        pass

    def get_id(self):
        return self._id

    def set_id(self, _id):
        self._id = _id

    # ID
    # Category Education / Health / Clothing / Taxes / Food
    # BuyDate
    # PaymentDate
    # Description
    # Type Expense / Credit


class MonthlyExpense(object):
    def __init__(self):
        pass


def main():
    c = credit_card.CreditCard()
    c.print_balance()

    e = Entry()
    e.set_id(69)
    print e.get_id()

if __name__ == '__main__':
    main()
