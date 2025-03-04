import random
import pprint
pp=pprint.PrettyPrinter(indent=4)

# 1. Popolamento statico iniziale:
diz_chef = {
    "Mario Rossi": [("Antipasti", (8, 7, 9), "Junior Chef"), ("Primi", (7, 8, 8), "Junior Chef"), ("Secondi", (9, 9, 8), "Junior Chef"), ("Dessert", (8, 8, 9), "Junior Chef")],
    "Luigi Bianchi": [("Antipasti", (7, 7, 8), "Senior Chef"), ("Primi", (8, 9, 7), "Senior Chef"), ("Secondi", (7, 8, 7), "Senior Chef"), ("Dessert", (9, 8, 8), "Senior Chef")],
    "Giulia Verdi": [("Antipasti", (9, 8, 8), "Junior Chef"), ("Primi", (8, 7, 9), "Junior Chef"), ("Secondi", (8, 8, 8), "Junior Chef"), ("Dessert", (7, 9, 8), "Junior Chef")]
}

# 2. Aggiunta statica di un nuovo chef:
diz_chef["Stefano Motta"] = [("Antipasti", (5, 9, 5), "Senior Chef"), ("Primi", (2, 6, 8), "Senior Chef"), ("Secondi", (8, 3, 5), "Senior Chef"), ("Dessert", (5, 6, 5), "Senior Chef")]

# 3. Funzione per l'aggiunta di una nuova categoria di piatto:
def nuova_cat():
    for chef in diz_chef.keys():
        diz_chef[chef].append(("Piatti unici", (random.randint(1,10), random.randint(1,10), random.randint(1,10)), diz_chef[chef][0][2]))

# 4. Funzione per la stampa dati di uno chef:
def stampa_dati(nome_chef):
    if nome_chef in diz_chef.keys():
        print(f"Categoria dello chef: {diz_chef[nome_chef][0][2]}")
        print(f"Nome cognome: {nome_chef}")
        for categoria_piatto, (creativita, gusto, presentazione), _ in diz_chef[nome_chef]:
            print(f"Punteggi {categoria_piatto}:")
            print(f"Creatività = {creativita}")
            print(f"Gusto = {gusto}")
            print(f"Presentazione = {presentazione}")

    else:
        print("Errore: chef non presente")

# 5. Funzione per la stampa dati di un piatto:
def stampa_dati_piatto(cat_piatto):
    controllo_esistenza = False
    for chef in diz_chef.keys():
        for categoria_piatto, (creativita, gusto, presentazione), categoria_chef in diz_chef[chef]:
            if categoria_piatto == cat_piatto:
                controllo_esistenza = True
                print(f"Nome cognome: {chef}")
                print(f"Categoria dello chef: {categoria_chef}")
                print(f"Punteggi {categoria_piatto}:")
                print(f"Creatività = {creativita}")
                print(f"Gusto = {gusto}")
                print(f"Presentazione = {presentazione}")

    if not controllo_esistenza:
        print("Errore: categoria piatto non presente")

# 6. Funzione per l'analisi dei punteggi:
def punteggio_totale(diz_chef, cat_piatto, cat_chef):
    controllo_piatto = False
    controllo_chef = False
    for chef in diz_chef.keys():
        for categoria_piatto, (creativita, gusto, presentazione), categoria_chef in diz_chef[chef]:
            if categoria_piatto == cat_piatto:
                controllo_piatto = True
            if categoria_chef == cat_chef:
                controllo_chef = True


    if controllo_piatto and controllo_chef:
        lista_nominativi = []
        somma_punteggi = 0

        for chef in diz_chef.keys():
            for categoria_piatto, (creativita, gusto, presentazione), categoria_chef in diz_chef[chef]:
                if categoria_piatto == cat_piatto and categoria_chef == cat_chef:
                    somma_punteggi += creativita + gusto + presentazione
                    lista_nominativi.append(chef)

        print(f"Somma totale: {somma_punteggi}")
        print("Lista chef:")
        for chef in lista_nominativi:
            print(chef)
        return (somma_punteggi, lista_nominativi)
    
    elif not controllo_piatto and not controllo_chef:
        print("Errore: tutti e due i parametri non esistenti")
    elif not controllo_piatto and controllo_chef:
        print("Errore: piatto inserito non esistente")
    elif controllo_piatto and not controllo_chef:
        print("Errore: chef non esistente")

