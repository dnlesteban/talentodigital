import pandas 	as pd # necesario en pd.DataFrame() para crear el DataFrame.
import numpy 	as np # necesario ens np.random para generar datos aleatorios (randint, normal, choice), y np.random.seed().
import seaborn 	as sns # necesario en funciones de Seaborn (histplot, kdeplot, jointplot, pairplot, set).
import matplotlib.pyplot as plt # necesario en plt.title(), plt.xlabel(), plt.ylabel(), plt.legend(), plt.show(), plt.gca().get_legend().

sns.set(style='whitegrid', palette='muted') # Configurar estilo general
np.random.seed(55)

data = {'Edad': np.random.randint(18, 25, 100),
        'Horas_de_estudio': np.random.randint(5, 30, 100),
        'Calificacion': np.random.normal(75, 10, 100).clip(0, 100),
        'Genre': np.random.choice(['femenino', 'masculino'], 100), # Cambié a genre porque me marca una especie de error al usar variables y etiquetas del mismo nombre o parecidos... Genero / Género... cosas de python. XD
        'Deporte': np.random.choice(['Futbol', 'Basquet', 'Natación', 'Voley'],100)
        }

df = pd.DataFrame(data)

sns.histplot(data=df, x='Horas_de_estudio', hue='Genre', bins=20, multiple='stack')
plt.title('Horas de estudio por género')
plt.xlabel('Horas de estudio')
plt.ylabel('Frecuencia')

