#para hallar graficas en x, y, z
"""
import matplotlib.pyplot as plt
import csv 

def leer_datos(nombre_archivo):
    datos = {'x': [], 'y': []}
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)  # Saltar la primera fila si contiene encabezados
        for fila in lector_csv:
            datos['x'].append(float(fila[0]))  # Suponiendo que la primera columna es X
            datos['y'].append(float(fila[3]))  # Suponiendo que la segunda columna es Y
    return datos

def generar_grafica(datos):
    plt.plot(datos['x'], datos['y'])
    plt.title('coordenadas en z')
    plt.xlabel('tiempo [s]')
    plt.ylabel('distancia en z [mm]')
    plt.show()

# Ingresa el nombre del archivo CSV con tus datos
nombre_archivo = 'coordenadas.csv'

# Lee los datos desde el archivo
datos = leer_datos(nombre_archivo)

# Genera y muestra la gráfica
generar_grafica(datos)
"""

#para calcular la velocidad angular y aceleracion angular

"""
import numpy as np
import matplotlib.pyplot as plt
import csv
vel=[]
acel=[]
# aqui creo estas dos listas para guardar los valores de la aceleracion angular y velocidad angular ya que nos va a ayudar a realizar los calculos de forma escalar
# Función para leer datos desde un archivo CSV
def leer_datos(nombre_archivo):
    x = []
    y = []
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            x.append(float(fila[0]))  # columna X es el dato del tiempo
            y.append(float(fila[5]))  # columna Y es el dato el cual quiera derivar
    return np.array(x), np.array(y)

# Función para calcular la derivada y la segunda derivada
def calcular_derivadas(x, y):
    dx = np.diff(x)
    dy_dx = np.diff(y) / dx
    vel.append(dy_dx)
    d2y_dx2 = np.diff(dy_dx) / dx[:-1]  # Usamos dx[:-1] para que las longitudes coincidan
    acel.append(d2y_dx2)
    return dy_dx, d2y_dx2

# Nombre del archivo CSV
nombre_archivo = 'angulo.csv'

# Leer datos desde el archivo CSV
x, y = leer_datos(nombre_archivo)

# Calcular derivadas
dy_dx, d2y_dx2 = calcular_derivadas(x, y)

# Gráficos
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(x, y)
plt.title('distancia angular')
plt.xlabel('tiempo [s]')
plt.ylabel('angulo[°]')

plt.subplot(3, 1, 2)
plt.plot(x[1:], dy_dx)  # Usamos x[1:] porque la primera derivada tiene un punto menos
plt.title('velocidad angular')
plt.xlabel('tiempo[s]')
plt.ylabel('velocidad [rad/s]')

plt.subplot(3, 1, 3)
plt.plot(x[2:], d2y_dx2)  # Usamos x[2:] porque la segunda derivada tiene dos puntos menos
plt.title('aceleracion angular')
plt.xlabel('tiempo[s]')
plt.ylabel('aceleracion[rad/s^2]')

plt.tight_layout()
plt.show()
"""
#para hallar la velocidad y aceleracion en x, y, z
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
# Función para leer datos desde un archivo CSV
def leer_datos(nombre_archivo):
    x = []
    y = []
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            x.append(float(fila[0]))  # columna X es el dato del tiempo
            y.append(float(fila[5]))  # columna Y es el dato el cual quiera derivar
    return np.array(x), np.array(y)

# Función para calcular la derivada y la segunda derivada
def calcular_derivadas(x, y):
    dx = np.diff(x)
    dy_dx = np.diff(y) / dx
    d2y_dx2 = np.diff(dy_dx) / dx[:-1]  # Usamos dx[:-1] para que las longitudes coincidan
    return dy_dx, d2y_dx2

# Nombre del archivo CSV
nombre_archivo = 'angulo.csv'

# Leer datos desde el archivo CSV
x, y = leer_datos(nombre_archivo)

# Calcular derivadas
dy_dx, d2y_dx2 = calcular_derivadas(x, y)

# Gráficos
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(x, y)
plt.title('distancia angular')
plt.xlabel('tiempo [s]')
plt.ylabel('angulo[°]')

plt.subplot(3, 1, 2)
plt.plot(x[1:], dy_dx)  # Usamos x[1:] porque la primera derivada tiene un punto menos
plt.title('velocidad angular')
plt.xlabel('tiempo[s]')
plt.ylabel('velocidad [rad/s]')

plt.subplot(3, 1, 3)
plt.plot(x[2:], d2y_dx2)  # Usamos x[2:] porque la segunda derivada tiene dos puntos menos
plt.title('aceleracion angular')
plt.xlabel('tiempo[s]')
plt.ylabel('aceleracion[rad/s^2]')

plt.tight_layout()
plt.show()
"""
#para hallar la aceleracion y velocidad en x, y, z de forma escalar
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
t=[]
s=[]
# Función para leer datos desde un archivo CSV
def leer_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            t.append(float(fila[0]))  # columna X es el dato del tiempo
            s.append(float(fila[5]))  # columna Y es el dato el cual quiera derivar
    return np.array(t), np.array(s)

# Función para calcular la derivada y la segunda derivada
def calcular_derivadas(t, s):
    dx = np.diff(t)
    dy_dx = np.diff(s) / dx
    w.append(dy_dx)
    d2y_dx2 = np.diff(dy_dx) / dx[:-1]  # Usamos dx[:-1] para que las longitudes coincidan
    alfa.append(d2y_dx2)
    return 
x=[]
y=[]
z=[]
alfa=[]
w=[]
radx= 930
rady= 0
radz= 1320

# Nombre del archivo CSV
nombre_archivo = 'angulo.csv'
nombre = 'coordenadas.csv'
# Leer datos desde el archivo CSV

# Calcular derivadas
calcular_derivadas(x, y)
def leer_datos(nombre):
    with open(nombre, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)  # Saltar la primera fila si contiene encabezados
        for fila in lector_csv:
            x.append(float(fila[1]))  # Suponiendo que la primera columna es X
            y.append(float(fila[2]))  # Suponiendo que la segunda columna es Y
            z.append(float(fila[3]))  #suponiendo que la tercera columna es Z
    return 
leer_datos(nombre)
velanz=[]
velany=[]
velanx=[]
alanz=[]
alany=[]
alanx=[]
# Lee los datos desde el archivo
datos = leer_datos(nombre_archivo)
velocidadz= [u * (radz-v) for u, v in zip(w, z)]
velanz.append(velocidadz)
velocidady= [u * (rady-v) for u, v in zip(w, y)]
velany.append(velocidady)
velocidadx= [u * (radx-v) for u, v in zip(w, x)]
velanx.append(velocidadx)
acelerarz= [(u**2) * (radz-v) for u, v in zip(w, z)]
alanz.append(acelerarz)
acelerary= [(u**2) * (rady-v) for u, v in zip(w, y)]
alany.append(acelerary)
acelerarx= [(u**2) * (radx-v) for u, v in zip(w, x)]
alanx.append(acelerarx)

def generar_grafica(t, velanx):
    plt.plot(t, velanx)
    plt.title('velocidad en x')
    plt.xlabel('tiempo [s]')
    plt.ylabel('velocidad en x [mm/s]')
    plt.show()


# Genera y muestra la gráfica
generar_grafica(t, velanx)
"""