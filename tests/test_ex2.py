from projeto.ex2 import Usuario

def test_qte_usuario():
    lista = []
    usuario1 = Usuario('Heber',39924463,'heberlevy@gmail.com')
    lista.append(usuario1)
    usuario2 = Usuario('Levy',99999999,'levy1990@gmail.com')
    lista.append(usuario2)
    assert len(lista) > 0


def test_listar_usuarios():
    test = Usuario.listar_usuarios
    assert test is not None




