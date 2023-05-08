"""
Project: New Curency
Author: Ignais La Paz Trujillo
Class: Blockchain
"""

import json
import pprint
from datetime import datetime
from time import time
from .crypto_currency import Block
from .transaction import Transaction
class Blockchain:

    #Constructor
    def __init__(self):
        self.chain = [self.genesis_block()]
        self.difficulty = 5
        self.pending_transaction = []
        self.reward = 10

    #First Block of the chain
    def get_genesis_block(self):
        genesis_block = Block(str(datetime.now()), "I'm the first block")
        return genesis_block

    #Last Block of the chain
    def get_last_block(self):
        return self.chain[-1]

    def mine_pending_trans(self, miner_address):
        new_block = Block(str(datetime.now()), self.pending_transaction)
        new_block.mine_block(self.difficulty)
        new_block.previous_block = self.get_last_block().hash

        test_chain = []
        for trans in new_block.transaction:
            temp = json.dumps(trans.__dict__, indent=5, separators=(',', ':'))
            test_chain.append(temp)
        pprint(test_chain)

        self.chain.append(new_block)
        reward = Transaction("System", miner_address, self.reward)
        self.pending_transaction.append(reward)
        self.pending_transaction = []

    def is_valid(self):
        for x in range(1, len(self.chain)):
            current_block = self.chain[x]
            previous_block = self.chain[x - 1]
            if (current_block.previous_block != previous_block.hash):
                return False
        return True

    def create_transaction(self, transaction):
        self.pending_transaction.append(transaction)


    def get_balace(self, wallet_address):
        balance = 0

        for block in self.chain:
            if block.previous_block == "":
                continue
            for trans in block.transaction:
                if trans.from_wallet == wallet_address:
                    balance -= trans.value
                if trans.to_wallet == wallet_address:
                    balance += trans.value

        return balance
