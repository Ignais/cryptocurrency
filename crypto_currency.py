"""
Project: New Curency
Author: Ignais La Paz Trujillo
"""
import hashlib
import json
import pprint
from datetime import datetime
from time import time

#Class Block

class Block:

    def __init__(self, time_stamp, transaction, previous_block=""):
        self.time_stamp = time_stamp
        self.trans = transaction
        self.previous_block = previous_block
        self.difficulty = 0
        self.hash = self.calculate_hash(transaction, time_stamp, self.difficulty)

    def calculate_hash(self, data, time_stamp, difficulty):
        data = str(data) + str(time_stamp) + str(difficulty)
        data = data.encode()
        hash = hashlib.sha256(data)

        return hash.hexdigest()