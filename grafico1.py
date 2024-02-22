import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Calificaciones de Ciencias')
plt.grid(False)
plt.show()

# Gráfico de barras de error con plt.errorbar()
materias = ['Matemáticas', 'Ciencias', 'Literatura']
calificaciones_promedio = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

# Usar un solo color para todos los elementos
color = 'skyblue'
plt.figure(figsize=(10, 6))
plt.errorbar(materias, calificaciones_promedio, yerr=np.transpose(errores), fmt='o', capsize=5, color='skyblue', label='Promedio')
plt.title('Calificaciones Promedio con Barras de Error')
plt.xlabel('Materias')
plt.ylabel('Calificación Promedio')
plt.legend(bbox_to_anchor=( 0.17, 1), loc='upper right', ncol=1)  # Ajustar la posición y el número de columnas
plt.grid(False)
plt.show()

# Histograma
plt.figure(figsize=(10, 6))
plt.hist(matematicas, bins=10, color='blue', edgecolor='blue')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Frecuencia')
plt.grid(False)
plt.show()