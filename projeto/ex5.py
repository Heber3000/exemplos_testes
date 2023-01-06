class Usuario:
    def __init__(self,nome,telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.dados = []




    def dados_usuario(self):

       dict = {'nome':self.nome,
               'telefone':self.telefone,
               'email':self.email}
       return dict
























