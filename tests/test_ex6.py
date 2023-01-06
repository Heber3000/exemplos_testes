from projeto.ex6 import dados_numerico, media

def test_dados_numerico():
    x = dados_numerico()
    assert len(x) > 0


def test_media():
    y = media()
    assert y !=0



