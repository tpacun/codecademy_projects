import random
import json
import os
import time

class Session:
    def __init__(self, username):
        self.userslist = './resources/users.csv'
        os.makedirs(os.path.dirname(self.userslist), exist_ok=True)
        self.username = username

    def load_user(self):
        with open(self.userslist, 'a') as userlist:
            user_dict = {}
            try:
                reader = userlist.read()
                user_dict = json.loads(reader)
                #loaded corrctly (eg not empty- maybe worth adding in specific error checking)
                #next step check for username in user_dict
                #return user_dict[self.username]
            except:
                # file is empty - need to create dictionary
                # write user to user_dict
                # return user_dict[self.username]
                if self.username in list(user_dict.keys):
                    print('Loading User')
                    for x in range(0,3):
                        time.sleep(1)
                        print('.')
                    return user_dict[self.username]
                else:
                    print('User not found. Creating new user')
                    for x in range(0,3):
                        time.sleep(1)
                        print('.')
                    writer.writeheader()
                    writer.writerow({
                        'name': self.username,
                        'settings': [],
                        'history': []})
                    return user_dict[self.username]


class Username:
    def __init__(self, name):
        self.name = name
        with open('files/users/userlist.csv','a') as f:
            user_dictionary = csv.DictReader(f)
            if self.name in user_dictionary.fieldsnames:
                self.settings = user_dictionary[self.name]['settings']
                self.history = user_dictionary[self.name]['history']
            else:
                self.settings = {}
                self.history = {}
                writer = csv.DictWriter(f)
                writer.writerow({'user': self.name, 'settings':self.settings, 'history':self.history})

class Card:
    def __init__(self, num, suit):
        self.suit = suit
        self.num = num

class Deck:
    def __init__(self):
        suits = ['c', 'd', 'h', 's']
        nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [Card(num,suit) for num in nums for suit in suits]
        self.shuffle(1)

    def shuffle(self, times = 0):
        random.shuffle(self.deck)
        if times > 1:
            for x in range(1, times):
                self.shuffle()
    
    def deal(self):
        return self.deck.pop(0)

class Hand:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.hand = [self.card1, self.card2]

    def draw(self, card):
        self.hand.append(card)
    
    def value(self, std_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}):
        total_value = 0
        for card in self.hand:
            total_value += std_values[card.num]
        if total_value > 21:
            Hand.value(std_values.update({'A': 1}))



print('Welcome to Blackjack')
init_user = input('Username:')
game_session = Session(username = init_user)
game_user = game_session.load_user()
print(game_user)
