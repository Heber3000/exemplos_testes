class Usuario:

    def __init__(self,nome,telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuarios = []

    def qte_usuarios(self,usuario):
        contador = 0
        self.usuarios.append(usuario)
        for i in self.usuarios:
            contador += 1

        return contador

    def listar_usuarios(self):
        return self.usuarios














