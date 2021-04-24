print('Welcome to my Blind auction program')

from art_auction import auction_logo
print(auction_logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'the winner of the bid is {winner} with an amount of ${highest_bid}')

while not bidding_finished:
    name = input('Please enter your name: ')
    price = int(input('Please Enter the price you wish to bid: $'))
    bids[name] = price
    other_users = input('Are there other users who wishes to bid, type "YES" or "NO"? \n').lower()
    if other_users == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif other_users == 'yes':
        clear()

    