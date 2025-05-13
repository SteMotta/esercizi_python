import math

class Pagella:
    def __init__(self, lista_voti):
        self.lista_voti = lista_voti
        
    def __repr__(self):
        if len(self.lista_voti) > 0:
            stringa_voti = ""
            for i, voto in enumerate(self.lista_voti):
                stringa_voti += f"Materia {i+1}: {voto}\n"
            return stringa_voti
        else:
            print("Lista vuota")
            
    def media(self):
        if len(self.lista_voti) > 0:
            somma = 0
            for i, voto in enumerate(self.lista_voti):
                somma += voto
            return somma/i
        else:
            print("Lista vuota")
            
    def __getitem__(self, indice):
        return self.lista_voti[indice]
    
    def __eq__(self, pagella):
        if (len(self.lista_voti) != len(pagella.lista_voti)):
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate")
            return None
        else:
            for voto1, voto2 in zip(self.lista_voti, pagella.lista_voti):
                if voto1 != voto2:
                    return False
            return True
        
    def __sub__(self, pagella):
        if (len(self.lista_voti) != len(pagella.lista_voti)):
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate")
            return None
        else:
            nuova_lista = []
            for voto1, voto2 in zip(self.lista_voti, pagella.lista_voti):
                nuova_lista.append(voto1-voto2) if voto1-voto2 >= 0 else nuova_lista.append(0)
            return nuova_lista
    
    def impegno(self):
        somma = 0
        for voto in self.lista_voti:
            somma += math.pow(voto, 2)
        return math.sqrt(somma)
        

pagella1 = Pagella([3, 4, 6, 3, 6, 7])
pagella2 = Pagella([3, 4, 6, 3, 6, 7])
pagella3 = Pagella([5, 2, 3, 7, 2, 3])

print(pagella1)
print(pagella1.media())
print(pagella1[1])

print(pagella1 == pagella2)
print(pagella1 - pagella3)

print(pagella1.impegno())
