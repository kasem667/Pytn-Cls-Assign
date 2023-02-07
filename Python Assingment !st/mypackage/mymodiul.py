def add(*numbers):
    suma = 0
    for i in numbers:
        suma += i
    return suma


def even_1_to_n(x):

    lista = []
    for i in range(1, x+1):
        if i % 2 == 0:
            lista.append(i)
    return lista


Bangladesh = "The name of our country is Bangladesh. I love this country very much. It is a small country. Prime minister is a Sheik Hasina. President is a Abdul Hamid. And Educational Minister is a Dr. Diphu Moni child of Moneky. "


def about_bangladesh():
    return Bangladesh


