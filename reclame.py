from algemene_functies import mijn_functie_2

def print_aanbieding_1(smaken, prijzen, korting):
    korting = prijzen * (1- korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaken}, van {prijzen} euro voor {korting}")

def inkomsten_totaal(inkomsten):
    totaal_inkomsten = sum(inkomsten)
    btw = totaal_inkomsten * 0.09
    print(f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw} euro btw betaald dinetn te worden.")

def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    return (laag, hoog)

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde = totaal / aantal
    print(f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro.")

def meervoudig(invoer_lijst):
    invoer_lijst = laag_en_hoog(invoer_lijst)
    return invoer_lijst
    
def combinatie(invoer_lijst_2):
    invoer_lijst_2 = meervoudig(invoer_lijst_2)
    return invoer_lijst_2

korte_lijst = combinatie(1, 2, 3)

mijn_functie_2(korte_lijst)


