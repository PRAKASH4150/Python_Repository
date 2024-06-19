from Node import *
import json
class RedBlackTree:
    def __init__(self):
        self.TNULL = Node("", color='black')
        self.root = self.TNULL

    def load_text_file(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return text

    def decompose_text(self, text):
        words = text.lower().split()
        words = [word.strip('.,!?;:"()[]') for word in words]
        return words

    def add_word(self, word):
        self.insert(word)

    def find_word(self, word):
        node = self.search_tree_helper(self.root, word)
        if node:
            return node.count
        else:
            return 0

    def gather_stats(self):
        max_word, max_count = "", 0
        min_word, min_count = "", float('inf')
        total_words = 0
        total_count = 0
        unique_words = 0
        
        def in_order_traversal(node):
            nonlocal max_word, max_count, min_word, min_count, total_words, total_count, unique_words
            if node != self.TNULL:
                in_order_traversal(node.left)
                total_words += 1
                total_count += node.count
                unique_words += 1
                if node.count > max_count:
                    max_word, max_count = node.word, node.count
                if node.count < min_count:
                    min_word, min_count = node.word, node.count
                in_order_traversal(node.right)
        
        in_order_traversal(self.root)
        average_count = total_count / unique_words if unique_words > 0 else 0
        stats = {
            "max_word": max_word,
            "max_count": max_count,
            "min_word": min_word,
            "min_count": min_count,
            "total_words": total_words,
            "unique_words": unique_words,
            "average_count": average_count,
            "tree_depth": self.get_tree_depth()
        }
        return stats

    def get_tree_depth(self):
        def depth_helper(node):
            if node == self.TNULL:
                return 0
            left_depth = depth_helper(node.left)
            right_depth = depth_helper(node.right)
            return max(left_depth, right_depth) + 1
        return depth_helper(self.root)

    def save_tree(self, file_path):
        def serialize_node(node):
            if node == self.TNULL:
                return None
            return {
                "word": node.word,
                "count": node.count,
                "color": node.color,
                "left": serialize_node(node.left),
                "right": serialize_node(node.right)
            }
        with open(file_path, 'w') as file:
            json.dump(serialize_node(self.root), file, indent=4)

    def insert(self, word):
        # Ordinary BST insert
        node = Node(word)
        node.left = self.TNULL
        node.right = self.TNULL
        node.parent = None

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if word == x.word:
                x.count += 1
                return
            elif node.word < x.word:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.word < y.word:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 'black'
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def delete_node(self, word):
        self.delete_node_helper(self.root, word)

    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.word == key:
                z = node

            if node.word <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Word not found in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.word:
            return node

        if key < node.word:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent