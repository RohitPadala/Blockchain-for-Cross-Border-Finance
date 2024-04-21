
def policy_check_money(sender_loc, receiver_loc, amount):

        if receiver_loc == 'B' and sender_loc == 'A':
            print('... Due to war sanctions, B cannot monetary transactions with A')
            return False
        else:
            if amount < 5000:
                print('... Amount is below the minimum threshold of 5000 USD')
                return False
            elif sender_loc == 'B' and receiver_loc == 'A' and amount > 50000:
                print('... Amount violates the upper limit of 50000 USD placed on A by B')
                return False
            elif sender_loc == 'B' and receiver_loc == 'C' and amount > 250000:
                print('... Amount violates the upper limit of 250000 USD placed on C by B')
                return False
            else:
                return True

def policy_check_realEstate(sender_loc, receiver_loc, area):
        if sender_loc == 'C' and area > 2400:
            print('... Area violates the upper limit of 2400 sqft set by C')
            return False
        elif receiver_loc == 'B' and sender_loc == 'A':
            print('... Due to war sanctions, B cannot buy real estate in A')
            return False            
        else:
            return True
        
def policy_check_shares(sender_loc, receiver_loc, equity, amount):
        if sender_loc == 'A' :
            if equity > 49:
                print('... Equity violates the upper limit of 49 percent placed by A')
                return False, 0, 0
            else:
                if receiver_loc == 'B':
                    fee = 0.15 * amount
                else:
                     fee = 0.1 * amount
                total = fee + amount
                return True, fee, total
        elif sender_loc == 'B': 
            if equity > 49:
                print('... Equity violates the upper limit of 49 percent equity placed by B')
                return False, 0, 0
            else:
                fee = 0.1 * amount
                total = fee + amount
                return True, fee, total
        else:
            if equity > 33:
                print('... Equity violates the upper limit of 33 percent equity placed by C')
                return False, 0, 0
            else:
                fee = 0.1 * amount
                total = fee + amount
                return True, fee, total





        

