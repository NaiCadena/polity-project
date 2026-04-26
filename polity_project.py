import pandas as pd

# Cargar base de datos Polity V
path = '/Users/naicadena/Documents/Projects/polity-project /p5v2018.xls'
polity = pd.read_excel(path)

# Exploración inicial
print(polity.shape)
print(polity.columns)
print(polity.head())

polity[["country", "year", "polity", "polity2", "democ", "autoc"]].head(10)
usa = polity[polity["country"] == "United States"]

usa[["year", "polity2"]].tail(10)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(usa["year"], usa["polity2"])
plt.title("Polity2 – Estados Unidos")
plt.xlabel("Año")
plt.ylabel("Polity2")
plt.show()






