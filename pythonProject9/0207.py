
# print("Hello World")
# # print("Daiva")
# # vardas="Daiva"
# # print("Daiva")
#
# x=5
# # print(x)
#
# vardas="Daiva" #string tipas
# amzius=35 #int tipas (sveikasis skaicius)
# kaina=10.99  #float
# ar pilnametis=True #boolean tipas
# # print(type(vardas))
# x = 5
# y = 10
#
# ar_lygu=x==y   #lyginamasis
# ar_nelygu=x!=y  #nelygu
# print(ar_nelygu)
# daugiau= x > y
# maziau = x< y
# print(maziau)

# x = True
# y = False
# # a=5
# # a=11
# # # print(a)
# #
# # rezultatas = x and y #and lygina abi reiksmes, ae x yra kaip ir y
# # rezultatas = x or y #jeigu bent viena salyga atitinka, bus true
# # rezultatas = not x
# # # print(rezultatas)
# # # print(rezultatas)
# # #
# # #
# # # print(rezultatas)
#
# # skaicius = 5
# # rezultats = x or y
# # ar_didesnis_uz_10 = not skaicius > 10
# # print(ar_didesnis_uz_10)

# x = 5
# # x +=1 #+= padidina 1
# x-=1 #-= sumazina 1
# print(x)

# if(salyga)

# # a = 5
# # a=11
# #
# # if a > 10:
# #     print(f"a yra daugiau uz {a}")
# # else:
# #     print("a nera daugiau uz 10")
#
# amzius = 20
# if amzius >=18:
#     statusas= "Suauges"
# else:
#     statusas = "Nepilnametis"
# statusas = "Suages" if amzius >=18 else "Nepilnametis"
# print(statusas)



# pirkiniu_krepselis = ['pienas', 'obuolys', 'duona', 'batonas']
# # pirkiniu_krepselis.append('kivis') #append = prideti i sarasa
# pirkiniu_krepselis.remove('obuolys')
# pirkiniu_krepselis.pop(1) #pop istrina pagal indeksa
# pirkiniu_krepselis.insert(2, 'moliugas')
# print(pirkiniu_krepselis[1:3]) #len suskaiciuoja

# tekstas = "Labas_pasauli"
# pasisveikinimas = tekstas[:5]
# print(pasisveikinimas)

studentai = {'Ona': {
    'Pazymiai': {
        'Matematika': 9,
        'Fizika': 10
    },
    'Atsiskaitymai': {
        'Matematika': False,
        'Fizika': True,
        'Lietuviu kalba': True
    }
}, 'Jonas': {
    'Pazymiai': {
        'Matematika': 7,
        'Fizika': 10
    },
    'Atsiskaitymai': {
        'Matematika': False,
        'Fizika': True,
        'Lietuviu kalba': False

    }
}}
print(studentai['Jonas']['Atsiskaitymai'])