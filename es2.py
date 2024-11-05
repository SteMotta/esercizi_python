tupla_vendite = (
        (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
        (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
        (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
        (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
        (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
        (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
        (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
        (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
    )

def media_globale(tupla_vendite):
    media = 0
    for sezione, dati_vendita in tupla_vendite:
        media += dati_vendita[1][1]
    return media/len(tupla_vendite) if len(tupla_vendite) > 0 else 0

def media(tupla_vendite, categoria_input, tipologia_pagamento_input):
    media = 0
    num_vendite = 0
    for sezione, dati_vendita in tupla_vendite:
        if sezione[1] == categoria_input and dati_vendita[1][0] == tipologia_pagamento_input:
            media += dati_vendita[1][1]
            num_vendite += 1
    return media/num_vendite if num_vendite > 0 else 0

