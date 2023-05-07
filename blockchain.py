"""
Project: New Curency
Author: Ignais La Paz Trujillo
Class:Blockchain
"""

from .crypto_currency import Block

class Blockchain:

    #Constructor
    def __init__(self):
        self.chain = [self.genesis_block()]
        self.difficulty = 5
        self.pending_transaction = []
        self.reward = 10

    