# Autor: Marc Bohner
import math


def directMapped():
    adresse = int(input("Adresse eingeben: "))
    blocksize = int(input("Blockgröße eingeben: "))
    anzahl = int(input("Blockanzahl eingeben: "))
    blocknummer = math.floor(adresse / blocksize)
    blockindex = blocknummer % anzahl
    tag = math.floor(blocknummer / anzahl)
    offset = adresse % blocksize

    print("Blocknummer: %d\t\t\tBerechnung: floor(Adresse / Blockgröße) = floor(%d / %d)" % (
        blocknummer, adresse, blocksize))
    print("Offset (in Bytes): %d\t\tBerechnung: Adresse mod Blockgröße = %d mod %d" % (offset, adresse, blocksize))
    print(
        "Blockindex: %d\t\t\t\tBerechnung: Blocknummer mod Blockanzahl = %d mod %d" % (blockindex, blocknummer, anzahl))
    print(
        "Tag: %d\t\t\t\t\t\tBerechnung: floor(Blocknummer / Blockanzahl) = floor(%d / %d)" % (tag, blocknummer, anzahl))


def xWay():
    adresse = int(input("Adresse eingeben: "))
    x = int(input("Wie viele verschiedene Caches sollen auf einmal berechnet werden?\n"))

    n = []
    blocksize = []
    cachesize = []
    anzahlbloecke = []
    anzahlsets = []
    setindex = []
    tag = []

    blocksize = int(input("Blockgröße: "))

    blocknummer = math.floor(adresse / blocksize)
    offset = adresse % blocksize

    for i in range(0, x):
        print("\nLevel {} Cache:".format(i + 1))
        n.append(int(input("Wie viel Way (N)?\n")))
        cachesize.append(int(input("Gesamtspeicherplatz (in Bytes): ")))
        anzahlbloecke.append(cachesize[i] / blocksize)
        anzahlsets.append(anzahlbloecke[i] / n[i])
        setindex.append(blocknummer % anzahlsets[i])
        tag.append(math.floor(blocknummer / anzahlsets[i]))

    # n = int(input("Wie viel Way (N)?"))
    # cachesize = int(input("Gesamtspeicherplatz (in Bytes):"))
    # anzahlbloecke = cachesize / blocksize
    # anzahlsets = anzahlbloecke / n
    # setindex = blocknummer % anzahlsets
    # tag = math.floor(blocknummer / anzahlsets)

    print("\nGilt für alle Cache-Level:")
    print("Blocknummer: %d\t\t\t\tBerechnung: floor(Adresse / Blockgröße) = floor(%d / %d)" % (
        blocknummer, adresse, blocksize))
    print("Offset (in Bytes): %d\t\t\tBerechnung: Adresse mod Blockgröße = %d mod %d" % (offset, adresse, blocksize))

    for i in range(0, x):
        print("\nSpeziell für Cache Level {}:".format(i + 1))
        print("Anzahl Blöcke im Cache: %d\t\tBerechnung: Gesamtspeicherplatz / Blockgröße = %d / %d" % (
            anzahlbloecke[i], cachesize[i], blocksize))
        print("Anzahl Sets im Cache: %d\t\tBerechnung: Anzahl Blöcke / N = %d / %d" % (anzahlsets[i], anzahlbloecke[i], n[i]))
        print("Set-Index: %d\t\t\t\t\tBerechnung: Blocknummer mod Anzahl Sets = %d mod %d" % (
            setindex[i], blocknummer, anzahlsets[i]))
        print("Tag: %d\t\t\t\t\t\tBerechnung: floor(Blocknummer / Anzahl Sets) = floor(%d / %d)" % (
            tag[i], blocknummer, anzahlsets[i]))


func = int(input("1: Direct Mapped Cache\n2: N-Way-Set-Associative Cache\n"))
if func == 1:
    directMapped()
elif func == 2:
    xWay()
