from this import d
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#total de ingresos mensuales sin contar devoluciones

#diccionario de meses con ventas 
dates = {int(date[3][3:5]) : [] for date in lifestore_sales}

#items_vendidos = {mes: productos_vendidos}
items_vendidos = {a : [d[1] for d in lifestore_sales if a in [int(d[3][3:5])] if d[4] != 1] for a in dates}

# precios = {item : precio_item}
precios = {a[0] : a[2] for a in lifestore_products}

# ingresos {mes : total_ventas}
ingresos = {mes : sum([precios[b] for b in item]) for mes,item in items_vendidos.items()}

productos_mensuales = {}
#se obtiene diccionario con numero de mes con llave y lista de productos vendidos sin repetir
for a,b in items_vendidos.items():
    productos_mensuales[a] = []
    for c in b:
        if c not in productos_mensuales[a]:
            productos_mensuales[a].append(c)
        else:
            continue


#ventas_mensuales = diccionario con promedio de ventas como valor para cada mes como llave
ventas_mensuales = {a : round(len(items_vendidos[a])/len(productos_mensuales[a]),2) for a,b in items_vendidos.items() if len(productos_mensuales[a]) != 0}

# total de ventas en todos los meses
anual = sum([b for a,b in ingresos.items()])


ingresos_totales = {a : 0 if a not in ingresos.keys() else ingresos[a] for a in range(1,13)}
ventas = {a : 0 if a not in ventas_mensuales.keys() else ventas_mensuales[a] for a in range(1,13)}



len_mes = {a : len(b) for a,b in items_vendidos.items()} # len_mes = {mes : total de ventas hechas}
len_list = [b for a,b in len_mes.items()] # lista ordenada ascendentemente de las ventas 
len_list.sort(reverse=True)
meses_mas_ventas = []

#ciclo para acomodar el mes correspondiente con sus ventas
for a in len_list:
    for b,c in len_mes.items():
        if a == c:
            meses_mas_ventas.append([c,b])



##codigo para imprimir punto 3

meses_str = [0,'enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

#texto para ganancias totales y ventas promedio mensuales 

ganancias_mensuales = ['El mes de {} tuvo una ganancia de {} pesos'.format(meses_str[a], ingresos_totales[a]) for a,b in ingresos_totales.items()]
ventas_promedio = ['El mes de {} tuvo {} ventas promedio'.format(meses_str[a],ventas[a]) for a,b in ventas.items()]
mejores_meses = ['El mes de {} tuvo {} ventas.'.format(meses_str[a[1]],a[0]) for a in meses_mas_ventas]
total_anual = "LifeStore registro para el 2020 un ingreso de {} pesos".format(anual)
