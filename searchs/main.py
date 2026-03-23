from akinator import Akinator
from collections import deque

def BFS(root):
    if root is None:
        return deque()
    lista = deque([root])
    resultado = deque()
    while lista:
        ponteiro = lista.popleft()
        resultado.append(ponteiro)
        if ponteiro.yes is not None:
            lista.append(ponteiro.yes)
        if ponteiro.no is not None:
            lista.append(ponteiro.no)
    return resultado

def recur_dfs(no, lista):
    if no is None:
        return
    lista.append(no)
    recur_dfs(no.yes, lista)
    recur_dfs(no.no, lista)

def DFS(root):
    if root is None:
        return deque()
    lista = deque()
    recur_dfs(root, lista)
    return lista

if __name__ == "__main__":
    jogo = Akinator()

    while True:
        print("\n1 - Jogar")
        print("2 - Mostrar árvore (BFS)")
        print("3 - Mostrar árvore (DFS)")
        print("0 - Sair")
        op = input("Escolha: ")

        if op == "1":
            jogo.jogar()
        elif op == "2":
            for no in BFS(jogo.root):
                print(no.valor)
        elif op == "3":
            for no in DFS(jogo.root):
                print(no.valor)
        elif op == "0":
            break