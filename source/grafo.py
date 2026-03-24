from collections import deque
from time import sleep
import json

class Node:
    def __init__(self, keyword, parent=None):
        self.parent = parent
        self.keyword = keyword

class Question(Node):
    def __init__(self, question, keyword, parent=None, yes=None, no=None):
        super().__init__(keyword, parent)
        self.question = question
        self.yes = yes
        self.no = no

class Answer(Node):
    def __init__(self, parent, answer, keyword):
        super().__init__(keyword, parent)
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
                    question=node_data['question'],
                    keyword=node_data['keyword'],
                    parent=parent
                )
                node.yes = build_tree(node_data['yes'], node)
                node.no = build_tree(node_data['no'], node)
            else:  # answer
                node = Answer(
                        parent=parent, 
                        answer=node_data['answer'], 
                        keyword=node_data['keyword']
                        )
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
    def start(self):
        if self.root is None:
            print("A árvore está vazia! porfavor utilize a função load_json para preenchê-la")
            return
        print("Seja bem vindo ao Akinator rudimentar!!\n")
        print("Para começar, pense em um animal")
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print("\n\nEstá pronto para responder as perguntas?")
        print("Para sair basta digitar \"sair\"")
        input("...")

        pointer = self.root

        while isinstance(pointer, Question):
            x = ""
            print(f"\n{pointer.question}")
            print("Responda com s para sim ou n para não")
            while x not in ["s", "n"]:
                x = input("-> ").lower().strip()
                if x == "sair":
                    return
                elif x not in ["s", "n"]:
                    print("\nPor favor, digite s ou n\nSé deseja sair, digite \"sair\"")
            if x == "s":
                if pointer.yes is None:
                    print("Erro! Árvore incompleta.")
                    input("...")
                    return
                pointer = pointer.yes
            else:
                if pointer.no is None:
                    print("Erro! Árvore incompleta.")
                    input("...")
                    return
                pointer = pointer.no
        if isinstance(pointer, Answer):
            print("\n\n\n\n")
            print("=x=" * 17)
            print(f"\nO animal que você estava pensando é {pointer.answer}\n")
            print("=x=" * 17)
            print("\nMuito obrigado por testar esse programa!!!")
        else:
            print("não foi possível chegar a uma conclução.")
        input("enter para sair...")

        

