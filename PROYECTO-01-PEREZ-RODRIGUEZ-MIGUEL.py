import os
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from punto1 import top_sellers, top_searches, less_sold, least_wanted
from punto2 import ranked
from punto3 import  ganancias_mensuales, ventas_promedio, mejores_meses, total_anual

login_info = {'Black_Bird':'Proyecto01', 'Pink_Duck': 'Calif101', 'Golden_Goose': 'Room202'}



os.system('cls')
print('-°-°-°-°-°-- Bienvenido al registro de datos de LifeStore --°-°-°-°-°- \n')
error = 0
while error <4:

    user = input('Ingresa tu nombre de usuario: ')

    if user in login_info.keys():
        os.system('cls')
        password = input('Ingrese password para {}: '.format(user))
        if password == login_info[user]:
            os.system('cls')
            error = 4
        else:
            os.system('cls')
            print("Password incorrecto:")    
    else:
        os.system('cls')
        print("Usuario incorrecto:")

os.system('cls') 
print('Resultados para punto 1 \n\n PRODUCTOS MAS VENDIDOS: \n')
for text in top_sellers:
    print(text)

print('\n\n Resultados para punto 1 \n\n PRODUCTOS MAS BUSCADOS:')

for text in top_searches:
    print(text)

print('\n\n Resultados para punto 1 \n\n PRODUCTOS MENOS BUSCADOS:')

for a,b in least_wanted.items():
    print("\n",a,'\n')
    for c in b:
        print(c)

print('\n\n Resultados para punto 1 \n\n PRODUCTOS MENOS VENDIDOS:')

for a,b in less_sold.items():
    print("\n",a,'\n')
    for c in b:
        print(c)

print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Punto 2-#-#-#-#-#-#-#-#-#-#-#-#--#-#-#-#-#-#-#\n\n')

#printing
print('Mejores puntuaciones:  \n')
for t in range(5):
    print(ranked[t])

print('\n Peores puntuaciones:')
for t in range(5):
    print(ranked[-t-1])


print('\n\n #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-Punto 3-#-#-#-#-#-#-#-#-#-#-#-#--#-#-#-#-#-#-#\n\n')
print('Total de ingresos mensual \n')
for t in ganancias_mensuales:
    print(t)

print('\n\nVentas mensuales promedio \n')
for t in ventas_promedio:
    print(t)
print('\n\n Meses con mejores ventas: \n\n')
for t in range(3):
    print(mejores_meses[t])

print('\n\n Ingresos anuales: \n\n')
print(total_anual)