dati_pluviali = [
    ("Milano", [("Gennaio", "N/D"), ("Febbraio", 15), ("Marzo", 10), ("Maggio", 7), ("Giugno", 16)]),
    ("Monza", [("Gennaio", 3), ("Febbraio", 6), ("Marzo", 8), ("Maggio", "N/D"), ("Giugno", 11)]),
    ("Brescia", [("Gennaio", 14), ("Febbraio", "N/D"), ("Marzo", 9), ("Maggio", 2), ("Giugno", 6)])
]

def analisi_citta(citta_input):
    for citta, dati in dati_pluviali:
        if citta == citta_input:
            if len(dati) != 0:
                media = 0
                numMesi = 0
                max = -1
                meseMax = {}
                min = 1000000
                meseMin = {}
                for mese, valore_mm in dati:
                    if valore_mm != "N/D":
                        media += valore_mm
                        numMesi += 1
                        if valore_mm > max:
                            max = valore_mm
                            meseMax = {mese}
                        elif valore_mm == max:
                            meseMax.add(mese)
                        if valore_mm < min:
                            min = valore_mm
                            meseMin = {mese}
                        elif valore_mm == min:
                            meseMin.add(mese)
                len(tuple(meseMax))
                len(tuple(meseMin))
                return (media/numMesi, (max, tuple(meseMax)), (min, tuple(meseMin)))
            else:
                return (0, ("Non inserito", 0), ("Non inserito", 0))


while True:
    citta_input = input("Inserisci la citta da analizzare: ")
    controllo = False
    for citta, dati in dati_pluviali:
        if citta_input == citta:
            controllo = True
    if controllo:
        break
    else:
        print("Errore: inserire una citta disponibile")
citta_analizzata = analisi_citta(citta_input)

print(f"Media di {citta_input}: {citta_analizzata[0]}")
print(f"Precipitazione massima di {citta_input}: {citta_analizzata[1][0]} nei mesi {citta_analizzata[1][1]}")
print(f"Precipitazione minima di {citta_input}: {citta_analizzata[2][0]} nei mesi {citta_analizzata[2][1]}")
            
            

