from collections import deque
import json

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
        self.leaf = deque()

    def load_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    
        def build_tree(node_data, parent=None):
            if node_data['type'] == 'question':
                node = Question(
                    parent=parent,
                    question=node_data['question'],
                    keyword=node_data['keyword']
                )
                node.yes = build_tree(node_data['yes'], node)
                node.no = build_tree(node_data['no'], node)
            else:  # answer
                node = Answer(parent=parent, answer=node_data['answer'])
                self.leaf.append(node)
            return node
    
        self.root = build_tree(data)
    def BFS(self):
        lista = deque([self.root])
        result = deque()

        while lista:
            pointer = lista.popleft()
            result.append(pointer)
            if isinstance(pointer, Question):
                if pointer.yes is not None:
                    lista.append(pointer.yes)
                if pointer.no is not None:
                    lista.append(pointer.no)
        return result
    def DFS(self):
        def recursive(lista, node):
            if node is None:
                return
            lista.append(node)
            if isinstance(node, Question):
                if node.yes is not None:
                    recursive(lista, node.yes)
                if node.no is not None:
                    recursive(lista, node.no)
        lista = deque()
        recursive(lista, self.root)
        return lista


