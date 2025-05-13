class Libro:
    def __init__(self, isbn, titolo, autore, anno):
        self.isbn = isbn
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    def __str__(self):
        return f"{self.titolo} di {self.autore} ({self.anno}) - ISBN: {self.isbn}"


class Biblioteca:
    def __init__(self):
        self.lista_libri = []

    def aggiungi_libro(self, libro):
        if len(self.lista_libri) != 0:
            for lib in self.lista_libri:
                if libro.isbn == lib.isbn:
                    print("Errore: isbn già presente")
                    return
        print("Libro aggiunto con successo")
        self.lista_libri.append(libro)

    def rimuovi_libro(self, isbn):
        if len(self.lista_libri) != 0:
            for libro in self.lista_libri:
                if libro.isbn == isbn:
                    self.lista_libri.remove(libro)
                    print(f"Libro {str(libro)} rimosso con successo.")
                    return
            print(f"Libro con ISBN {isbn} non trovato")
        else:
            print("Biblioteca vuota")

    def elenco_libri(self):
        if len(self.lista_libri) != 0:
            lista = ""
            for libro in self.lista_libri:
                lista += str(libro) + "\n"
            return lista
        else:
            return "Biblioteca vuota"

    def cerca_libro(self, isbn):
        if len(self.lista_libri) != 0:
            for libro in self.lista_libri:
                if libro.isbn == isbn:
                    return str(libro)
            return None
        else:
            print("Biblioteca vuota")
            return None

def input_isbn():
    while True:
        isbn = int(input("Inserisci isbn: "))
        if isbn < 1000000000000:
            print("Errore: isbn deve avere almeno 13 cifre")
        else:
            return isbn

def input_titolo():
    titolo = input("Inserisci il titolo del libro: ")
    return titolo

def input_autore():
    autore = input("Inserisci l'autore del libro: ")
    return autore

def input_anno():
    while True:
        anno = int(input("Inserisci l'anno del libro: "))
        if anno < 0:
            print("Errore: anno minore di 0")
        else:
            return anno
        
def input_libro():
    isbn = input_isbn()
    titolo = input_titolo()
    autore = input_autore()
    anno = input_anno()
    return Libro(isbn, titolo, autore, anno)

def aggiungi_libro():
    libro = input_libro()
    biblioteca.aggiungi_libro(libro)

def rimuovi_libro():
    isbn = input_isbn()
    print(f"Rimozione del libro con ISBN {isbn}:")
    biblioteca.rimuovi_libro(isbn)
    print("\nLibri presenti dopo la tentata rimozione:")
    print(biblioteca.elenco_libri())
    
def elenco_libri():
    print("Libri presenti in biblioteca:")
    print(biblioteca.elenco_libri())
    
def cerca_libro():
    isbn = input_isbn()
    print(f"Ricerca del libro con ISBN {isbn}:")
    libro = biblioteca.cerca_libro(isbn)
    print(libro) if libro != None else print("Il libro cercato non esiste")
        
biblioteca = Biblioteca()

while True:
    print()
    print("- Biblioteca")
    print("1 - Aggiungi Libro")
    print("2 - Rimuovi Libro")
    print("3 - Elenco Libri")
    print("4 - Cerca Libro")
    print("0 - ESCI")
    metodo = int(input("Cosa vuoi fare: "))
    print()
    if metodo == 1:
        aggiungi_libro()
    elif metodo == 2:
        rimuovi_libro()
    elif metodo == 3:
        elenco_libri()
    elif metodo == 4:
        cerca_libro()
    elif metodo == 0:
        print("Chiudendo il programma")
        break
    else:
        print("Metodo inserito non valido")
        
