import datetime
import hashlib
import json
import random
import string


class Block:
    def __init__(self, transaction, previous_hash=None):
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.utcnow().isoformat()
        self.nonce = None
        self.hash = None

    def calculate_hash(self):
        return hashlib.sha256(json.dumps({
            'transaction': [tx.to_dict() for tx in self.transaction],
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'nonce': self.nonce
        }, sort_keys=True).encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        if self.hash is None:
            self.hash = ''
        while self.hash[:difficulty] != prefix:
            self.nonce = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            self.hash = self.calculate_hash()

    def is_valid(self):
        return self.hash == self.calculate_hash()