def media_totale(diz_chef, cat_piatto, cat_chef):
    controllo_piatto = False
    controllo_chef = False
    for chef in diz_chef.keys():
        for categoria_piatto, (creativita, gusto, presentazione), categoria_chef in diz_chef[chef]:
            if categoria_piatto == cat_piatto:
                controllo_piatto = True
            if categoria_chef == cat_chef:
                controllo_chef = True


    if controllo_piatto and controllo_chef:
        lista_nominativi = []
        somma_punteggi = 0
        conta = 0
        for chef in diz_chef.keys():
            for categoria_piatto, (creativita, gusto, presentazione), categoria_chef in diz_chef[chef]:
                if categoria_piatto == cat_piatto and categoria_chef == cat_chef:
                    somma_punteggi += creativita + gusto + presentazione
                    lista_nominativi.append(chef)
                    conta += 3

        media = (somma_punteggi/conta)
        print(f"Media totale: {media:.2f}")
        print("Lista chef:")
        for chef in lista_nominativi:
            print(chef)
        return (media, lista_nominativi)
    
    elif not controllo_piatto and not controllo_chef:
        print("Errore: tutti e due i parametri non esistenti")
    elif not controllo_piatto and controllo_chef:
        print("Errore: piatto inserito non esistente")
    elif controllo_piatto and not controllo_chef:
        print("Errore: chef non esistente")

# 7. Funzione per l'aggiunta di un nuovo chef:
def inserisci_dati_nuovo_chef():
    lista_categorie_piatti = ["Antipasti", "Primi", "Secondi", "Dessert", "Patti unici"]
    lista_dati = []
    cat_chef = input_cat_chef()
    for cat_piatto in lista_categorie_piatti:
        print(f"Inserisci voti {cat_piatto}")
        voti = input_voti()
        lista_dati.append((cat_piatto, voti, cat_chef))

    return lista_dati

def input_voti():
    lista_cat_voti = ["Creatività", "Gusto", "Presentazione"]
    lista_voti = []
    for cat_voto in lista_cat_voti:
        while True:
            voto = int(input(f"{cat_voto}: "))
            if voto < 1 or voto > 10:
                print("Errore: voto inserito non valido")
            else:
                lista_voti.append(voto)
                break

    return tuple(lista_voti)

def input_cat_chef():
    while True:
        input_cat = int(input("Quel è la categoria dello chef (1 = Junior Chef, 2 = Senior Chef): "))
        if input_cat != 1 and input_cat != 2:
            print("Errore: categoria scelta non valida")
        else:
            if input_cat == 1:
                return "Junior Chef"
            else:
                return "Senior Chef"
            
def input_chef():
    while True:
        nome = input("Inserici il nome dello chef: ")
        if len(nome) == 0:
            print("Errore: inserimento non valido")
        else:
            break

    while True:
        cognome = input("Inserici il cognome dello chef: ")
        if len(cognome) == 0:
            print("Errore: inserimento non valido")
        else:
            break
    
    return (nome, cognome)

def inserisci_nuovo_chef(diz_chef, tupla_nominativi, lista_risultati):
    if isinstance(tupla_nominativi, tuple) and len(tupla_nominativi) == 2:
        if isinstance(lista_risultati, list) and len(lista_risultati) == 5:
            controllo_tuple = True
            for obj in lista_risultati:
                if not isinstance(obj, tuple) and len(obj) != 3:
                    controllo_tuple = False
                    break
                elif not isinstance(obj[1], tuple):
                    controllo_tuple = False
                    break

            if controllo_tuple:
                controllo_voti = True
                for _, voti, _ in lista_risultati:
                    if len(voti) != 3:
                        controllo_voti = False
                        break

                if controllo_voti:
                    controllo_interi = True
                    for _, (voto1, voto2, voto3), _ in lista_risultati:
                        if not isinstance(voto1, int) or not isinstance(voto2, int) or not isinstance(voto3, int):
                            controllo_interi = False
                            break
                    
                    if controllo_interi:
                        nome, cognome = tupla_nominativi
                        if nome + " " + cognome in diz_chef.keys():
                            print("Errore: chef già esistente")
                        else:
                            diz_chef[nome + " " + cognome] = lista_risultati
                            print("Chef aggiunto correttamente")
                    else:
                        print("Errore: i voti non sono tutti interi")    
                else:
                    print("Errore: numero di voti non validi")  
            else:
                print("Errore: tuple lista risultati o tupla voti non valida")   
        else:
            print("Errore: lista risultati non valida")  
    else:
        print("Errore: tupla nominativi non valida")   

