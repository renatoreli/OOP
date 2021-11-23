class Zivotinja:
    def __init__(self,vrsta_ishrane,naziv,vrsta,broj_nogu):
        self.vrsta_ishrane=vrsta_ishrane
        self.naziv= naziv
        self.vrsta = vrsta
        self.broj_nogu = broj_nogu

    def test(self):
        print(self.naziv,self.broj_nogu)

    def ispisi(self):
        print(f"ishrana: {self.vrsta_ishrane}", self.naziv, self.vrsta,self.broj_nogu)
        print(f"naziv:{self.naziv}")
        print(f"vrsta: {self.vrsta}")
        print(f"broj nogu: {self.broj_nogu}")

class Letecazivotinja(Zivotinja): #Zivotinja je nadklasa Zivotinja vrsta
    def __init__(self, vrsta_ishrane, naziv, vrsta, broj_nogu,raspon_krila, broj_jaja):
        super().__init__(vrsta_ishrane, naziv, vrsta, broj_nogu)
        self.raspon_krila = raspon_krila
        self.broj_jaja= broj_jaja

    def ispisi(self):
        print(f"ishrana: {self.vrsta_ishrane}")
        print(f"naziv:{self.naziv}")
        print(f"vrsta{self.vrsta}")
        print(f"broj nogu{self.broj_nogu}")
        print(f"broj jaja {self.broj_jaja}")
        print(f"raspon krila {self.raspon_krila}")
    
class MorskaZivotinja(Zivotinja):
    def __init__(self,vrsta_ishrane,naziv,vrsta,broj_nogu, broj_peraja):
        super().__init__(vrsta_ishrane,naziv, vrsta, broj_nogu)
        self.broj_peraja = broj_peraja

class Hobotnica(MorskaZivotinja):
    def __init__(self, vrsta_ishrane, naziv, vrsta, broj_nogu, broj_peraja):
        super().__init__(vrsta_ishrane, naziv, vrsta, broj_nogu, broj_peraja)
hob=Hobotnica("svejed","kraken","mekusac",0,0)
hob.ispisi()
#kit = Zivotinja ("mesojed", "kit","riba",0)
#kokos = Zivotinja ("biljojed","kokos","ptica",2)

#ptica = Letecazivotinja("mesojed","kit","riba",0,42,4)
#ptica.ispisi()
#print(ptica.raspon_krila,ptica.broj_jaja)

#riba=MorskaZivotinja("mesojed", "kit","riba",3,5)
#riba.test()

#-----------------------------------------------#
# Zivotinja --> Morska zivotinja --> Hobotnica  #
#-----------------------------------------------#