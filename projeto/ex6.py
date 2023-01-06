from random import randint


def dados_numerico():
    lista = []

    for i in range(100):
        lista.append(randint(1, 100))

    return lista


def media():
    lista = []

    for i in range(100):
        lista.append(randint(1, 100))

    return sum(lista)/len(lista)



if __name__ == '__main__':
    print(dados_numerico())
    print(media())

