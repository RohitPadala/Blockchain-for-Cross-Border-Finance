import hashlib
import hmac
import json


class User:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.secret_keys = {}
        self.transactions = []

    def add_secret_keys(self, X, secretKey):
        self.secret_keys[X] = secretKey

    def print_user_transactions(self):
        if self.transactions == []:
            print(f'No transactions done by {self.name}')
        else:
            for tx in self.transactions:
                print(tx)

    def add_user_transaction(self, transaction):
        self.transactions.append(transaction)


