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

print(df.head())

sns.histplot(data = df, x = 'Calificacion', kde = True, bins = 20, color='skyblue')
plt.title('Distribución de calificaciones')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.show()

sns.kdeplot(data = df, x = 'Horas_de_estudio', fill = True, color = 'green')
plt.title('Estimación de densidad de horas de estudio')
plt.xlabel('Horas de estudio')
plt.ylabel('Densidad')
plt.show()

sns.kdeplot(data = df, x = 'Horas_de_estudio', hue = 'Genre', fill = True, multiple = 'stack')
plt.title('Horas de estudio por género')
plt.xlabel('Horas de estudio')
plt.ylabel('Densidad')
# plt.legend(title = 'Género') # No es necesario y causa algun tipo de conflicto si el title ya está en el hue = 
plt.show()


'''O RIGINAL
sns.histplot(data=df, x = 'Horas_de_estudio', hue='Genre',kde=True, bins=20, multiple='stack')
plt.title('Horas de estudio por genero')
plt.xlabel('Horas de estudio')
plt.ylabel('Frecuencia')
plt.legend(title='Género')  
plt.show()

hue compitiendo con title
Si usas hue=... en seaborn, generalmente se dibuja la leyenda automáticamente.
Si luego llamas a plt.legend() sin argumentos para cambiar el título, aparece un warning.

otra cosita... XD
kde=True le dice a seaborn que además de mostrar el histograma, trace una curva Kernel Density Estimation (estimación de densidad).
Pero cuando usas hue (para dividir por categorías) y multiple='stack', el gráfico intenta apilar los histogramas por categoría.
En esa situación, la curva KDE no se puede calcular para cada grupo apilado fácilmente, porque sns.histplot no soporta bien la combinación kde=True + multiple='stack' + hue.

'''
sns.histplot(data=df, x='Horas_de_estudio', hue='Genre', bins=20, multiple='stack')
plt.title('Horas de estudio por género')
plt.xlabel('Horas de estudio')
plt.ylabel('Frecuencia')

# Capturar la leyenda actual y cambiarle el título
leg = plt.gca().get_legend()
leg.set_title('Género')

plt.show()


''' ORIGINAL
sns.jointplot(data=df,x='Horas_de_estudio', y='Calificacion', color='red', kind='kde')
plt.suptitle('Relacion horas de estudio y calificacion', y=1.02 )
plt.show()

Problema:
jointplot devuelve su propio objeto de figura, por lo que no se debe usar el plt.suptitle() directamente sin asignar el objeto. 
Si se hace tal como está, el título puede quedar mal posicionado o no aparecer.
'''
g = sns.jointplot(data=df, x='Horas_de_estudio', y='Calificacion', color='red', kind='kde')
g.figure.suptitle('Relación horas de estudio y calificación', y=1.02)
plt.show()

''' ORIGINAL
sns.pairplot(df[['Edad','Horas_de_estudio','Calificacion']] )
plt.suptitle('Matriz entre edad, horas de estudio y calificacion', y=1.02)

sns.pairplot() muestra las relaciones entre múltiples variables, pero, al igual que con jointplot, hay un detalle con el uso de plt.suptitle():
y es que sns.pairplot() también devuelve un objeto propio (de tipo PairGrid), y plt.suptitle() podría no posicionarse bien.
'''
g = sns.pairplot(df[['Edad', 'Horas_de_estudio', 'Calificacion']])
g.fig.suptitle('Matriz entre edad, horas de estudio y calificación', y=1.02)
plt.show()

'''
En el caso de sns.pairplot(), el objeto que retorna es un seaborn.axisgrid.PairGrid, y para acceder a la figura asociada, debes usar g.fig,
no es g.figure, como ocurre con jointplot() (que sí devuelve un objeto tipo FacetGrid o JointGrid, con .figure).
sns.pairplot --> g.fig
joinplot()   --> g.figure

- Crea el mismo pairplot y guarda el objeto PairGrid devuelto en la variable g.

- Usa g.fig para acceder directamente a la figura que pairplot creó internamente.

- Llama a suptitle() sobre esa figura específica, garantizando que el título sea parte de la figura correcta.
'''



           
