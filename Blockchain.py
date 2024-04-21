from Block import Block
from Transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 2

    def create_genesis_block(self):
        return Block([Transaction("Genesis", "", 0, "", "")], "0")
    
    def add_genesis_block(self, block):
        self.chain.append(block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            print(current_block.hash)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if not current_block.is_valid():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True