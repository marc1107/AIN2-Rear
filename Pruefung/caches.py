import math

print("Adresse eingeben:")
adresse = int(input())


def directMapped():
    print("Blockgröße eingeben:")
    blocksize = int(input())
    print("Blockanzahl eingeben:")
    anzahl = int(input())
    blocknummer = math.floor(adresse/blocksize)
    blockindex = blocknummer % anzahl
    tag = math.floor(blocknummer/anzahl)
    offset = adresse % blocksize

    print("Blocknummer:", blocknummer)
    print("Blockindex:", blockindex)
    print("Tag:", tag)
    print("Offset (in Bytes):", offset)


def xWay():
    print("Wie viel Way?")
    way = int(input())
    print("Blockgröße:")
    blocksize = int(input())
    print("Gesamtspeicherplatz (in Bytes):")
    cachesize = int(input())
    anzahlbloecke = cachesize / blocksize
    anzahlsets = anzahlbloecke / way
    blocknummer = math.floor(adresse/blocksize)
    setindex = blocknummer % anzahlsets
    tag = math.floor(blocknummer/anzahlsets)
    offset = adresse % blocksize

    print("Blocknummer:", blocknummer)
    print("Set-Index:", setindex)
    print("Anzahl Sets im Cache:", anzahlsets)
    print("Anzahl Blöcke im Cache:", anzahlbloecke)
    print("Tag:", tag)
    print("Offset (in Bytes):", offset)



print("1: Direct Mapped Cache\n2: X-Way-Set-Associative Cache")
func = int(input())
if func == 1:
    directMapped()
elif func == 2:
    xWay()



