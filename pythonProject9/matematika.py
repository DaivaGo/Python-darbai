# def sudetis(a,b):
#     return a+b
#
# def daugyba(a,b):
#     return a*b

# def didziausias_skaicius(a,b):
#     return a if a > b else b

# def pasisveikinimas(vardas):
#     return f"Labas, {vardas}"
#
# def pirmas_elementas(sarasas):
#     return sarasas[0]

# def teksto_apvertimas(tekstas):
#     apverstas = (tekstas[::-1])
#     return apverstas

# def skaiciu_suma(sarasas):
#     sarasas=[1,2,3,4]
#     return sum(sarasas)

# def filtruoti_teigiamus(sarasas):
#     return [x for x in sarasas if x>0]

# def gauti_pirma_elementa(sarasas):
#     return sarasas[0] if sarasas else None

# def ar_skaicius_dalus(skaicius):
#    return True if skaicius %3==0 else False

# def rasti_pasikartojancius_zodzius(tekstas):
#    rezultatas = [zodis for zodis in tekstas if len(zodis)!=len(set(zodis))]
#    return rezultatas
import requests

# def ar_visi_vartotojai_pilnameciai(vartotojai):
#    vartotojai = [20,23,25]
#       for vartotojas in vartotojai:


# def skaiciuotuvas(operacija, x,y):
#    if operacija=='sudetis':
#       return x+y
#    elif operacija=='atimtis':
#       return x-y
#    elif operacija=='daugyba':
#       return x*y
#    elif operacija=='dalyba':
#       return x/y


# def gauti_http_status(url):
#     try:
#         response = requests.get(url)
#         return response.status_code
#     except requests.RequestException:
#         return None

# def vartotojo_amziaus_patikrinimas(amzius):
#     return amzius >=18

# def atidalintas_tekstas(tekstas):
#    return tekstas.split()

# 3. Sąrašo Filtravimas: Parašykite funkciją, kuri priima sąrašą skaičių ir grąžina tik tuos,
# kurie yra didesni už nurodytą reikšmę. Parašykite testą su parametrizuota fikstūra.

# def skaiciu_patikrinimas(skaiciai):
#    for skaicius in skaiciai:
#       return skaicius >20

# Tarkime, norite patikrinti, kaip jūsų sistema elgiasi per visą naudojimo scenarijų,
# pavyzdžiui, vartotojo prisijungimą, atlieka veiksmą ir atsijungia.
# Jūs turite patikrinti, kaip jūsų sistema elgiasi per visą naudojimo scenarijų, pavyzdžiui,
# vartotojo prisijungimą, veiksmo atlikimą ir atsijungimą.

def prisijungti(vartotojas):
   return vartotojas == 'admin'


def veiksmas(atlikti_veiksma):
   return f'atliktas veiksmas: {atlikti_veiksma}'


def atsijungti(vartotojas):
   return f'{vartotojas} atsijunge'