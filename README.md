# Akinator - Árvore de Decisão em Python

Um jogo de adivinhação onde o programa tenta adivinhar o que o usuário está pensando através de perguntas de sim/não, utilizando uma árvore de decisão binária.

## Sobre o Projeto

Este projeto implementa um sistema de adivinhação baseado em árvore de decisão. O usuário responde perguntas com "sim" ou "não", e o sistema navega pela árvore até chegar a uma resposta final.

### Conceitos Implementados
- **Árvore Binária de Decisão**: Estrutura onde cada nó de pergunta possui dois ramos (sim/não)
- **Busca em Largura (BFS)**: Percorre a árvore nível por nível
- **Busca em Profundidade (DFS)**: Percorre a árvore até o fundo antes de retroceder
- **Serialização JSON**: Carregamento da árvore de decisão a partir de arquivos

## Funcionalidades

- **Jogo Interativo**: Sistema faz perguntas e adivinha a resposta
- **Comparação de Algoritmos**: Compare performance entre BFS e DFS
- **Carregamento de Árvores**: Suporte a arquivos JSON para diferentes árvores de decisão
- **Visualização de Caminhos**: Veja a ordem de visitação dos nós em cada algoritmo

## Estrutura da Árvore

A árvore de decisão é composta por dois tipos de nós:

- **Question**: Representa uma pergunta, com ramos `yes` e `no`
- **Answer**: Representa uma resposta final (folha da árvore)

### Nomenclatura dos Keywords

Os nós utilizam o formato `[profundidade]_[identificador]`:

| Componente | Descrição | Exemplo |
|------------|-----------|---------|
| profundidade | Nível do nó na árvore (0 = raiz) | `0`, `1`, `2` |
| identificador | Nome descritivo do nó | `vertebrado`, `mamifero`, `cachorro` |

**Exemplos:**
- `0_vertebrado` - Nó raiz (pergunta sobre vertebrados)
- `1_aquatico` - Pergunta na profundidade 1
- `3_peixe` - Resposta na profundidade 3

## Algoritmos de Busca

### BFS (Busca em Largura)
- Percorre a árvore nível por nível
- Utiliza uma fila (`deque`) para gerenciar os nós
- Ordem de visitação: raiz → nível 1 → nível 2 → ...

### DFS (Busca em Profundidade)
- Percorre a árvore até o fundo antes de retroceder
- Implementação recursiva
- Ordem de visitação: vai descendo pelo ramo `yes` até encontrar uma resposta

### Comparação

| Aspecto | BFS | DFS |
|---------|-----|-----|
| Complexidade de Tempo | O(n) | O(n) |
| Complexidade de Espaço | O(w)* | O(h)** |
| Implementação | Iterativa (fila) | Recursiva |

*w = largura máxima da árvore  
**h = altura da árvore

## Estrutura de Dados

### Node (Classe Base)
- `parent`: Referência ao nó pai
- `keyword`: Identificador único do nó

### Question (herda Node)
- `question`: Texto da pergunta
- `yes`: Ramo para resposta SIM
- `no`: Ramo para resposta NÃO

### Answer (herda Node)
- `answer`: Texto da resposta final
## Créditos
- Rodrigo Alves Barboza da Silva
- Luiz Arthur da Silva Costa
