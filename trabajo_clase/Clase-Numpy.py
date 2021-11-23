import numpy as np

'''
array_1D = np.array((1,2,3)) #Podemos pasar listas [] o tuplas (). Todas separadas por comasy encerradas en corchetes
print(array_1D)
array_1D.ndim

array_2D = np.array([(1,2,3), (4,5,6)],)
print(array_2D.ndim)
print(array_2D.shape)
print(len(array_2D))

array_3D = np.array([([1,2],[3,4]),
                     ([5,6], [6,7])])

# biomasa en unidades de absorbancia
ecoli_matraz = np.array([0.1, 0.15, 0.19, 0.5,.9, 1.4, 1.8, 2.1, 2.3])
print(ecoli_matraz.ndim)
print(ecoli_matraz.shape)
print(len(ecoli_matraz))

ecoli_m_b = np.array([[0.1, 0.15, 0.19, 0.5,  # Matraz 250 mL
                       0.9, 1.4, 1.8, 2.1, 2.3],
                      [0.1, 0.17, 0.2, 0.53,  # Biorreactor 50 L
                       0.97, 1.43, 1.8, 2.1,  2.8],
                      [0.1, 0.17, 0.2, 0.52,  # B. alimentado 50 L
                       0.95, 1.41, 1.8, 2.2,  2.8]
                    ])
'''

#Ejercicio 1.

produccion = np.array([ [5,3], [11, 7], [4, 9], [2, 6]])
costos = np.array([3.5, 5, 7, 4.3])
costo_unitario = (costos/produccion.T).T

menor_costo = costo_unitario.min()
mayor_costo = costo_unitario.max()

menor_costo_bool = costo_unitario==menor_costo
mayor_costo_bool = costo_unitario==mayor_costo