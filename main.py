from User import User
from Blockchain import Blockchain
from Transaction import Transaction, Transaction_RealEstate, Transaction_Shares
from Policy import policy_check_money, policy_check_realEstate, policy_check_shares

if __name__ == "__main__":
    
    UserDB = {}
    
    Alice = User('Alice', 'A')
    Bob = User('Bob', 'B')
    Charlie = User('Charlie', 'C')
    Dummy = User('Dummy', 'A')

    UserDB[Alice.name] = Alice
    UserDB[Bob.name] = Bob
    UserDB[Charlie.name] = Charlie
    UserDB[Dummy.name] = Dummy

    Alice.add_secret_keys('Bob', b'1')
    Alice.add_secret_keys('Charlie', b'3')
    Alice.add_secret_keys('Dummy', b'5')

    Bob.add_secret_keys('Alice', b'1')
    Bob.add_secret_keys('Charlie', b'2')
    Bob.add_secret_keys('Dummy', b'6')

    Charlie.add_secret_keys('Alice', b'3')
    Charlie.add_secret_keys('Bob', b'2')
    Charlie.add_secret_keys('Dummy', b'7')

    Dummy.add_secret_keys('Alice', b'100')
    Dummy.add_secret_keys('Bob', b'101')
    Dummy.add_secret_keys('Charlie', b'102')

    blockchain = Blockchain()
    genesis_block = blockchain.create_genesis_block()
    genesis_block.calculate_hash()
    blockchain.add_genesis_block(genesis_block)

    ('\n\n-------------------------------------------------------------------------------------------------------------')
    print("*****BLOCKCHAIN FOR CROSS BORDER EXCHANGES*****\n")

    while(True):

        print('\n-------------------------------------------------------------------------------------------------------------')
        print("... Available commands: ")
        print("... 1. add block --- Add new block to existing blockchain")
        print("... 2. view user --- View successful transactions of a user")
        print("... 3. exit --- Exit from console. All transactions are written to file and loaded on next run")

        command = input(">>> ")

        if command == '1' or command == 'add block':
            
            if blockchain.is_chain_valid():
            
                print('... No issue found in verification of Blockchain')
                sender = input(">>> Enter sender username: ")
                if sender in UserDB.keys():
                    sender_loc = UserDB[sender].location
                    reciever = input('>>> Enter reciever username: ')
                    if reciever in UserDB.keys():
                        reciever_loc = UserDB[reciever].location
                        print('... Transaction Modes available:')
                        print('... 1. Wire Money')
                        print('... 2. Real Estate')
                        print('... 3. Shares')
                        mode = input('>>> Mode for Transaction: ')
                        if mode == '1':
                            # currency = input('Enter the currency: ')
                            amount = input('>>> Enter the amount to be transfered in USD: ')
                            transaction = Transaction(sender, reciever, amount, sender_loc, reciever_loc)
                            # print(policy_check_money(sender_loc, reciever_loc, int(amount)))
                            if policy_check_money(sender_loc, reciever_loc, int(amount)):
                                print('... Transaction now being verified')
                                data = transaction.calculate_data()
                                transaction.process_transaction(sender, reciever, data, UserDB, blockchain)
                             
                            
                        elif mode == '2':
                            amount = input('>>> Price for the land: ') 
                            area = input('>>> Area in sqft: ')
                            transaction = Transaction_RealEstate(sender, reciever, amount, sender_loc, reciever_loc, area)

                            if policy_check_realEstate(sender_loc, reciever_loc, int(area)):
                                print('... Transaction now being verified')
                                data = transaction.calculate_data()
                                transaction.process_transaction(sender, reciever, data, UserDB, blockchain)

                        elif mode == '3':
                            company = input('>>> Company whose shares you want to sell: ')
                            percent = input('>>> Percentage of shares you are selling: ')
                            amount = input('>>> Amount of shares you want to sell: ')
                            transaction = Transaction_Shares(sender, reciever, amount, sender_loc, reciever_loc, company, percent)

                            cond, fee, total = policy_check_shares(sender_loc, reciever_loc, int(percent), int(amount))
                            transaction.fee = fee
                            transaction.total = total
                            
                            if cond:
                                print(f'... Tax on transaction = {fee}')
                                print(f'... Total Charged = {total}')
                                print('... Transaction now being verified')
                                data = transaction.calculate_data()
                                transaction.process_transaction(sender, reciever, data, UserDB, blockchain)


                        else:
                            print('... Not valid transaction mode')
                    else:
                        print('... Reciever does not exist in User Database')
                else:
                    print('... Sender does not exist in User Database')

            else:
                print('... Some issue faced in validating blockchain')

        elif command=='2' or command == 'view user':
            sender = input(">>> Username: ")
            if sender in UserDB.keys():
                UserDB[sender].print_user_transactions()
            else:
                print('... User does not exist in User Database')

        elif command == '3' or command == 'exit':
            print("... Exiting blockchain console")
            break
        else:
            print('... Invalid command')

