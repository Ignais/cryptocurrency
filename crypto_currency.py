"""
Project: New Curency
Author: Ignais La Paz Trujillo
Class: Block
"""
import hashlib

#Class Block

class Block:

    #Constructor
    def __init__(self, time_stamp, transaction, previous_block=""):
        self.time_stamp = time_stamp
        self.transaction = transaction
        self.previous_block = previous_block
        self.difficulty = 0
        self.hash = self.calculate_hash(transaction, time_stamp, self.difficulty)

    #Calculate hash
    def calculate_hash(self, data, time_stamp, difficulty):
        data = str(data) + str(time_stamp) + str(difficulty)
        data = data.encode()
        hash = hashlib.sha256(data)

        return hash.hexdigest()

    #Mine block
    def mine_block(self, difficulty):
        difficulty_check = "0" * difficulty

        while self.hash[:difficulty] != difficulty_check:
            self.hash = self.calculate_hash(self.transaction, self.time_stamp, self.difficulty)
            self.difficulty += 1