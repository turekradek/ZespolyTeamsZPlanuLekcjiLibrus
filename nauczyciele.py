# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:41:34 2022

@author: radek
"""
#%%
import pandas as pd
import xmltodict
def glowna():
    global przedmioty, klasy, nauczyciele, grupy , lekcje
    # nauczyciele_azyre = pd.read_csv('nauczyciele.csv',delimiter=';')
    nauczyciele_azyre = pd.read_csv('wzor_nauczyciele.csv',delimiter=';')
    # plik = open(r'plan.xml')
    plik = open(r'wzor_plan.xml')
    xml_plik = plik.read()
    moj_slownik = xmltodict.parse(xml_plik)
    przedmioty =  moj_slownik['timetable']['subjects']['subject']
    klasy = moj_slownik['timetable']['classes']['class']
    nauczyciele = moj_slownik['timetable']['teachers']['teacher']
    grupy = moj_slownik['timetable']['groups']['group']
    lekcje = moj_slownik['timetable']['lessons']['lesson']
    
    przedmioty  = pd.DataFrame(przedmioty)
    klasy = pd.DataFrame(klasy)
    nauczyciele = pd.DataFrame(nauczyciele)
    grupy = pd.DataFrame(grupy)
    lekcje = pd.DataFrame(lekcje)
    pol = pd.Series(lekcje['@id'])
    polecenia = pd.DataFrame(pol)
    polecenia['klasy'] = pd.Series(lekcje['@classids'])
    polecenia['klasy_id'] = pd.Series(lekcje['@classids'])
    polecenia['grupy'] = pd.Series(lekcje['@groupids'])
    polecenia['przedmiot'] = pd.Series(lekcje['@subjectid'])
    polecenia['nauczyciel'] = pd.Series(lekcje['@teacherids'])
    polecenia['nauczyciel_nazw'] = pd.Series(lekcje['@teacherids'])
    polecenia['loginy'] = polecenia['nauczyciel_nazw']
    polecenia['lekwtyg'] = pd.Series(lekcje['@periodsperweek'])
    pol_sl = polecenia.to_dict()
    n = nauczyciele['@name'].where(nauczyciele['@lastname']=='Chwiećko').dropna()
    kla = pd.Series(klasy['@name'].values, index=klasy['@id'])
    klaa= pd.Series(klasy['@name'].values, index=klasy['@id'])
    nau = pd.Series(nauczyciele['@name'].values, index=nauczyciele['@id'])
    naunazwiska = pd.Series(nauczyciele['@lastname'].values, index=nauczyciele['@id'])
    przed = pd.Series(przedmioty['@name'].values , index=przedmioty['@id'])
    przedskr = pd.Series(przedmioty['@short'].values , index=przedmioty['@id'])
    gr = pd.Series(grupy['@name'].values , index=grupy['@id'])
    nau_log = pd.Series(nauczyciele_azyre['login'].values , index=nauczyciele_azyre['Nazwisko'])
    
    polecenia['przedmiot'] = polecenia['przedmiot'].apply( lambda x: przedskr[x])
    polecenia['nauczyciel_nazw'] = polecenia['nauczyciel_nazw'].apply( lambda x: naunazwiska[x])
    polecenia['nauczyciel'] = polecenia['nauczyciel'].apply( lambda x: nau[x] )
    polecenia['grupy'] = polecenia['grupy'].apply( lambda x:  gr[x.split(',')[0]]) 
    polecenia['klasy'] = polecenia['klasy'].apply( lambda x: '_'.join([kla[el] for el in x.split(',')]) )
    polecenia['klasy_id'] = lekcje['@classids'].apply( lambda x:  ' '.join(x.split(',') ))
    polecenia['loginy'] = polecenia['nauczyciel_nazw'].apply( lambda x: nau_log[x]     )
    polecenia['lekwtyg'] = polecenia['lekwtyg'].apply(lambda x: str(int(float(x))))
    return polecenia
polecenia = glowna()
# '''
# New-Team -Displayname '3AP_3BP_3CP_Język angielski' -Template 'EDU_Class' -Owner 'login@domena.com'
# '''
def nauczyciele_():
    a = nauczyciele['@name']
    return a.tolist()
def klasy_():
    a = klasy['@short']
    return a.tolist()
''' ZNAJDUJE LEKCJE NAUCZYCIELA '''
def lekcje_nauczyciela(nazwisko):
    nazwisko = nazwisko.split()[0]
    nazwisko = nazwisko.title()
    odp = polecenia[polecenia['nauczyciel_nazw'] == nazwisko][['klasy','grupy','przedmiot','lekwtyg']]
    #odp = odp.to_string(col_space=None,columns=['klasy','grupy','przedmiot','lekwtyg'],header=True,index=False)
    odp = odp.to_html(col_space=None,columns=['klasy','grupy','przedmiot','lekwtyg'],header=True,index=False)
    if 'Empty DataFrame' in odp:
        return f'Najprawdopodobniej nauczyciel {nazwisko}\nnie ma żadnych lekcji w planie '
    else:
        return odp
# za = lekcje_nauczyciela('Turek')
def ile_lekcji_na_tydzien(nazwisko):
    identyfikator = nauczyciele[nauczyciele['@name'] == nazwisko]['@id'].iloc[0]
    ile = []
    for i in range( len( lekcje)):
        if lekcje.iloc[i]['@teacherids'] == identyfikator:
            ile.append(float(lekcje.iloc[i]['@periodsperweek']))
    return int(sum(ile))

# zzz = ile_lekcji_na_tydzien('Turek Radosław')

''' TWORZY POLECENIA '''
def pol(klasy , przedmiot , login  ):
    lista = ["New-Team -Displayname '",klasy.replace('LO_',' '),'_',przedmiot,"' -Template 'EDU_Class' -Owner '",login,"'"]
    return lista
''' TWORZY POLECENIA '''
def tworzenie_polecen():
    lista = []
    for i in range(len(polecenia)):
        lista.append(pol(polecenia.iloc[i]['klasy'],   polecenia.iloc[i]['przedmiot'] ,
                         polecenia.iloc[i]['loginy']))
    lista = sorted(lista, key=lambda x : x[1])
    lista = [ ''.join(el) for el in lista ]
    return '\n'.join(lista)
def polecenia_do_pliku(nazwa):
    with open(nazwa+'.txt', 'w', encoding='utf8') as f:
        f.write(tworzenie_polecen())
    
''' ZAPISUJE DO PLIKU '''
def zapis_do_pliku(nazwa,tresc):
    with open(nazwa+'.txt','w',encoding='utf8') as f:
        f.write(tresc)

''' DZIALA ZNAJDUJAC LEKCJE WYBRANEJ KLASY '''
def lekcje_poindeksie(klasa):
    global lekwtyg
    klasa = klasa.upper()
    odp = []
    for i in range( len( polecenia)):
        if klasa in polecenia.iloc[i]['klasy']:
            odp.append([ polecenia.iloc[i]['klasy'].replace(' LO','') ,
                        polecenia.iloc[i]['przedmiot'],
                        polecenia.iloc[i]['grupy'], 
                        str(int(float(polecenia.iloc[i]['lekwtyg']))),
                        polecenia.iloc[i]['nauczyciel']])
    odp = sorted( odp , key=lambda x : x[1])
    kl = [ el[0] for el in odp ]
    prz = [ el[1] for el in odp ]
    gr = [ el[2] for el in odp ]
    le = [ el[3] for el in odp ]
    nn = [ el[4] for el in odp ]
    lekwtyg = []   
    ile = []
    for i in range(len( prz )):
        if prz[i] not in lekwtyg:
            lekwtyg.append(prz[i])
            ile.append(int(le[i]))

    frame = pd.DataFrame({'klasa': kl,
                       'przedmiot': prz,
                       'grupy': gr,
                       'lekwtyg': le,
                       'nauczyciel': nn})
    odp = [ '\t'.join(el) for el in odp]
    #do_string = frame.to_string(col_space=None,columns=['klasa','przedmiot','nauczyciel'],header=True,index=False)
    do_html   = frame.to_html(col_space=None,columns=['klasa','przedmiot','grupy',
                                                      'lekwtyg','nauczyciel'],header=True,index=False)
    return (do_html,sum(ile), lekwtyg)
    #return (do_html)

# zq = lekcje_poindeksie('3gp')
# zzxx = tworzenie_polecen()
