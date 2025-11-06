import numpy as np 
import random 
import argparse 

parser = argparse.ArgumentParser(description= "Programa de saludo")
parser.add_argument("--saludo", default = "saluda primero")
args = parser.parse_args()

mensaje = str(args.saludo)

dr = random.randint(1,100)
try:
    if mensaje == "Hola":
        if dr <=50:
            print("Hola, como estas?")
        elif dr <=75:
            print("Hola, me llamo computina")
        else:
            print("Hablale a la mano")
    else:
        print("Saluda primero")
except:
    print("algo hiciste mal")