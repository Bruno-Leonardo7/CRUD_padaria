def validacaoNum(texto):
    try:
        num = float(texto.replace(',','.'))
    except:
        return 0
    else:
        return num