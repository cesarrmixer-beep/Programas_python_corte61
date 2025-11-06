#importar las librerias 
import numpy as np 
import pandas as pd 
import argparse 


parser = argparse.ArgumentParser(description="Resumen estadistico")
parser.add_argument("input",help="Archivo csv")

args = parser.parse_args()
df = pd.read_csv(args.input)

print(df.describe())

