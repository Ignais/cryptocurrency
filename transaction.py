"""
Project: New Curency
Author: Ignais La Paz Trujillo
Class: Transaction
"""


class Transaction:

    def __init__(self, from_wallet, to_wallet, amount):
        self.from_wallet = from_wallet
        self.to_wallet = to_wallet
        self.amount = amount