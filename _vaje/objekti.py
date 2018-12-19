#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Oseba():
    emso = ""
    ime = ""
    priimek =""

    def __init__(self, e, i, p):
        self.emso = e
        self.ime = i
        self.priimek = p

    def izpisi_vse(self):
        print self.ime + " " + self.priimek + " ima EMŠO " + self.emso

    def izpisi_vse2(self, nekaj_dodstnega):
        print self.ime + " " + self.priimek + " ima EMŠO " + self.emso + nekaj_dodstnega

# oseba1 = Oseba("123", "Janez", "Novak")
oseba1 = Oseba("123456", "Janez", "Novak")
# oseba1.emso = "1234567"
# oseba1.ime = "Janez"
# oseba1.priimek = "Novak"

print oseba1.ime

# oseba2 = Oseba()
# oseba2.emso = "654321"
# oseba2.ime = "Zdravko"
# oseba2.priimek = "Dren"
#
# print oseba2.ime


# seznam = [oseba1, oseba2]

# for s in seznam:
#     # print s.ime
#     # s.izpisi_vse()
#     s.izpisi_vse2(" in ni občan Ljubljane")


## drugačen način - konstruktor ##
# class Avto():
#     znamka = ""
#     barva = ""
#     letnik = ""
#
#     def __init__(self, znamka, barva, letnik):
#         self.znamka = znamka
#         self.barva = barva
#         self.letnik = letnik
#
#
#     def nastavi_znamko(self, z):
#         self.znamka = z
#
#     def izpisi_znamko(self):
#         print self.znamka
#
# avto1 = Avto("bmw", "modra", "1980")
# print avto1.znamka
#
# avto1.nastavi_znamko("audi")
# print avto1.znamka
#
# avto1.znamka = "alfa"
# print  avto1.znamka
#
# avto1.izpisi_znamko()



##########################



class Ucitelj(Oseba):
    predmet = ""

    def __init__(self, e, i, p, pred):
        Oseba.__init__(self, e, i, p)
        self.predmet = pred

ucitelj = Ucitelj("123", "Rok", "Novak", "matematika")
print ucitelj.ime + " " + ucitelj.priimek + " " + ucitelj.predmet
ucitelj.izpisi_vse()