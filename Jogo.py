def cabecalho(string):
    print('=' * len(string))
    print(  string)
    print('=' * len(string))


def geraDicionario():
    """
    Gera um dicionario com todas as palavras do arquivo txt
    :return: a lista 
    """

    dicionario = []
    arq = open('PALAVRAS.txt', 'r')
    for palavra in arq:
        separado = palavra.split()
        #print(separado[0])
        dicionario.append(separado[0]) #0 -> vai ser uma de cada vez
    arq.close()
    return dicionario



def recebeFrase():
    """
    Analise para evitar palavras com caracteres especiais
    e palavras sem '*'
    :return: Frase correta
    """
    while True:
        frase = input('Digite uma frase com letras e (*) para caracteres desconhecios: ').upper().strip()
        ok = True
        for char in frase:
            if not 'a' <= char <= 'z' and not 'A' <= char <= 'Z' and char != '*' and char != ' ':
                ok = False
            elif not '*' in frase:
                ok = False
        if ok:
            break
        else:
            print('Não digite letras e simbolos especiais...')
    return frase

def procuraPalavra(frase_a_ser_analisada):
    """
    Salvamento de palavras com '*'
    :param frase_a_ser_analisada: A frase digitada pelo usuario pós filtrada
    :return: lista contendo as palavras com '*'
    """
    frase = frase_a_ser_analisada.split()
    analise = []
    #analise das palavras separadamente
    for palavra in frase: #frase = split da frase
        if '*' in palavra:
            analise.append(palavra)
    return analise

def separaPorTamanho(dicionario, palavras):
    """
    Separa por tamanho as listas do dicionario de palavras
    :param dicionario: Lista gigante com palavras em potencial
    :param palavras: lista com palavras separadas com '*' digitadas pelo usuario
    :return: lista com palavras com o mesmo numero de caracteres das separadas com '*'
    """
    for item in dicionario:
        for vetor in palavras:
            if len(item) == len(vetor): #se o numero de char em uma palavra do dicionario for igual ao da palavra da frase ela é separada
                msm_num_char.append(item)
    return msm_num_char

def facilitando_problema(palavras_c_mesmo_num_carac):
    """
    Salva o conjunto de letras de cada palavra em uma lista
    :param palavras_c_mesmo_num_carac: lista com as palavras com o len == as das palavras com *
    :return: uma lista em que cada índice é uma lista contendo as letras das mesmas como seu indice
    """
    for item in palavras_c_mesmo_num_carac:
        letras_das_palavras_parecidas.clear()
        for letras in item:
            letras_das_palavras_parecidas.append(letras)
        lista_letras_das_palavras_parecidas.append(letras_das_palavras_parecidas[:])
    return lista_letras_das_palavras_parecidas


def facilitando_problema2(palavras_asterisco):
    """
    Colococa as letras das palavras da frase digitada pelo usuário em uma lista
    :param palavras_asterisco: uma lista com as palavras do usuario(pó-filtrada)
    :return: void
    """
    split_palavras = []
    for palavras in palavras_asterisco:
        split_palavras.clear()
        for letras in palavras:
            split_palavras.append(letras)
        lista_letras_das_palavras_asterisco.append(split_palavras[:])

def acheiPalavras(lista_letras_das_palavras_parecidas, lista_letras_das_palavras_asterisco):
    """

    :param lista_letras_das_palavras_parecidas:Lista com as letras das palavras do dicionario com o mesmo numero de char
    :param lista_letras_das_palavras_asterisco:Lista com as letras das palavras da frase digitada pelo usuário
    :return:
    """
    for pos, letras in enumerate(lista_letras_das_palavras_parecidas):
        for items in lista_letras_das_palavras_asterisco:
            ok = True
            if len(items) == len(letras):
                c = 0
                while True:
                    if c == len(letras):
                        lista_achei.append(lista_letras_das_palavras_parecidas[pos])#insere a palavra
                        break
                    if letras[c] == items[c] or items[c] == '*':
                        c += 1
                        ok = True
                    else:
                        ok = False
                        break
            else:
                ok = False




#variaveis
lista_palavras = []
analise_primaria = []
analise_len = []
msm_num_char = []
letras_das_palavras_parecidas = []#complemento da lista de letras abaixo
lista_letras_das_palavras_parecidas = []
lista_letras_das_palavras_asterisco = []
lista_achei = []
#fim_variaveis

#PROGRAMA PRINCIPAL (main)
lista_palavras = geraDicionario() #O dicionario passa pra ca
frase = recebeFrase()
lista_palavras_com_asterisco = procuraPalavra(frase)
lista_com_palavras_do_dicionario = separaPorTamanho(lista_palavras, lista_palavras_com_asterisco) #separacao de palavreas com potencial
lista_com_letras_potencial = facilitando_problema(lista_com_palavras_do_dicionario) #separada por palavras
facilitando_problema2(lista_palavras_com_asterisco)
acheiPalavras(lista_letras_das_palavras_parecidas, lista_letras_das_palavras_asterisco)
cabecalho('As palavras podem ser :')


if not len(lista_achei) == 0:
    for pos, letras in enumerate(lista_achei):
        for c in range(0, len(letras)):
            if c == len(letras) - 1:
                print(letras[c])
            else:
                print(letras[c], end='')
else:
    print('Desalpe :( ')
    add = str(input('Nosso banco de palavras não pode achar sua requisicao. Pode informar a palavra que almejava? ')).upper().strip()
    a = open('PALAVRAS.txt', 'a')
    a.write(f'\n{add}')
