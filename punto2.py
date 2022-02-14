from re import L
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
""" 
                    Punto 2
"""
#-#-#-#-#-#-#-#-#-#-#-#-#-#- Generar lista con reseñas -#-#-#-#-#-#-#-#-#-#-#-#-#-#

#se genera umbral para discriminar productos sin puntuacion o con menos del promedio de ventas
mean = len(lifestore_sales) / len(lifestore_products)

# puntos = {item_producto: total_vendidas}
puntos = {a[0]: len([b[2] for b in lifestore_sales if b[1] == a[0]]) for a in lifestore_products}

# score = {item_producto: [mean_score,total_vendidas]}
score = {}
for a in lifestore_products:
    score[a[0]]= [b[2] for b in lifestore_sales if b[1] == a[0]]

    if len(score[a[0]]) != 0:
        score[a[0]] = [sum(score[a[0]]) / len(score[a[0]]),puntos[a[0]]]
    else:
        score[a[0]] = 0

#lista1 = [rank, sold, item]   
lista1 = [[b[0],b[1],a] for a,b in score.items() if b != 0 and b[1] >= mean] #or len() != 1
lista1.sort(reverse = True)

ranked = []
for item in lista1:
    for a in lifestore_products:
        if a[0] == item[2]:
            b = a[1]
            
    ranked.append('El producto {} con {} ventas, tiene una calificacion de {}'.format(b[:27], item[1],round(item[0],2)))
