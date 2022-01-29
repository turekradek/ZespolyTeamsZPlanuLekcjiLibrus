import pandas as pd
import xmltodict


def glowna():
    global przedmioty, klasy, nauczyciele, grupy, lekcje
    # nauczyciele_azyre = pd.read_csv('nauczyciele.csv',delimiter=';')
    nauczyciele_azyre = pd.read_csv("wzor_nauczyciele.csv", delimiter=";")
    # plik = open(r'plan.xml')
    with open(r"wzor_plan.xml") as plik:
        xml_plik = plik.read()
    moj_slownik = xmltodict.parse(xml_plik)
    return moj_slownik


def nauczyciele_azyre_():
    return pd.read_csv("wzor_nauczyciele.csv", delimiter=";")


def przedmioty_():
    przedmioty = glowna()["timetable"]["subjects"]["subject"]
    return pd.DataFrame(przedmioty)


def klasy_():
    klasy = glowna()["timetable"]["classes"]["class"]
    return pd.DataFrame(klasy)


def klasy_lista():
    klasy = klasy_()
    a = klasy["@short"]
    return a.tolist()


def nauczyciele_():
    nauczyciele = glowna()["timetable"]["teachers"]["teacher"]
    return pd.DataFrame(nauczyciele)


def nauczyciele_lista():
    a = nauczyciele_()["@name"]
    return a.tolist()


def grupy_():
    grupy = glowna()["timetable"]["groups"]["group"]
    return pd.DataFrame(grupy)


def lekcje_():
    lekcje = glowna()["timetable"]["lessons"]["lesson"]
    return pd.DataFrame(lekcje)

def nauczyciele_seria():
    nauczyciele = nauczyciele_()
    nau = pd.Series(nauczyciele["@name"].values, index=nauczyciele["@id"])
    naunazwiska = pd.Series(nauczyciele["@lastname"].values, index=nauczyciele["@id"])
    return nau, naunazwiska


def przedmioty_seria():
    przedmioty = przedmioty_()
    przed = pd.Series(przedmioty["@name"].values, index=przedmioty["@id"])
    przedskr = pd.Series(przedmioty["@short"].values, index=przedmioty["@id"])
    return przed, przedskr


def grupy_seria():
    grupy = grupy_()
    gr = pd.Series(grupy["@name"].values, index=grupy["@id"])
    return gr


def klasy_seria():
    klasy = klasy_()
    kla = pd.Series(klasy["@name"].values, index=klasy["@id"])
    klaa = pd.Series(klasy["@name"].values, index=klasy["@id"])
    return kla, klaa


def nauczyciele_loginy():
    nauczyciele_azyre = nauczyciele_azyre_()
    nau_log = pd.Series(
        nauczyciele_azyre["login"].values, index=nauczyciele_azyre["Nazwisko"]
    )
    return nau_log


def tworzenie_listy_polecen():
    lekcje = lekcje_()
    przedm_seria = przedmioty_seria()
    nau_seria = nauczyciele_seria()
    gr_seria = grupy_seria()
    kl_seria = klasy_seria()
    polecenia = pd.DataFrame(pd.Series(lekcje["@id"]))
    polecenia["klasy"] = pd.Series(lekcje["@classids"]).apply(
        lambda x: "_".join([kl_seria[0][el] for el in x.split(",")])
    )
    polecenia["klasy_id"] = pd.Series(lekcje["@classids"]).apply(lambda x: " ".join(x.split(",")))
    polecenia["grupy"] = pd.Series(lekcje["@groupids"]).apply(
        lambda x: gr_seria[x.split(",")[0]]
    )
    polecenia["przedmiot"] = pd.Series(lekcje["@subjectid"]).apply(
        lambda x: przedm_seria[1][x]
    )
    polecenia["nauczyciel"] = pd.Series(lekcje["@teacherids"]).apply(
        lambda x: nau_seria[0][x]
    )
    polecenia["nauczyciel_nazw"] = pd.Series(lekcje["@teacherids"]).apply(
        lambda x: nau_seria[1][x]
    )
    polecenia["loginy"] = polecenia["nauczyciel_nazw"].apply(
        lambda x: nauczyciele_loginy()[x]
    )
    polecenia["lekwtyg"] = pd.Series(lekcje["@periodsperweek"]).apply(lambda x: str(int(float(x))))
    return polecenia

