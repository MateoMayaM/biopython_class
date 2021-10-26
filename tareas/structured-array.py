'''
NAME
       structured-array.py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <matteo.mayam@outlook.com>

DESCRIPTION
        Este programa crea arrays estructurados con los datos de otros arrays prevismente especificados.

CATEGORY
       Numpy array.

EXAMPLE:

        Input:
            No necesita input.
        Output:
            [('Gen 1',  5, 3, 3.5, 0.7       , 1.16666667)
             ('Gen 2', 11, 7, 5. , 0.45454545, 0.71428571)
             ('Gen 3',  4, 9, 7. , 1.75      , 0.77777778)
             ('Gen 4',  2, 6, 4.3, 2.15      , 0.71666667)]



LIGA DE GITHUB: [https://github.com/MateoMayaM/biopython_class/blob/master/tareas/structured-array.py
'''

# Importación de librerías.
import numpy as np

# Definición de los arrays que contienen la producción y el costo.
produccion = np.array([ [5,3], [11, 7], [4, 9], [2, 6]])
costos = np.array([3.5, 5, 7, 4.3])

# Creación del array estructurado de producción.
produccion_struct = np.array([('Gen 1', 5, 3), ('Gen 2', 11, 7), ('Gen 3', 4, 9), ('Gen 4', 2, 6)],
       dtype=[('Gen', (np.str_, 10)), ('30 grados', np.int32), ('35 grados', np.int32)])

# Creación del array estructurado de costos
costos_struct = np.array([('Gen 1', 3.5), ('Gen 2', 5), ('Gen 3', 7), ('Gen 4', 4.3)],
       dtype=[('Gen', (np.str_, 10)), ('Costo', np.float32)])

# Obtención del costo unitario
costo_unitario = (costos/produccion.T).T

# Creación del array estructurado del costo unitario
costounitario_struct = np.array([('Gen 1', 0.7, 1.16666667), ('Gen 2', 0.45454545, 0.71428571), ('Gen 3', 1.75, 0.77777778), ('Gen 4', 2.15, 0.71666667)],
       dtype=[('Gen', (np.str_, 10)), ('Costo unitario: 30 grados', np.float64), ('Costo unitario: 35 grados', np.float64)])

# Creación del array estructurado con todas las categorías.
ejercicio1_struct= np.array([('Gen 1', 5, 3, 3.5, 0.7, 1.16666667),
                             ('Gen 2', 11, 7, 5, 0.45454545, 0.71428571),
                             ('Gen 3', 4, 9, 7, 1.75, 0.77777778),
                             ('Gen 4', 2, 6, 4.3, 2.15, 0.71666667)],
       dtype=[('Gen', (np.str_, 10)), ('30 grados', np.int32), ('35 grados', np.int32), ('Costo', np.float32),
              ('Costo unitario: 30 grados', np.float64), ('Costo unitario: 35 grados', np.float64)])

print(ejercicio1_struct)