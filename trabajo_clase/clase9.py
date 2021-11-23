""""
Ejemplos biológicos numpy

import numpy as np
count_matrix = np.array([ [3, 3, 0],
                          [0, 0, 1],
                          [1, 1, 0],
                          [0, 0, 1],
                          [1, 0, 4],
                          [1, 2, 0]])

count_matrix = np.where(count_matrix > 0, 1, 0)
print(count_matrix)

# producto punto de los dos vecotores
print("producto punto gen1vsgen1:", np.dot(count_matrix.T[0], count_matrix.T[0]))

#### Gen 1 vs gen 3
print(np.vstack((count_matrix.T[0],count_matrix.T[2])) ) # para visualizar

print("producto punto gen1 vs gen3:", np.dot(count_matrix.T[0], count_matrix.T[2]))

import matplotlib.pyplot as plt

plt.imshow(expresion)
plt.colorbar()
plt.show()



from Bio.Seq import Seq
import numpy as np
def secuencia_aleatoria(tamano = 100, p = [0.5, 0.5, 0.5, 0.5],seed = None):
    np.random.seed(seed) # posibilidad de reproducibilidad
    DNA = list("ATGC")
    #secuencia random con distribucion p
    secuencia = Seq(''.join(np.random.choice(DNA, tamano, p)))
    return(secuencia)
# probemos
secuencia = secuencia_aleatoria(25, p=[0.1,0.2,0.4,0.3])
secuencia

"""
'''
# pandas: series

import pandas as pd

serie = pd.Series([1, 2, 3, 4, 5],
                  index = {"a", "b", "c", "d", "e"},
                  name = "Ejemplo Serie")

Ejercicio 1
import pandas as pd

serie = pd.Series(['a', 'b', 'c', 'd', 'e'],
                  index=['a', 'b', 'c', 'd', 'e'],
                  name="Ejemplo Serie")


print(serie)

'''
# Ejercicio 1

produccion = pd.Series([5, 11, 4, 7, 2],
                        index= ['gen1', 'gen2', 'gen3', 'gen4', 'gen5'])

costos = pd.Series([ 5, 4.3, 7, 3.5],
                  index=['gen1', 'gen2', 'gen3', 'gen5'])

costo_unitario = costos/produccion.T

bool_min = costo_unitario == costo_unitario.min()
bool_max = costo_unitario == costo_unitario.max()

costo_unitario[bool_min | bool_max]