# '''
# New-Team -Displayname '3AP_3BP_3CP_Język angielski' -Template 'EDU_Class' -Owner 'login@domena.com'
# '''

""" ZNAJDUJE LEKCJE NAUCZYCIELA """

def lekcje_nauczyciela(nazwisko):
    nazwisko = nazwisko.split()[0]
    nazwisko = nazwisko.title()
    polecenia = tworzenie_listy_polecen()
    odp = polecenia[polecenia["nauczyciel_nazw"] == nazwisko][
        ["klasy", "grupy", "przedmiot", "lekwtyg"]
    ]
    odp = odp.to_html(
        col_space=None,
        columns=["klasy", "grupy", "przedmiot", "lekwtyg"],
        header=True,
        index=False,
    )

    if "Empty DataFrame" in odp:
        return (
            f"Najprawdopodobniej nauczyciel {nazwisko}\nnie ma żadnych lekcji w planie "
        )
    else:
        return odp



def ile_lekcji_na_tydzien(nazwisko):
    nauczyciele = nauczyciele_()
    lekcje = lekcje_()
    identyfikator = nauczyciele[nauczyciele["@name"] == nazwisko]["@id"].iloc[0]
    ile = []
    for i in range(len(lekcje)):
        if lekcje.iloc[i]["@teacherids"] == identyfikator:
            ile.append(float(lekcje.iloc[i]["@periodsperweek"]))
    return int(sum(ile))


""" TWORZY POLECENIA """


def pol(klasy, przedmiot, login):
    lista = [
        "New-Team -Displayname '",
        klasy.replace("LO_", " "),
        "_",
        przedmiot,
        "' -Template 'EDU_Class' -Owner '",
        login,
        "'",
    ]
    return lista


""" TWORZY POLECENIA """


def tworzenie_polecen():
    lista = []
    polecenia = tworzenie_listy_polecen()
    for i in range(len(polecenia)):
        lista.append(
            pol(
                polecenia.iloc[i]["klasy"],
                polecenia.iloc[i]["przedmiot"],
                polecenia.iloc[i]["loginy"],
            )
        )
    lista = sorted(lista, key=lambda x: x[1])
    lista = ["".join(el) for el in lista]
    return "\n".join(lista)


def polecenia_do_pliku(nazwa):
    with open(nazwa + ".txt", "w", encoding="utf8") as f:
        f.write(tworzenie_polecen())


""" ZAPISUJE DO PLIKU """


def zapis_do_pliku(nazwa, tresc):
    with open(nazwa + ".txt", "w", encoding="utf8") as f:
        f.write(tresc)


""" DZIALA ZNAJDUJAC LEKCJE WYBRANEJ KLASY """


def lekcje_poindeksie(klasa):
    klasa = klasa.upper()
    przedmioty = przedmioty_()
    polecenia = tworzenie_listy_polecen()
    odp = [ [ polecenia.iloc[i]["klasy"].replace(" LO", ""),polecenia.iloc[i]["przedmiot"],
            polecenia.iloc[i]["grupy"], str(int(float(polecenia.iloc[i]["lekwtyg"]))),
            polecenia.iloc[i]["nauczyciel"], ] for i in range(len(polecenia)) if klasa in polecenia.iloc[i]["klasy"]]

    prz = [el[1] for el in odp]
    le = [el[3] for el in odp]
    lekwtyg = []
    ile = 0
    for i in range(len(prz)):
        if prz[i] not in lekwtyg:
            lekwtyg.append(prz[i])
            ile += int(le[i])
    frame = pd.DataFrame( {"klasa": [el[0] for el in odp],
            "przedmiot": prz,
            "grupy": [el[2] for el in odp],
            "lekwtyg": [el[3] for el in odp],
            "nauczyciel": [el[4] for el in odp],
        }
    )


    do_html = frame.to_html(
        col_space=None,
        columns=["klasa", "przedmiot", "grupy", "lekwtyg", "nauczyciel"],
        header=True,
        index=False,
    )
    return do_html, ile, lekwtyg
