import random

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

ZMAGA = "W"
PORAZ = "X"

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo.upper()
        self.crke = crke.upper() 
        #vse stvari v igri so zgolj velike črke

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

        #napacne = []
        #for crka in crke:
        #    if crka not in geslo:
        #        napacne += crka
        #return napacne

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

        #pravilne = []
        #for crka in crke:
        #    if crka in geslo:
        #        pravilne.append(crka)
        #return pravilne

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all([i in self.crke for i in self.geslo])
        #for crka in self.geslo:
        #    if crka not in self.crke:
        #        return False
        #return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
        #for crka in geslo:
        #    if crka not in crke:
        #        return True
        #return False

    def pravilni_del_gesla(self):
        novo_geslo = ""
        for crka in self.geslo:
            if crka in self.crke:
                novo_geslo += crka
            else:
                novo_geslo += "_"
        return novo_geslo

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if self.poraz():
            return PORAZ

        if crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke += crka

        if self.zmaga():
            return ZMAGA

        if crka in self.geslo:
            return PRAVILNA_CRKA
        #vrstni red je pomemben, saj bi drugače ob zmagi javilo le pravilno črko in ne zmage

        if self.poraz():
            return PORAZ

        return NAPACNA_CRKA

bazen_besed = []
with open("besede.txt", encoding="utf8") as input_file:
    bazen_besed = input_file.readlines()

def nova_igra(bazen_besed):
    beseda = random.choice(bazen_besed).strip()
    return Igra(beseda, "")






        







    
