import hashlib
import hmac
import json
import random
from Block import Block


class Transaction:
    def __init__(self, sender, reciever, amount, sender_loc, receiver_loc):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        # self.currency = currency
        self.sender_loc = sender_loc
        self.reciever_loc = receiver_loc

    def to_dict(self):
        return {
            'sender': self.sender,
            'reciever': self.reciever,
            'amount': self.amount,
            # 'currency': self.currency,
            'sender_location': self.sender_loc,
            'reciever_location': self.reciever_loc
        }

    def calculate_data(self):
        data = json.dumps(self.to_dict(), sort_keys=True).encode('utf-8')
        random_bit = random.randint(0, 1)
        random_bit_bytes = bytes([random_bit])
        data = data + random_bit_bytes
        return data
    
    def verify_hash(self, hash1, hash2):
        return hmac.compare_digest(hash1, hash2)
    
    def calculate_hmac_signature(self, data, secret_key):
        return hmac.new(secret_key, data, hashlib.sha256).hexdigest()
    
    def process_transaction(self, sender, receiver, data, UserDB, blockchain):
        if receiver not in UserDB[sender].secret_keys or sender not in UserDB[receiver].secret_keys:
            print('... No shared secret key found')
        else:
            sender_secret_key = UserDB[sender].secret_keys[receiver]
            receiver_secret_key = UserDB[receiver].secret_keys[sender]
            sender_hash = self.calculate_hmac_signature(data, sender_secret_key)
            receiver_hash = self.calculate_hmac_signature(data, receiver_secret_key)
            if sender_hash != receiver_hash:
                print('... Transaction Failed (Shared keys are not same)')
            else:
                # print(sender_hash, " ", receiver_hash)
                print('... Transaction Successful')
                print('... Adding transaction details to user transaction history')
                UserDB[sender].add_user_transaction(self.to_dict())
                UserDB[receiver].add_user_transaction(self.to_dict())
                print('... Transaction added to users transaction history')

                new_block = Block([self])
                blockchain.add_block(new_block)
                print('... Block added to blockchain')


class Transaction_RealEstate(Transaction):
    def __init__(self, sender, reciever, amount, sender_loc, reciever_loc, area):
        super().__init__(sender, reciever, amount, sender_loc, reciever_loc)
        self.area = area

    def to_dict(self):
        return {
            'sender': self.sender,
            'reciever': self.reciever,
            'amount': self.amount,
            # 'currency': self.currency,
            'sender_location': self.sender_loc,
            'reciever_location': self.reciever_loc,
            'area': self.area
        }

    def calculate_data(self):
        data = json.dumps(self.to_dict(), sort_keys=True).encode('utf-8')
        random_bit = random.randint(0, 1)
        random_bit_bytes = bytes([random_bit])
        data = data + random_bit_bytes
        return data
    
    def process_transaction(self, sender, receiver, data, UserDB, blockchain):
        if receiver not in UserDB[sender].secret_keys or sender not in UserDB[receiver].secret_keys:
            print('... No shared secret key found')
        else:
            sender_secret_key = UserDB[sender].secret_keys[receiver]
            receiver_secret_key = UserDB[receiver].secret_keys[sender]
            sender_hash = self.calculate_hmac_signature(data, sender_secret_key)
            receiver_hash = self.calculate_hmac_signature(data, receiver_secret_key)
            if sender_hash != receiver_hash:
                print('... Transaction Failed (Shared keys are not same)')
            else:
                # print(sender_hash, " ", receiver_hash)
                print('... Transaction Successful')
                print('... Adding transaction details to user transaction history')
                UserDB[sender].add_user_transaction(self.to_dict())
                UserDB[receiver].add_user_transaction(self.to_dict())
                print('... Transaction added to users transaction history')

                new_block = Block([self])
                blockchain.add_block(new_block)
                print('... Block added to blockchain')
    
class Transaction_Shares(Transaction):
    def __init__(self, sender, reciever, amount, sender_loc, reciever_loc, company, percent):
        super().__init__(sender, reciever, amount, sender_loc, reciever_loc)
        self.company = company
        self.percent = percent
        self.fee = 0
        self.total = 0

    def to_dict(self):
        return {
            'sender': self.sender,
            'reciever': self.reciever,
            'amount': self.amount,
            # 'currency': self.currency,
            'sender_location': self.sender_loc,
            'reciever_location': self.reciever_loc,
            'company': self.company,
            'percent': self.percent,
            'fee': self.fee,
            'total': self.total
        }

    def calculate_data(self):
        data = json.dumps(self.to_dict(), sort_keys=True).encode('utf-8')
        random_bit = random.randint(0, 1)
        random_bit_bytes = bytes([random_bit])
        data = data + random_bit_bytes
        return data
    
    def process_transaction(self, sender, receiver, data, UserDB, blockchain):
        if receiver not in UserDB[sender].secret_keys or sender not in UserDB[receiver].secret_keys:
            print('... No shared secret key found')
        else:
            sender_secret_key = UserDB[sender].secret_keys[receiver]
            receiver_secret_key = UserDB[receiver].secret_keys[sender]
            sender_hash = self.calculate_hmac_signature(data, sender_secret_key)
            receiver_hash = self.calculate_hmac_signature(data, receiver_secret_key)
            if sender_hash != receiver_hash:
                print('... Transaction Failed (Shared keys are not same)')
            else:
                # print(sender_hash, " ", receiver_hash)
                print('... Transaction Successful')
                print('... Adding transaction details to user transaction history')
                UserDB[sender].add_user_transaction(self.to_dict())
                UserDB[receiver].add_user_transaction(self.to_dict())
                print('... Transaction added to users transaction history')

                new_block = Block([self])
                blockchain.add_block(new_block)
                print('... Block added to blockchain')

    
