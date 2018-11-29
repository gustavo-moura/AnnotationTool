import pandas
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

d = pandas.read_csv(r'dados/empreendedorismo.csv', sep=',')

data = d.drop(columns='NUSP')
parallel_coordinates(data, 'Resultado', color=[[0,1,0,0.9],[1,0,0,0.2]])
plt.show()