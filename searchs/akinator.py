from node import No

class Akinator:
    def __init__(self):
        self.root = No("É um animal?",
            yes=No("Cachorro"),
            no=No("Pedra")
        )

    def jogar(self):
        atual = self.root
        while not atual.is_folha():
            resposta = input(f"{atual.valor} (s/n): ").lower()

            if resposta == "s":
                atual = atual.yes
            else:
                atual = atual.no
        resposta = input(f"Você está pensando em: {atual.valor}? (s/n): ").lower()
        if resposta == "s":
            print("Acertei!")
        else:
            self.aprender(atual)

    def aprender(self, no_errado: No):
        resposta_correta = input("O que você estava pensando? ")

        pergunta = input(
            f"Digite uma pergunta que diferencie {resposta_correta} de {no_errado.valor}: "
        )

        resposta_para_correto = input(
            f"Para {resposta_correta}, qual seria a resposta? (s/n): "
        ).lower()
        novo_no = No(pergunta)

        if resposta_para_correto == "s":
            novo_no.yes = No(resposta_correta)
            novo_no.no = No(no_errado.valor)
        else:
            novo_no.no = No(resposta_correta)
            novo_no.yes = No(no_errado.valor)

        no_errado.valor = novo_no.valor
        no_errado.yes = novo_no.yes
        no_errado.no = novo_no.no