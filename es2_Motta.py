tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 123)),
        ("marzo", ("gas", 234)),
        ("maggio", ("elettrico", 65)),
        ("maggio", ("gas", 234)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 234)),
        ("marzo", ("gas", 321)),
    ]),
    ("Monza", [
        ("gennaio", ("elettrico", 463)),
        ("gennaio", ("gas", 342)),
    ]),
    ("Como", [
        ("gennaio", ("elettrico", 123)),
        ("gennaio", ("gas", 231)),
        ("febbraio", ("elettrico", 98)),
        ("febbraio", ("gas", 231)),
        ("marzo", ("elettrico", 78)),
        ("marzo", ("gas", 111)),
    ]),
)

def analizza_consumi_energetici(input_citta, input_risorsa):
    media = 0
    cont = 0
    max = 0
    mese_max = {}
    for citta, dati in tupla_consumi_energetici:
        if citta == input_citta:
            for mese, (tipologia, consumo) in dati:
                if tipologia == input_risorsa:
                    media += consumo
                    cont += 1
                    if consumo > max:
                        max = consumo
                        mese_max = {mese}
                    elif consumo == max:
                        mese_max.add(mese)
    return (media/cont, (max, tuple(mese_max)))
        

controllo_citta = True
while controllo_citta:
    input_citta = input("Inserisci la città da analizzare: ")
    for citta, dati in tupla_consumi_energetici:
        if citta == input_citta:
            controllo_citta = False
    if controllo_citta:
        print("Errore: citta inserita non valida")

controllo_risorsa = True
while controllo_risorsa:
    input_risorsa = input("Inserisci la tipologia della risorsa da analizzare: ")
    for citta, dati in tupla_consumi_energetici:
        for mese, (tipologia, consumo) in dati:
            if tipologia == input_risorsa:
                controllo_risorsa = False
    if controllo_risorsa:
        print("Errore: tipologia inserita non valida")

print(analizza_consumi_energetici(input_citta, input_risorsa))