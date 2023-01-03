from projeto.ex4 import EquacaoDoSegundoGrau


def test_equacao():
    equacao1 = EquacaoDoSegundoGrau(1,2,3)
    assert equacao1.calculo_delta != 0

def test_equacao2():
    equacao2 = EquacaoDoSegundoGrau(0,1,3)
    assert equacao2.calculo_delta() != str
