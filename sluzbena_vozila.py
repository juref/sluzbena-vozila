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
    zakljuci = False
    while zakljuci ==  False:
        znamka = raw_input("Vnesi znamko avtomobila:")
        tip = raw_input("Vnesi tip avtomobila:")
        kilometer = raw_input("Vnesi kilometre avtomobila:")
        zservis = raw_input("Vnesi datum zadnjega servisa:")
        seznam.append(Avto(znamka.title(), tip.title(), kilometer, zservis))
        while True:
            odg = raw_input("Zelis dodati se kaksno vozilo? da/ne:")
            if odg.lower() == "da" or odg.lower() == "d":
                print " "
                break
            elif odg.lower() == "ne" or odg.lower() == "n":
                zakljuci = True
                return zakljuci
            else:

                print ""
                print 'Prosim izberite "da" ali "ne"!'
                print ""

def izpis_seznama(avtomobili):
    if len(avtomobili) == 0:
        print "Seznam je prazen!"
    for stej, a in enumerate(avtomobili):
        a.izpis_vozila(stej + 1)

def izbrisi_avto(seznam):
    zakljuci = False
    if len(seznam) == 0:
        print "V seznamu ni avtomobilov!"
    else:
        while zakljuci == False:
            for stej, a in enumerate(seznam, 1):
                print str(stej) + ") " + a.znamka + "-" + a.model + " / " + a.km + "km" + " / " + a.servis

            print ""
            print 'q) Izhod'
            print ""
            izbor = raw_input('Katero vozilo bi želel izbrisati (vpiši zaporedno št.)? Za izhod izberite "q": ')
            if izbor == "q":
                break
            elif int(izbor) >= int(len(seznam)):
                print "\nIzbrano število ni iz seznama! Prosim vnesite pravilno vrednost (število od 1 do %s):\n" % len(seznam)
            else:
                while True:
                    zakljuci = False
                    del seznam[int(izbor) - 1]
                    da_ne = raw_input("Želiš izbrisati še kakšno vozilo (da/ne)? ")

                    if da_ne == "da":
                        break
                    elif da_ne == "ne":
                        zakljuci = True
                        return zakljuci
                    else:
                        print ""
                        print 'Prosim izberite "da" ali "ne"!'
                        print ""

def shrani_txt(seznam, txt_datoteka):
    for a in seznam:
        txt_datoteka.write(a.znamka + "," + a.model + "," + a.km + "," + a.servis + "\n")

############### Začetek aplikacije ####################

print "\nDobrodošli v programu z aupravljanje službenih vozil"

vozila = [] # brez tega javi error če je txt datoteka prazna!

txt_datoteka = open("./_txt/vozila.txt", "r+")

vmesni_seznam = []

for vrstica in txt_datoteka:
    vmesni_seznam.append(vrstica.strip())

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
    print ""
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
        dodaj_avto(vozila)
    elif selection == "5":
        izbrisi_avto(vozila)
    elif selection == "q":
        txt_data = open("./_txt/vozila.txt", "w+")
        shrani_txt(vozila, txt_data)
        print "\nHvala in nasvidenje!"
        break
    else:
        print "\nNapaka! Niste izbrali nobone od možnih operacij."

