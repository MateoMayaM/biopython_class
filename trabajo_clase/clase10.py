import pandas as pd
import numpy as np

'''
pd_DF = pd.DataFrame(np.random.rand(3, 2),
                     columns=["columna_1", "columna_2"],
                     index=['a','b','c'])

# A partir de objetos series.

produccion = pd.Series([5, 11, 4, 7, 2],
                       index= ['gen1', 'gen2', 'gen3','gen4', 'gen5'],
                       name='production')
costos = pd.Series([ 5, 4.3, 7, 3.5],
                  index=['gen1', 'gen2', 'gen3', 'gen5'],
                  name='costos')

costo_benecio = pd.DataFrame({'costos':costos,
                              'produccion':produccion})
'''
#Ejercicio 1

produccion = pd.Series([5, 11, 4, 7, 2],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
costos = pd.Series([ 3.5, 5, 7, 4.3],
                  index=['gen1', 'gen2', 'gen3', 'gen5'],
                  name='costos')
costo_beneficio = pd.DataFrame({'costos': costos,
                       'produccion': produccion})

# Crear una columna llamada "costo unitario" con los valores de los costos unitarios

costo_beneficio['unitario'] = costo_beneficio.costos/costo_beneficio.produccion

# Obtener los índices de los valores máximos de cada columna ll
costo_beneficio.idxmax()

# Ejercicio 2

produccion_30 = pd.Series([5, 11, 4, 7, 2],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
produccion_35 = pd.Series([3, 7, 9, 4, 6],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
costos = pd.Series([ 3.5, 5, 7, 4.3],
                  index=['gen1', 'gen2', 'gen3', 'gen5'],
                  name='costos')
costo_beneficio = pd.DataFrame({'costos': costos,
                       'produccion 30°': produccion_30,
                        'produccion 35°': produccion_35})

columnas_interes = ['produccion 30°', 'produccion 35°']
producciones = costo_beneficio.loc[:, columnas_interes]
producciones.div(costo_beneficio.costos, axis=0)

# Renombrar
costos_unitarios.rename( columns = {'produccion 30°':'costo unitario 30°',
                                   'produccion 35°':'costo unitario 35°'},
                         inplace=True)


organismos = np.random.choice(['procariotas', 'eucariotas', 'arqueas'], 5, p=[0.5, 0.3, 0.2])
costo_beneficio['organismos'] = organismos
costo_beneficio

# MATPLOTLIB.

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# creamos figura
fig = plt.figure()
# creamos un eje
ax = plt.axes()

x = np.linspace(0, 10, 1000)
# ploteamos (x, y respectivamente)
ax.plot(x, np.sin(x))

ax.set(xlim=(0, 10), ylim=(-2, 2),  #limites
       xlabel="x", ylabel="sen(x)", #etiquetas
       title="grafiquita")       #titulo

# al momento de usar un plt show , matplotlib descarta la figura,
plt.show()


#subplots
# aqui creamos dos, distribuidos(1,2)

fig, axs = plt.subplots(nrows = 1, ncols = 2)

axs[0].plot(x, np.sin(x))  #primer axes

axs[1].plot(x, np.cos(x)) #segundo axes

#poner labes, etc

# enseña plot
plt.show()


plt.plot(x, np.sin(x), "-.")
plt.plot(x, np.cos(x), "o")
plt.show()


