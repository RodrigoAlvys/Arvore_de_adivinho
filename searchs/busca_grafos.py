from collections import deque

def BFS(root: "None | No") -> deque["No"]:
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

def recur_dfs(no: "No", lista: deque["No"]) -> None:
    lista.append(no)
    if no.yes is not None:
        recur_dfs(no.yes, lista)
    if no.no is not None:
        recur_dfs(no.no, lista)
    return
def DFS(root: "None | No") -> deque["No"]:
    if root is None:
        return deque()
    lista = deque()
    recur_dfs(root, lista)
    return lista
    
