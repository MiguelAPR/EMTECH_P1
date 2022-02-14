import re
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#-#-#-#-#-#-#-#-#-#- LISTAS DE MAYORES VENTAS Y BUSQUEDAS -#-#-#-#-#-#-#-#-#-#

#Se obtiene una lista de coordenadas (sell/search,#item,nombre) 
coord_search = [[[k[0] for l in lifestore_searches if k[0]==l[1]].count(k[0]),k[0],k[1]] for k in lifestore_products]
coord_sell = [[[i[0] for j in lifestore_sales if (i[0] == j[1]) and (j[4] != 1)].count(i[0]),i[0],i[1]] for i in lifestore_products]
 
 #Se ordena descendentemente la lista de coordenadas para escoger los n-esimos primeros elementos
coord_sell.sort(reverse= True)
coord_search.sort(reverse=True)

top_sellers = ['El producto {} se vendio {} veces'.format(coord_sell[i][2][:30],coord_sell[i][0]) for i in range(5)]
top_searches = ['El producto {} se busco {} veces'.format(coord_search[i][2][:30],coord_search[i][0]) for i in range(10)]


#-#-#-#-#-#-#-#-#-#- LISTAS POR CATEGORIA CON MENORES  VENTAS Y BUSQUEDAS (POR CATEGORIA) -#-#-#-#-#-#-#-#-#-#

#dict categorty = {categorias : [categoria_de_items]}
dict_category = {i[3]: [j[0] for j in lifestore_products if j[3] == i[3]] for i in lifestore_products}

#diccionarios con categorias como llaves y  coord (busqueda/venta , item)
worst_search = {i[3] : [j for j in coord_search if j[1] in dict_category[i[3]]] for i in lifestore_products}
worst_sell = {i[3] : [j for j in coord_sell if j[1] in dict_category[i[3]]] for i in lifestore_products}

#ordenar valores ascendentemente 
for val in worst_sell:
    worst_sell[val].sort(reverse=False)
    worst_search[val].sort(reverse=False)

#Se crean diccionarios para ser impresos en listas
less_sold = {'Para la categoria de {}'.format(cate) : ['El producto {} se vendio {} veces'.format(i[2][:30],i[0]) for i in worst_sell[cate]] for cate in dict_category}

least_wanted = {'Para la categoria de {}'.format(cate) : ['El producto {} se busco {} veces'.format(i[2][:30],i[0]) for i in worst_search[cate]] for cate in dict_category}


for a,b in least_wanted.items():
    print("\n",a,'\n')
    for c in b:
        print(c)
        




