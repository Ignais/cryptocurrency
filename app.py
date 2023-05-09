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

ignais = Blockchain()

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
def create_blockchain():
    if (len(ignais.chain)) == 0:
        ignais.chain.append(ignais.get_genesis_block())
        chain = blockchain(ignais.chain)
        content = {
            "chain": chain,
            "difficulty": ignais.difficulty,
            "reward": ignais.reward
        }
        mongo.db.ignais.insert_one(content)
        return {"message": "Success created"}
    return {"message": "The chain is not empty"}

app.run("0.0.0.0", port=8080, debug=True)