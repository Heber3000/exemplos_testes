import math
class EquacaoDoSegundoGrau:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calculo_delta(self):
        if self.a == 0:
            return f'Não é equação do segundo grau'
        else:
            self.delta = (math.pow(self.b, 2) - 4 * self.a * self.c)
            if self.delta < 0:
                return f'Não há raízes'
            elif self.delta == 0:
                return f'Só há uma raiz {"%.2f" % float((-self.b + math.sqrt(self.delta)) / self.a * 2)}'
            else:
                return f'Há duas raizes {"%.2f" % float((-self.b + math.sqrt(self.delta)) / self.a * 2)},{"%.2f" % float((-self.b - math.sqrt(self.delta)) / self.a * 2)}'
