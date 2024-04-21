# Blockchain for Cross Border Finances

Team No.: 31

| Name  | Roll No. |
| ------------- | ------------- |
| Rohit Aryan  | 2020AAPS0293H  |
| Rohit Tulsi Padala  | 2021AAPS1896H  |
| Vipanchi Dixit  | 2021A3PS2983H  |
| K Dheeraj  | 2020AAPS2098H  |
| Niharika Pappu | 2020AAPS1322H  |

## Brief Description of the Project
Our project aims to facilitate cross-border finances through blockchain technology. By leveraging the inherent security, transparency, and efficiency of blockchain, we're creating a platform that streamlines international transactions, reduces processing times, and minimizes red-tape costs associated with traditional banking systems. 

Through HMAC verification in a Challenge-Response Algorithm Implementation, we're providing a trusted and immutable framework for conducting cross-border transactions, removing intermediaries and enhancing trust between parties. Ultimately, our goal is to empower individuals and businesses alike to participate in the global economy seamlessly and securely.

## Steps to run the file

1. Download all the code files and ensure that they are stored in the same directory. There are a total of six .py files.
2. Run the following python command in a relevant terminal. Ensure that the terminal is pointed to the directory containing the code files.

    ```
    python main.py
    ```
3. Once the console runs, the step by step procedure is presented to the user via statements on the console itself.

Points to note: Only valid usernames in the database are that of 'Alice', 'Bob' and 'Charlie'. We have also included a user 'Dummy' who can be used to simulate an unauthorised, malicious user/attacker. This can be shown in the demo. However, for the code to work, when the console asks you for sender or receiver usernames, you must enter one of the valid users only. Any attempt for Alice to make a transaction with Alice, i.e. herself, will result in an error.

## Example Usage

``` ruby
    >>> add block
    >>> Enter sender username: Alice
    >>> Enter receiver username: Charlie
    >>> Mode for Transaction: 1
    >>> Enter the amount to be transferred in USD: 10000
```

## Conditions put between countries to simulate actual scenarios

1. Share Transfer Tax: A flat tax of 10% is imposed on the transfer of shares between residents and non-residents of all countries to discourage speculative trading and ensure fair taxation. 

2. Country A imposes a higher transfer tax rate of 15% on shares transferred to residents of Country B compared to shares transferred to residents of Country C, reflecting political tensions between the two countries.

3. Share Transfer Limitation: Country C is weary of foreign influence in its capitalistic machine. 
Hence, shares can be transferred between residents of Country C and those of different countries, with a maximum allowable percentage of shares bought by non-residents, i.e. citizens of Countries A or B, set at 33%. Countries A and B follow the same policy but at 49%.

4. Country A has imposed a political embargo on Country B because of B’s active engagement in war, due to which residents of B are prohibited from availing of direct transfer of money and real estate. Transfer of shares is still permitted.

5. Country C does not permit non-residents to purchase properties larger than 2400 sqft. 

6. Country B caps the maximum amount of a single wire transfer of money at 50,000 USD for country A and 250,000 USD for country C.

7. All countries do not permit a wire transfer of funds of less than 5000 USD since it would be a waste of resources to allocate to transacting such a small amount.

## Code explanation

### Main.py

**User**: Represents a user with a username and location, and manages secret keys for transactions.

**Blockchain**: Manages the blockchain, including adding blocks and validating the chain.

**Transaction, Transaction_RealEstate, Transaction_Shares**: Represent different types of transactions, each with its own data requirements and processing logic.

**policy_check_money, policy_check_realEstate, policy_check_shares**: Functions for policy checks related to transactions.

### Block.py
    
**Importing Libraries**: The code imports necessary libraries like datetime, hashlib, json, random, and string.

**Block Class Definition**: The Block class represents a block in a blockchain. Each block contains a list of transactions, a reference to the previous block's hash, a timestamp, a nonce (a number used only once), and its own hash.

**Constructor (__init__)**: The __init__ method initializes a Block object. It takes a list of transactions and an optional previous_hash. It sets the transactions, previous_hash, timestamp, nonce (initially None), and hash (initially None).

**calculate_hash Method**: The calculate_hash method computes the hash of the block using the SHA-256 hashing algorithm. It converts the block's attributes into a JSON string, sorts the keys for consistency, encodes the string, and then computes the hash.

**mine_block Method**: The mine_block method is used to mine the block by finding a hash that meets a certain difficulty level (defined by the difficulty parameter). It repeatedly calculates the hash with different nonce values until a hash with the required number of leading zeros is found.

**is_valid Method**: The is_valid method checks if the block's hash is valid by comparing it with the computed hash using calculate_hash.


### Blockchain.py

**__init__(self)**: Initializes the blockchain with an empty list chain to store blocks and sets the difficulty of mining to 2.

**create_genesis_block(self)**: Creates a genesis block (the first block in the blockchain) with a single transaction labeled "Genesis". The genesis block has no previous hash, so "0" is passed as the previous_hash argument.

**add_genesis_block(self, block)**: Adds the genesis block to the blockchain's chain.

**get_last_block(self)**: Returns the last block in the blockchain's chain.

**add_block(self, new_block)**: Adds a new block to the blockchain. Sets the previous_hash of the new block to the hash of the last block in the chain, then calls mine_block on the new block with the specified difficulty level to find a valid hash. Finally, appends the new block to the chain.

**print_chain(self)**: Prints the hash of each block in the blockchain except for the genesis block.

**is_chain_valid(self)**: Checks the validity of the blockchain. Iterates over each block in the chain (excluding the genesis block) and checks if each block is valid (using is_valid method of Block class) and if the previous_hash of each block matches the hash of the previous block in the chain. If any block is found to be invalid, or if the previous_hash does not match, the chain is considered invalid.

### Policy.py

**policy_check_money** checks if a monetary transaction meets the specified conditions and limits for the sender and receiver locations.

**policy_check_realEstate** checks if a real estate transaction meets the specified conditions and limits for the sender and receiver locations.

**policy_check_shares** checks if a share transaction meets the specified conditions and limits for the sender and receiver locations, and calculates the fee and total amount for the transaction.

Each function returns a boolean value indicating whether the transaction is allowed (True) or not (False), along with additional information such as fees and total amounts in the case of share transactions.

### Transaction.py

**Transaction class**: Represents a generic transaction between two parties. It includes methods for converting the transaction to a dictionary, calculating data for hashing, verifying hash values, and processing the transaction. The process_transaction method checks for shared secret keys between the sender and receiver, calculates HMAC signatures, and adds the transaction to the user's transaction history and the blockchain.

**Transaction_RealEstate class**: Extends the Transaction class and includes an additional attribute for the area of real estate being transacted. It overrides the to_dict and calculate_data methods to include the new attribute in the transaction data.

**Transaction_Shares class**: Extends the Transaction class and includes additional attributes for the company and percentage of shares being transacted. It also includes attributes for fees and total amount. Similar to the other classes, it overrides the to_dict and calculate_data methods.

### User.py

**__init__(self, name, location)**: The constructor method initializes a User object with a name, location, an empty dictionary to store secret keys for Challenge-Response Authentication, and an empty list to store transactions.

**add_secret_keys(self, X, secretKey)**: This method adds a secret key secretKey for user X to the secret_keys dictionary.

**print_user_transactions(self)**: This method prints all transactions of the user. If no transactions have been made, it prints a message indicating that.

**add_user_transaction(self, transaction)**: This method adds a transaction to the user's list of transactions.
