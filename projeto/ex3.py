class CarrinhoSuperMercado:
    def __init__(self,produto):
        self.produto = produto
        self.lista = []


    def adicionar_no_carrinho(self,produto):
        self.produto = produto

        self.lista.append(self.produto)
        return self.lista

    def qtd_itens_carrinho(self):
        return len(self.lista)









