# Regresión Lineal Simple: Horas de Estudio vs Calificaciones

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import statsmodels.api as sm
from scipy import stats

# Datos: Horas de estudio (X) y calificaciones (Y)
horas_estudio = np.array([1, 2, 4, 5, 6, 8, 9, 10, 12, 15]).reshape(-1, 1)
calificaciones = np.array([55, 60, 65, 70, 78, 80, 85, 92, 95, 100])

# Visualización de los datos
plt.figure(figsize=(8, 6))
plt.scatter(horas_estudio, calificaciones, color='blue', label='Datos reales')
plt.xlabel('Horas de estudio')
plt.ylabel('Calificación')
plt.title('Horas de estudio vs Calificaciones')
plt.grid(True)
plt.legend()
plt.show()

# Entrenar modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(horas_estudio, calificaciones)

# Parámetros del modelo
beta_0 = modelo.intercept_
beta_1 = modelo.coef_[0]
print('Modelo ajustado exitosamente')
print(f'Intercepto (b0): {beta_0:.2f}')
print(f'Pendiente (b1): {beta_1:.2f}')

# Predicciones
y_prediction = modelo.predict(horas_estudio)
print('Predicciones realizadas')

# Visualización: Datos + Línea de ajuste
plt.figure(figsize=(8, 6))
plt.scatter(horas_estudio, calificaciones, color='blue', label='Datos reales')
plt.plot(horas_estudio, y_prediction,
         color='red',
         label='Predicción (línea de ajuste)')
plt.xlabel('Horas de estudio')
plt.ylabel('Calificación')
plt.title('Regresión Lineal Simple')
plt.grid(True)
plt.legend()
plt.show()

# Métricas de evaluación
mse = mean_squared_error(calificaciones, y_prediction)
mae = mean_absolute_error(calificaciones, y_prediction)
r2 = r2_score(calificaciones, y_prediction)

print(f'Error cuadrático medio (MSE): {mse:.2f}')
print(f'Error absoluto medio (MAE): {mae:.2f}')
print(f'Coeficiente de determinación (R²): {r2:.2f}')

# Modelo con statsmodels para obtener resumen estadístico
x_sm = sm.add_constant(horas_estudio)  # Agrega constante para el intercepto
modelo_sm = sm.OLS(calificaciones, x_sm).fit()

print('\nResumen del modelo (statsmodels):')
print(modelo_sm.summary())

# Test de normalidad de residuos (Shapiro-Wilk)
residuos = modelo_sm.resid
stat, p_value = stats.shapiro(residuos)

print('--------------------------------------------------')
print(f'Estadístico de Shapiro-Wilk: {stat:.3f}')
print(f'P-valor: {p_value:.3f}')
if p_value > 0.05:
    print('✅ Los residuos parecen seguir una distribución normal (no se rechaza H₀).')
else:
    print('❌ Los residuos no siguen una distribución normal (se rechaza H₀).')
print('--------------------------------------------------')

