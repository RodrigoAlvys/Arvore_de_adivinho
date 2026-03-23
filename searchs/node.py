class No:
    def __init__(self, valor: str, yes: "No" = None, no: "No" = None):
        self.valor = valor
        self.yes = yes
        self.no = no

    def is_folha(self) -> bool:
        return self.yes is None and self.no is None