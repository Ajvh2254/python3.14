class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)

    def __getitem__(self, i):
        return self.players[i]

    def __repr__(self):
        return f"Club {self.name}: {self.players}"


some_club = Club('Arsenal')
some_club.players.append('Jerome')
some_club.players.append('Terrence')

print(len(some_club)) # prints length of list
print(some_club) # prints repr description of list
print(some_club[0]) # player name by the index using 'getitem'

for club in some_club:
    print(club) # iterates through for loop using 'len' and 'getitem'

