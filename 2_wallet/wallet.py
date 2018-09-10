#!/usr/bin/env python3


class InsufficientAmount(Exception):
    pass

class Wallet(object):
    """ define your wallet    
    """
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount