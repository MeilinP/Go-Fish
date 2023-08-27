from PlayerHand import PlayerHand
from Card import Card

# testing card
def test_Card():
    c1=Card('h','3')
    c2=Card('c','3')
    c3=Card('d','5')
    c4=Card('c','4')
    c1.left=c2
    c2.parent=c1
    c1.right=c3
    c3.parent=c1
    assert c1.__str__() == 'H 3 | 1\n'
    assert c2.is_left() == True
    assert c3.is_right() == True
    assert c1.is_root() == True
    assert not c1.is_leaf()
    assert c1.has_any_children
    c1.replace_card('c','4',c2,c3,1)
    assert c1.__str__()=='C 4 | 1\n'
    assert c1>c2
    assert c1<c3
    assert c1==c4
    assert c1.getRightChildMinCard() == c3
    
#testing PlayerHand
def test_basics():
    bst = PlayerHand()
    assert bst.root == None
    assert bst.size == 0
    bst.put('h', 'j')
    bst.put('d', 'a')
    bst.put('c', 'j')
    bst.put('s', '9')
    bst.put('h', 'k')
    bst.put('h', '6')
    bst.put('s', 'k')
    bst.put('s', 'q')
    bst.put('s', 'k')
    bst.put('c', 'j')
    bst.put('s', 'k')
    assert bst.getTotalCards() == 11
    assert bst.getMin().__str__() == 'D A | 1\n'
    assert not bst.isEmpty()
def test_treeManipulation():
    bst = PlayerHand()
    bst.put('h', 'j')
    bst.put('d', 'a')
    bst.put('c', 'j')
    bst.put('s', '9')
    bst.put('h', 'k')
    bst.put('h', '6')
    bst.put('s', 'k')
    bst.put('s', 'q')
    bst.put('s', 'k')
    bst.put('c', 'j')
    bst.put('s', 'k')
    assert bst.get('h','j').__str__() == 'H J | 1\n'
    assert bst.get('s','a')==None
    assert bst.getSuccessor('h','j').__str__() == 'S Q | 1\n'
    assert bst.getSuccessor('s','k') == None
    bst.delete('s','k')#delete node and testing preOrder()
    assert bst.preOrder() == \
	"""H J | 1
D A | 1
C J | 2
S 9 | 1
H 6 | 1
H K | 1
S Q | 1
S K | 2\n"""
    assert bst.delete('c','a') == False
    bst.delete('h', 'j')#delete root node and testing inOrder
    assert bst.inOrder() ==\
	"""D A | 1
H 6 | 1
S 9 | 1
C J | 2
S Q | 1
H K | 1
S K | 2\n"""


'''
bst.delete('h', 'j')
print(bst.preOrder())
bst.delete('s', 'q')
bst.delete('h', 'k')
bst.delete('s', 'k')
bst.delete('s', 'k')
bst.delete('s', 'k')
print(bst.preOrder())
bst.delete('d', 'a')
bst.delete('c', 'j')
print(bst.preOrder())
print(bst.size)
bst.delete('c', 'j')
bst.delete('s', '9')
print(bst.preOrder())
print(bst.size)#h6
bst.delete('h', '6')
print(bst.preOrder())
'''
'''
def test_bst_delete_root():
	bst = PlayerHand()
	bst.put('d', 'j')

	bst.delete('d', 'j')

	assert bst.root is None

	bst.put('h', 'j')
	bst.put('d', 'a')
	bst.put('c', 'j')
	bst.put('s', '9')
	bst.put('h', 'k')
	bst.put('h', '6')
	bst.put('s', 'k')
	bst.put('s', 'q')
	bst.put('s', 'k')
	bst.put('c', 'j')
	bst.put('s', 'k')

	assert bst.delete('h', 'j') is True

	assert bst.preOrder() == \
	"""S Q | 1
D A | 1
C J | 2
S 9 | 1
H 6 | 1
H K | 1
S K | 3\n"""

	bst.delete('s', 'q')
	bst.delete('h', 'k')
	bst.delete('s', 'k')
	bst.delete('s', 'k')
	bst.delete('s', 'k')

	assert bst.preOrder() == \
	"""D A | 1
C J | 2
S 9 | 1
H 6 | 1\n"""

	bst.delete('d', 'a')
	bst.delete('c', 'j')

	assert bst.preOrder() == \
	"""C J | 1
S 9 | 1
H 6 | 1\n"""

	bst.delete('c', 'j')
	bst.delete('s', '9')
	assert bst.delete('h', '6') is True

	assert bst.preOrder() == ""
'''





