import numpy as np 
import pandas as pd 
import argparse 

#Creacion de un obejto de coneccion 
parser = argparse.ArgumentParser(description = "Programa en python que grafica histogramas dados sus parametros") #Igual siempre 
parser.add_argument("media", help = "Valor promedio del histograma") #Solo cambia el arguemnto 
parser.add_argument("desv", help = "Error estandar del hostograma") #Solo cambia el argumento 
parser.add_argument("--n", default = 100, help = "Tamaño de muestro")
args =parser.parse_args() #igual siempre 

n = int(args.n)
media = float(args.media)
desv = float(args.desv)

#Generar datos aleatorios cpn distribucion normal clear
datos = np.random.normal(size = n, loc = media, scale = desv) 
datos = datos.round(0).astype(int) 

#Eliminar valores atipocos 
datos_trim = [] 
for i in range(len(datos)): 
  if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv: 
    datos_trim.append(datos[i]) 

datos_trim = pd.DataFrame(datos_trim) 
datos_trim.columns = ['Datos'] 

#Generar un historigrama de los datos
histograma = datos_trim.groupby('Datos').size() 

for i in range(len(histograma)): 
  if histograma.index[i]>=0: 
    s = "+" 
  else: 
    s = "" 
  print( 
    s, 
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                       abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), 

    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = "" 
    )
    