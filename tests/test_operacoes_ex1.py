from projeto.ex1 import soma,subtracao,multi,divisao
import pytest

@pytest.mark.operacoes
class TestOperacoes:

    def test_soma(self):
        assert soma(1,3) == 4

    def test_subtracao(self):
        assert subtracao(1,3) == -2

    def test_multi(self):
        assert multi(1,3) == 3

    def test_divisao(self):
        assert divisao(1,3) == 1/3
