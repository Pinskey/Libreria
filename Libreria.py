import Libro_a_casa

lista_dei_libri = []
lista_libri_prestati = []

while True:
    if len(lista_dei_libri) == 0:
        print("La libreria è vuota. Aggiungi il primo libro")
        lista_dei_libri.append(Libro_a_casa.Aggiunta())
    else:
        print("Selezionare cosa fare:")
        print("1) Aggiungere un libro\n2) Stampa a schermo la libreria\n3) Disponibilità libreria\n4) Libro in prestito")
        print("5) Restituzione\n6) Exit")
        scelta_funzione = int(input())
        if (scelta_funzione == 1):
            lista_dei_libri.append(Libro_a_casa.Aggiunta())
        elif (scelta_funzione == 2):
            Libro_a_casa.Elenco_libri(lista_dei_libri)
        elif(scelta_funzione==3):
            print("I libri disponibili sono:")
            for libro in Libro_a_casa.Elenco_libri_disponibili(lista_dei_libri,lista_libri_prestati):
                print("-",libro)
        elif (scelta_funzione==4):
            lista_libri_prestati.append(Libro_a_casa.Prestito())
        elif (scelta_funzione==5): 
            lista_libri_prestati.remove(Libro_a_casa.Restituzione())
        else:
            break