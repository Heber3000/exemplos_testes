from projeto.ex1 import soma,subtracao,multi,divisao

import pytest

def test_soma():
    assert 4 == soma(1,3)

def test_subtracao():
    assert -2 == subtracao(1,3)

def test_multi():
    assert 3 == multi(1,3)

def test_divisao():
    assert 1/3 == divisao(1,3)