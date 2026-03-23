from collections import deque

class Node:
    def __init__(self, parent=None):
        self.parent = parent

class Question(Node):
    def __init__(self, parent=None, question, keyword, yes=None, no=None):
        super().__init__(parent)
        self.question = question
        self.keyword = keyword
        self.yes = yes
        self.no = no

class Answer(Node):
    def __init__(self, parent, answer):
        super().__init__(parent)
        self.answer = answer

class Akinator:
    def __init__(self):
        self.root = None
        self.leaf = []

