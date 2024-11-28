def Aggiunta():
    print("Inserire il titolo del libro che si vuole aggiungere:")
    libro_da_aggiungere = input()
    return libro_da_aggiungere

def Elenco_libri(lista_dei_libri):
    print("L' elenco dei libri è il seguente")
    for libro in lista_dei_libri:
        print("-",libro)

def Elenco_libri_disponibili(lista_libri,lista_libri_prestati):
    lista_libri_disponibili=[]
    
    for libro in lista_libri:
        if libro not in lista_libri_prestati:
            lista_libri_disponibili.append(libro)
    return lista_libri_disponibili
    
def Elenco_libri_prestati(lista_libri_prestati):
    print("L' elenco dei libri prestati:")
    for libro in lista_libri_prestati:
        print("-",libro)

def Prestito():
    print("Quale libro vuoi prendere in prestito?")
    libro_richiesto = input()
    return libro_richiesto

def Restituzione():
    print("Quale libro vuoi restituire?")
    libro_da_restituire = input()
    return libro_da_restituire