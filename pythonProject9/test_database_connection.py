import pytest
import psycopg2
from db_config import db_config

# @pytest.fixture(scope="module")
# def db_connection():
#     conn=None
#     try:
#         conn = psycopg2.connect(**db_config)
#         yield conn
#     finally:
#         if conn is not None:
#             conn.close()
#
# def test_postgres_connection(db_connection):
#     assert db_connection is not None
#     assert db_connection.status== psycopg2.extensions.STATUS_READY


# @pytest.fixture(params=[1,2,3,4])
# def skaicius(request):
#     return request.param
#
# def test_is_dvieju(skaicius):
#     assert skaicius %2==0 or skaicius %2==1

# @pytest.fixture(params=['hello', 'pytest', 'world'])
# def word(request):
#     return request.param
#
# def test_word_contains_py(word):
#     assert 'py' in word or 'py' not in word

# @pytest.fixture(params=[1,2,3])
# def skaicius(request):
#     return request.param
#
# def test_number_is_positive(skaicius):
#     assert skaicius >0

# 1. Skirtingų Matematinių Operacijų Testavimas: Sukurkite paprasta skaičiuotuvą,
# kuris atlieka pagrindines matematines operacijas: sudėtį, atimtį, daugybą ir dalybą.
# Parašykite fikstūrą, kuri patikrintų ar Jūsų programa veikia teisingai ir atlieka visas operacijas.




# def sudetis(a,b):
#     return a+b
#
# def atimtis(a,b):
#     return a-b
#
# def daugyba(a,b):
#     return a*b
#
# def dalyba(a,b):
#     return a/b
# @pytest.fixture(params=['daugyba', 'dalyba', 'sudetis', 'atimtis'])
# def operacija(request):
#     return request.param
#
# def test_ar_veikia_operacijos(operacija):
from matematika import prisijungti, veiksmas, atsijungti

# @pytest.fixture(params=[('sudetis', 2,3,5),
#                         ('atimtis', 5,2,3),
#                         ('daugyba', 3,4,12),
#                         ('dalyba', 10,2,5)])
#
# def matematika(request):
#     return request.param
#
# def test_skaiciuotuvas(matematika):
#     operacija, x,y,numatytas_rezultatas=matematika
#     assert skaiciuotuvas(operacija,x,y)==numatytas_rezultatas

# @pytest.fixture(params=[
#     ('http://www.google.com', 200),
#     ('http://neegzistuojantisurl.com', None),
#     ('https://www.github.com', 200),
#     ('http://www.tikrai_ne_tinklapis.com', None)
#  ])
# def url_ir_tiketinas_rezultatas(request):
#     return request.param
#
# def test_gauti_http_status(url_ir_tiketinas_rezultatas):
#     url, tiketinas_rezultatas=url_ir_tiketinas_rezultatas
#     assert gauti_http_status(url)==tiketinas_rezultatas


# @pytest.fixture(params=[16,18,20,17])
#
# def vartotojo_amziaus(request):
#     return request.param
#
# def test_vartotojo_amziaus_patikrinimas(vartotojo_amziaus):
#     numatytas_rezultatas = vartotojo_amziaus>=18
#     assert vartotojo_amziaus_patikrinimas(vartotojo_amziaus)==numatytas_rezultatas

# @pytest.fixture(params=[
#         ('labas rytas Lietuva', ['labas', 'rytas', 'Lietuva']),
#         ('Python-pytest', ['Python-pytest'])])
#
# def atidalinti_zodziai(request):
#      return request.param
#
# def test_atidalintas_tekstas(atidalinti_zodziai):
#     eilute, nustatytas_rezultatas = atidalinti_zodziai
#     assert atidalintas_tekstas(eilute) == nustatytas_rezultatas
#
#     print(nustatytas_rezultatas)

# pytest.fixture(params=[20,53,45,12,65])
#
# def duotieji_skaiciai(request):
#     return request.param
#
# def test_skaiciu_patikrinimas(duotieji_skaiciai):
#     numatytas_rezultatas=duotieji_skaiciai >20
#     assert skaiciu_patikrinimas(duotieji_skaiciai)==numatytas_rezultatas

@pytest.fixture(params=[{'vartotojas': 'admin', 'veiksmas': 'atnaujinti duomenys', 'atsakymas': 'atliktas veiksmas: atnaujinti duomenys'},
                        {'vartotojas': 'svecias', 'veiksmas': 'skaityti', 'atsakymas': False}])

def naudojimo_scenarijus(request):
    return request.param

def test_naudojimo_scenarijus(naudojimo_scenarijus):
    vartotojas = naudojimo_scenarijus['vartotojas']
    atlikti_veiksma = naudojimo_scenarijus['veiksmas']
    prisijungimo_statusas = prisijungti(vartotojas)
    if vartotojas == 'admin':
        assert prisijungimo_statusas == True
        veiksmo_statusas = veiksmas(atlikti_veiksma)
        assert veiksmo_statusas == naudojimo_scenarijus['atsakymas']
    else:
        assert prisijungimo_statusas == False

    if vartotojas == 'admin':
        atsijungimas = atsijungti(vartotojas)
        assert atsijungimas == f'{vartotojas} atsijunge'

