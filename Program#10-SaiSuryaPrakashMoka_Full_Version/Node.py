class Node:
    def __init__(self, word, count=1, color='red'):
        self.word = word
        self.count = count
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
