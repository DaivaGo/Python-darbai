# from matematika import sudetis, daugyba
# def test_sudetis():
#     num1, num2=5,10
#     rezultatas=14
#     faktinis_rezultatas=sudetis(num1,num2)
#     assert faktinis_rezultatas == rezultatas, (f"Sudeties testas nepavyko: {num1}+{num2}"
#                                             (f"turetu buti rezultatas {rezultatas}, bet gavome {faktinis_rezultatas}")
#
# def test_daugyba():
#     assert daugyba(5,5)==25

# from matematika import didziausias_skaicius
#
# def test_didziausias_skaicius():
#     assert didziausias_skaicius(10,5)==10
#     assert didziausias_skaicius(2,3)==3
#     assert didziausias_skaicius(7,7)==7

# from matematika import pasisveikinimas
#
# def test_pasisveikinimas():
#     assert pasisveikinimas('Daiva')== 'Labas, Daiva'

# from matematika import pirmas_elementas
#
# def test_pirmas_elementas():
#     assert pirmas_elementas([1,2,3])==1

# from matematika import teksto_apvertimas
# def test_teksto_apvertimas():
#     assert teksto_apvertimas('alus') == 'sula'

# from matematika import skaiciu_suma
#
# def test_skaiciu_suma():
#     assert skaiciu_suma([1,2,3,4])==10

# from matematika import filtruoti_teigiamus
# def test_filtruoti_teigiamus():
#     assert filtruoti_teigiamus([-1,-2,1,2,3])==[1,2,3]
#     assert filtruoti_teigiamus([-1,-2,-3])==[]

# from matematika import gauti_pirma_elementa
import pytest

# @pytest.mark.parametrize("sarasas, tiketinas_rezultatas",[
#     ([1,2,3],1),
#     (['a', 'b', 'c'], 'a'),
#     ([], None),
#     ([[1,2], [3,4],[5,6]],[1,2])
# ])
#
# def test_gauti_pirma_elementa(sarasas, tiketinas_rezultatas):
#     assert gauti_pirma_elementa(sarasas)==tiketinas_rezultatas

# from matematika import ar_skaicius_dalus
#
# @pytest.mark.parametrize("skaicius, tiketinas_rezultatas",[
#     (3,True),
#     (7,False),
#     (0,False),
#     (9, True)
# ])
# def test_ar_skaicius_dalus(skaicius, tiketinas_rezultatas):
#     assert ar_skaicius_dalus(skaicius)==tiketinas_rezultatas
from matematika import rasti_pasikartojancius_zodzius

@pytest.mark.parametrize("tekstas, tiketinas_rezultatas", [
    (['labas', 'stalas', 'viso', 'gero'], ['labas', 'stalas']),
    (['analitika', 'informatika', 'taip', 'ne'], ['analitika', 'informatika']),
    (['programa', 'kinas', 'laukas', 'ne'], ['programa', 'laukas'])
])
def test_rasti_pasikartojancius_zodzius(tekstas, tiketinas_rezultatas):
    assert rasti_pasikartojancius_zodzius(tekstas) == tiketinas_rezultatas