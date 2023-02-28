#Luhnův test používají některé bankovní společnosti k rozpoznání platného čísla kreditní karty od náhodně poskládaných číslic.
karta_1 = "49927398716"
karta_2 = "215455557748"
karta_3 = "79927398714"


#obrátíš pořadí číslic v zadaném čísle
def obracene_poradi(cislo_karty):
    return cislo_karty[::-1]


#suma číslic na lichých pozicích

def sum_licha_cisla(cislo_karty: str) -> int:
    cislo_karty = (obracene_poradi(cislo_karty))
    count = 0
    for x in range(0,len(cislo_karty),2):
        count = count + int(cislo_karty[x])
    return count

def sum_suda_cisla(cislo_karty: str) -> int:
    count1 = 0
    cislo_karty = (obracene_poradi(cislo_karty))

#vybereš číslice na sudých pozicích, vynásobíš je dvěma, sečteš jednotlivé cifry ve všech číslech a uděláš sumu
    list_vynasobeno = []
    for x in range(1,len(cislo_karty),2):
        list_vynasobeno.append(int(cislo_karty[x])*2)
    novy_vysledek = []
    count1 = 0
    for x in list_vynasobeno:
        if len(str(x)) == 2:
            novy_vysledek.append(int(str(x)[0]) + int(str(x)[1]))
        else: 
            novy_vysledek.append(x)
    for x in novy_vysledek:
        count1 = count1 + int(x)
    return count1


def soucet_sum(cislo_karty):
    return sum_licha_cisla(str(cislo_karty)) + sum_suda_cisla(str(cislo_karty))

#výslednou hodnotu vydělíš deseti a pokud bude zbytek po dělení nula, je číslo platné

def je_karta_platna(cislo_karty) -> bool:
    return soucet_sum(cislo_karty) % 10 == 0


print(
    je_karta_platna("49927398716"),
    je_karta_platna("215455557748"),
    je_karta_platna("79927398714"),
    sep="\n"
)