"""
Project: New Curency
Author: Ignais La Paz Trujillo
Class:Blockchain
"""

import json
import pprint
from datetime import datetime
from time import time
from .crypto_currency import Block

class Blockchain:

    #Constructor
    def __init__(self):
        self.chain = [self.genesis_block()]
        self.difficulty = 5
        self.pending_transaction = []
        self.reward = 10

    #First Block of the chain
    def genesis_block(self):
        genesis_block = Block(str(datetime.now()), "I'm the first block")
        return genesis_block

    #Last Block of the chain
    def last_block(self):
        return self.chain[-1]

