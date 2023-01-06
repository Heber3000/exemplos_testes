from projeto.ex5 import Usuario


def test_dados():
    x = Usuario('Heber', 39924463, 'heberlevy@hotmail.com')
    return x.dados_usuario().values() is not None







