#Card.py

class Card:
    def __init__(self, suit, rank, parent = None, left = None, right = None, count = 1):
        self.suit = suit
        self.rank = rank
        self.parent = parent
        self.left = left
        self.right = right
        self.count = count
    def getSuit(self):
        return self.suit.upper()
    def setSuit(self, suit):
        self.suit = suit
    def getRank(self):
        return self.rank.upper()
    def setRank(self, rank):
        self.rank = rank
    def getCount(self):
        return self.count
    def setCount(self, count):
        self.count = count
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent
    def getLeft(self):#same as has_left_child
        return self.left
    def setLeft(self, left):
        self.left = left
    def getRight(self):#same as has_right_child
        return self.right
    def setRight(self, right):
        self.right = right
    def __str__(self):
        return '{} {} | {}\n'.format(self.getSuit(),self.getRank(),self.count)
    def is_left(self):
        if self.parent and self.parent.left:
                return self.parent.left == self
        else:
            return False
    def is_right(self):
        if self.parent and self.parent.right:
                return self.parent.right == self
        else:
            return False
    def is_root(self):
        return not self.parent
    def is_leaf(self):
        return not (self.right or self.left)
    def has_any_children(self):
        return self.right or self.left
    def replace_card(self, suit, rank, left, right, count):
        self.suit = suit
        self.rank = rank
        self.left = left
        self.right = right
        self.count= count
        if self.getLeft():
            self.left.parent = self
        if self.getRight():
            self.right.parent = self
    #1.rank,2.suit
    def __gt__(self,rhs):
        rankD={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
        suitD={'C':1,'D':2,'H':3,'S':4}
        if self.rank.upper() == rhs.rank.upper():
            return suitD[self.suit.upper()]>suitD[rhs.suit.upper()]
        else:
            return rankD[self.rank.upper()]>rankD[rhs.rank.upper()]
    def __lt__(self,rhs):
        rankD={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
        suitD={'C':1,'D':2,'H':3,'S':4}
        if self.rank.upper() == rhs.rank.upper():
            return suitD[self.suit.upper()]<suitD[rhs.suit.upper()]
        else:
            return rankD[self.rank.upper()]<rankD[rhs.rank.upper()]
    def __eq__(self, rhs):
        rankD={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
        suitD={'C':1,'D':2,'H':3,'S':4}
        return rankD[self.rank.upper()] == rankD[rhs.rank.upper()] and suitD[self.suit.upper()]==suitD[rhs.suit.upper()]
    def getRightChildMinCard(self):
        right = self.getRight()
        while right.getLeft():
            right=right.left
        return right

            
