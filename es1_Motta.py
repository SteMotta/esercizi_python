tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

def media_gol_partite(tupla_partite):
    media = 0
    for squadra_casa, squadra_ospite, punti_casa, punti_ospite in tupla_partite:
        media += punti_casa + punti_ospite
    
    return media/len(tupla_partite)

def media_gol_squadra(tupla_partite, squadra):
    media = 0
    num_partite = 0
    for squadra_casa, squadra_ospite, punti_casa, punti_ospite in tupla_partite:
        if squadra_casa == squadra:
            media += punti_casa
            num_partite += 1
        elif squadra_ospite == squadra:
            media += punti_ospite
            num_partite += 1

    return media/num_partite

def partita_con_piu_gol(tupla_partite):
    partita_max = ()
    max = 0
    for squadra_casa, squadra_ospite, punti_casa, punti_ospite in tupla_partite:
        if (punti_casa + punti_ospite) > max:
            max = (punti_casa + punti_ospite)
            partita_max = (squadra_casa, squadra_ospite, punti_casa, punti_ospite)
    
    return partita_max

def partita_con_meno_gol(tupla_partite):
    partita_min = ()
    min = 100
    for squadra_casa, squadra_ospite, punti_casa, punti_ospite in tupla_partite:
        if (punti_casa + punti_ospite) < min:
            min = (punti_casa + punti_ospite)
            partita_min = (squadra_casa, squadra_ospite, punti_casa, punti_ospite)
    
    return partita_min

def percentuale_vittorie_squadra(tupla_partite, squadra):
    num_partite = 0
    num_partite_vinte = 0
    for squadra_casa, squadra_ospite, punti_casa, punti_ospite in tupla_partite:
        if squadra_casa == squadra:
            if punti_casa > punti_ospite:
                num_partite += 1
                num_partite_vinte += 1
            else:
                num_partite += 1
        elif squadra_ospite == squadra:
            if punti_ospite > punti_casa:
                num_partite += 1
                num_partite_vinte += 1
            else:
                num_partite += 1

    return (num_partite_vinte/num_partite)*100

def stampa_tupla(tupla_partite):
    for squadra_casa, squadra_ospite, punti_casa, punti_ospite in tupla_partite:
        print(f"{squadra_casa} vs {squadra_ospite}, {punti_casa}:{punti_ospite}")

def input_squadra(tupla_partite):
    controllo_input = True
    while controllo_input:
        squadra_input = input("Che squadra vuoi inserire? ")
        for squadra_casa, squadra_ospite, *punti in tupla_partite:
            if squadra_casa == squadra_input or squadra_ospite == squadra_input:
                controllo_input = False
        if controllo_input:
            print("Errore: inserita squadra non disponibile")
    return squadra_input

print("Partite disputate:")
stampa_tupla(tupla_partite)

continuare = True
while(continuare):
    print("1 - Stampa media partite")
    print("2 - Stampa media squadra inserita")
    print("3 - Stampa partita con più gol")
    print("4 - Stampa partita con meno gol")
    print("5 - Stampa percentuale di vittoria della squadra inserita")
    while True:
        metodoInput = int(input("Che metodo vuoi eseguire? "))
        if metodoInput < 1 or metodoInput > 5:
            print("Errore: inserito metodo non valido")
        else:
            break
    
    if metodoInput == 1:
        print(f"La media dei gol = {media_gol_partite(tupla_partite):.1f}")
    elif metodoInput == 2:
        squadra_inserita = input_squadra(tupla_partite)
        print(f"La media dei gol della squadra {squadra_inserita} = {media_gol_squadra(tupla_partite, squadra_inserita):.1f}")
    elif metodoInput == 3:
        print(f"La partita con più gol = {partita_con_piu_gol(tupla_partite)}")
    elif metodoInput == 4:
        print(f"La partita con più gol = {partita_con_meno_gol(tupla_partite)}")
    else:
        squadra_inserita = input_squadra(tupla_partite)
        print(f"La percentuale di vittoria della {squadra_inserita} = {percentuale_vittorie_squadra(tupla_partite, squadra_inserita):.0f}%")
    
    continuare_input = int(input("Vuoi continuare?('1' per continuare) "))
    if continuare_input != 1:
        continuare = False