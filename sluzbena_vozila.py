#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Avto():
    def __init__(self, znamka_avta, model_avta, km_avta, servis_avta):
        self.znamka = znamka_avta
        self.model = model_avta
        self.km = km_avta
        self.servis = servis_avta

    def izpis_vozila(self, stej): # stej doda stevilo pred izpis za lažje izbiranje v nadaljnih korakih
        print str(stej) + ") " + self.znamka + " " + self.model + " prevoženih " + self.km + " km, zadnji servis:" + self.servis

def dodaj_avto(seznam):
    while True:
        znamka = raw_input("Vnesi znamko avtomobila:")
        tip = raw_input("Vnesi tip avtomobila:")
        kilometer = raw_input("Vnesi kilometre avtomobila:")
        zservis = raw_input("Vnesi datum zadnjega servisa:")
        seznam.append(Avto(znamka.title(), tip.title(), kilometer, zservis))
        odg = raw_input("Zelis dodati se kaksno vozilo? Da/ne:")
        if odg.lower() == "da" or odg.lower() == "d":
            print " "
        else:
            break

def izpis_seznama(avtomobili):
    for stej, a in enumerate(avtomobili):
        a.izpis_vozila(stej + 1)

def izbrisi_avto(seznam):
    if len(seznam) == 0:
        print "V seznamu ni avtomobilov!"
    else:
        print len(seznam)


############### Začetek aplikacije ####################

print "\nDobrodošli v programu z aupravljanje službenih vozil"

txt_datoteka = open("./_txt/vozila.txt", "r+")

vmesni_seznam = []

for vrstica in txt_datoteka:
    vmesni_seznam.append(vrstica.strip())

    vozila = []

    for v in vmesni_seznam:
        vozila.append(Avto(v.split(",")[0],
                           v.split(",")[1],
                           v.split(",")[2],
                           v.split(",")[3]))

while True:
    print ""
    print "1) Ogled seznama vozil"
    print "2) Urejati število prevoženih kilometrov"
    print "3) Urejati datum zadnjega servisa"
    print "4) Dodati novo vozilo"
    print "5) Izbrisati obstoječe vozilo"
    print "q) Za prekinitev programa"
    print ""
    selection = raw_input("Prosim izberite 1, 2, 3, 4, 5 ali q: ")
    print ""

    if selection == "1":
        izpis_seznama(vozila)
    elif selection == "2":
        print "kilometri"
    elif selection == "3":
        print "datum"
    elif selection == "4":
        print "dodaj"
    elif selection == "5":
        izbrisi_avto(vozila)
    elif selection == "q":
        print "\nHvala in nasvidenje!"
        break
    else:
        print "\nNapaka! Niste izbrali nobone od možnih operacij."

