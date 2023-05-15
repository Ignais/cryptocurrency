"""
Project: New Curency
Author: Ignais La Paz Trujillo
Main Flask application with MongoDB Connection
"""

from blockchain import Blockchain

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/blockchain"
mongo = PyMongo(app)

def block_entity(block):
    return {
        "time_stamp": block.time_stamp,
        "transaction": block.transaction,
        "previous_block": block.previous_block,
        "difficulty": block.difficulty,
        "hash": block.hash
    }

def blockchain(chain):
    return [block_entity(block) for block in chain]

@app.route("/blockchain", methods=["GET","POST"])
def create_blockchain(name):
    new_chain = mongo.db.blkch.find_one({'name': name})
    if not new_chain:
        blkch = Blockchain(name=name)
        if (len(blkch.chain)) == 0:
            blkch.chain.append(blkch.get_genesis_block())
            chain = blockchain(blkch.chain)
            content = {
                "name": name,
                "chain": chain,
                "difficulty": blkch.difficulty,
                "reward": blkch.reward
            }
            mongo.db.blkch.insert_one(content)
            return {"message": "Success created"}
    return {"message": "The chain is not empty"}

app.run("0.0.0.0", port=8080, debug=True)