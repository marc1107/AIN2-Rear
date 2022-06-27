# Autor: Marc Bohner
import math

print("Adresse eingeben:")
adresse = int(input())


def directMapped():
    print("Blockgröße eingeben:")
    blocksize = int(input())
    print("Blockanzahl eingeben:")
    anzahl = int(input())
    blocknummer = math.floor(adresse / blocksize)
    blockindex = blocknummer % anzahl
    tag = math.floor(blocknummer / anzahl)
    offset = adresse % blocksize

    print("Blocknummer: %d\t\t\tBerechnung: floor(Adresse / Blockgröße) = floor(%d / %d)" % (
        blocknummer, adresse, blocksize))
    print(
        "Blockindex: %d\t\t\t\tBerechnung: Blocknummer mod Blockanzahl = %d mod %d" % (blockindex, blocknummer, anzahl))
    print(
        "Tag: %d\t\t\t\t\t\tBerechnung: floor(Blocknummer / Blockanzahl) = floor(%d / %d)" % (tag, blocknummer, anzahl))
    print("Offset (in Bytes): %d\t\tBerechnung: Adresse mod Blockgröße = %d mod %d" % (offset, adresse, blocksize))


def xWay():
    print("Wie viel Way (N)?")
    n = int(input())
    print("Blockgröße:")
    blocksize = int(input())
    print("Gesamtspeicherplatz (in Bytes):")
    cachesize = int(input())
    anzahlbloecke = cachesize / blocksize
    anzahlsets = anzahlbloecke / n
    blocknummer = math.floor(adresse / blocksize)
    setindex = blocknummer % anzahlsets
    tag = math.floor(blocknummer / anzahlsets)
    offset = adresse % blocksize

    print("Blocknummer: %d\t\t\t\tBerechnung: floor(Adresse / Blockgröße) = floor(%d / %d)" % (
        blocknummer, adresse, blocksize))
    print("Anzahl Blöcke im Cache: %d\t\tBerechnung: Gesamtspeicherplatz / Blockgröße = %d / %d" % (
        anzahlbloecke, cachesize, blocksize))
    print("Anzahl Sets im Cache: %d\t\tBerechnung: Anzahl Blöcke / N = %d / %d" % (anzahlsets, anzahlbloecke, n))
    print("Set-Index: %d\t\t\t\t\tBerechnung: Blocknummer mod Anzahl Sets = %d mod %d" % (
        setindex, blocknummer, anzahlsets))
    print("Tag: %d\t\t\t\t\t\tBerechnung: floor(Blocknummer / Anzahl Sets) = floor(%d / %d)" % (
        tag, blocknummer, anzahlsets))
    print("Offset (in Bytes): %d\t\t\tBerechnung: Adresse mod Blockgröße = %d mod %d" % (offset, adresse, blocksize))


print("1: Direct Mapped Cache\n2: N-Way-Set-Associative Cache")
func = int(input())
if func == 1:
    directMapped()
elif func == 2:
    xWay()
