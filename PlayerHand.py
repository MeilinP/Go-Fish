#PlayerHand.py
from Card import Card
class PlayerHand:
    def __init__(self):
        self.root =None
        self.size = 0
#tested
    def getTotalCards(self):
        return self.size
#tested
    def getMin(self):
        if self.size ==0:
            return None
        elif self.size == 1:
            return self.root
        else:
            current = self.root
            while current.left:
                current = current.left
            return current
#tested
    def isEmpty(self):
        if self.root:
            return False
        else:
            return True
#tested
    def getSuccessor(self, suit,rank):
        currentCard = self.get(suit,rank)
        #check if the card exists
        if currentCard:
            #if it has a rightchild, recursively go left
            if currentCard.getRight():
                return currentCard.getRightChildMinCard()
            #it doesnt have a rightchild, check parent
            else:
                if currentCard.getParent():
                    #if it is the left child, the succ is its parent
                    if currentCard.is_left():
                        return currentCard.parent
                    #if it is the right child, the successor is the parent that is the left child of its parent
                    else:
                        parent = currentCard.parent
                        while not parent.is_left():
                            if parent.parent:
                                parent=parent.parent
                            else:
                                return None
                        return parent.parent
                else:
                    return None
        else:
            return None
        
#tested
    def put(self,suit,rank):
        if self.root:
            self._put(suit,rank,self.root)
        else:
            self.root = Card(suit,rank)
        self.size+=1
    def _put(self,suit,rank,currentCard):
        if Card(suit,rank) == currentCard:
            currentCard.count +=1
        elif Card(suit,rank)<currentCard:
            if currentCard.left:
                self._put(suit,rank,currentCard.left)
            else:
                currentCard.left=Card(suit,rank,parent=currentCard)
        else:
            if currentCard.right:
                self._put(suit,rank,currentCard.right)
            else:
                currentCard.right = Card(suit,rank,parent=currentCard)
#tested
    def get(self,suit,rank):
        if self.root:
            res = self._get(suit, rank, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None
    def _get(self, suit, rank, currentCard):
        if not currentCard:
            return None
        elif currentCard==Card(suit,rank):
            return currentCard
        elif Card(suit,rank)<currentCard:
            return self._get(suit,rank,currentCard.left)
        else:
            return  self._get(suit,rank,currentCard.right)
    def delete(self,suit,rank):
        cardToRemove = self.get(suit,rank)
        if self.size >1:
            if cardToRemove and cardToRemove.count>1:
                cardToRemove.count-=1
                self.size-=1
                return True
            elif cardToRemove and cardToRemove.count==1:
                self.remove(cardToRemove)
                self.size-=1
                return True
            else:
                return False
        elif self.size == 1 and cardToRemove:
            self.root = None
            self.size=0
            return True
        else:
            return False
    def splice_out(self,c):
        if c.is_leaf():
            if c.is_left():
                c.parent.left = None
            else:
                c.parent.right = None
        elif c.right or c.left:
            if c.left:
                if c.is_left():
                    c.parent.setLeft(c.left)
                else:
                    c.parent.setRight(c.left)
                c.left.setParent(c.parent)
            else:
                if c.is_left():
                    c.parent.setLeft(c.right)
                else:
                    c.parent.setRight(c.right)
                c.right.setParent(c.parent)
#remove will only be called in the case that a card to be deleted has only 1 count
    def remove(self, currentCard):
        #no child
        if currentCard.is_leaf():
            if currentCard.is_left():
                currentCard.parent.left = None
            else:
                currentCard.parent.right = None
        #two children
        elif currentCard.right and currentCard.left:
            succ = self.getSuccessor(currentCard.suit,currentCard.rank)
            if succ:
                self.splice_out(succ)
                currentCard.suit = succ.suit
                currentCard.rank = succ.rank
                currentCard.count =succ.count
        # one child
        else:
            if currentCard.left:
                if currentCard.is_left():
                    currentCard.left.parent=currentCard.parent
                    currentCard.parent.left = currentCard.left
                elif currentCard.is_right():
                    currentCard.left.parent = currentCard.parent
                    currentCard.parent.right = currentCard.left
                else:
                    currentCard.replace_card(currentCard.left.suit,
                                                                 currentCard.left.rank,
                                                                 currentCard.left.left,
                                                                 currentCard.left.right,
                                                                 currentCard.left.count)
            else:
                if currentCard.is_left():
                    currentCard.right.parent=currentCard.parent
                    currentCard.parent.left = currentCard.right
                elif currentCard.is_right():
                    currentCard.right.parent = currentCard.parent
                    currentCard.parent.right = currentCard.right
                else:
                    currentCard.replace_card(currentCard.right.suit,
                                                                 currentCard.right.rank,
                                                                 currentCard.right.left,
                                                                 currentCard.right.right,
                                                                 currentCard.right.count)
    def inOrder(self):
        if self.root:
            return self._inOrder(self.root)
        else:
            return ''
    def _inOrder(self,node):
        ret = ""
        if node:
            ret += self._inOrder(node.left)
            ret += node.__str__() 
            ret += self._inOrder(node.right)
        return ret
    def preOrder(self):
        if self.root:
            return self._preOrder(self.root)
        else:
            return ''
    def _preOrder(self,node):
        ret = ""
        if node:
            ret += node.__str__()
            ret += self._preOrder(node.left)             
            ret += self._preOrder(node.right)
        return ret
        


        
























        
