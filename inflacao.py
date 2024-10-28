import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/inflacao.csv')

print("Dados carregados com sucesso!")
print(df.head())
print(df.dtypes)

null_counts = df.isnull().sum()
print(null_counts)

df['referencia'] = pd.to_datetime(df['referencia'], errors='coerce')
print(df.dtypes)


coluna_ipca = 'ipca_variacao'


Q1 = df[coluna_ipca].quantile(0.25)
Q3 = df[coluna_ipca].quantile(0.75)
IQR = Q3 - Q1


limite_inferior_ipca = Q1 - 1.5 * IQR
limite_superior_ipca = Q3 + 1.5 * IQR

outliers_iqr_ipca = df[(df[coluna_ipca] < limite_inferior_ipca) | (df[coluna_ipca] > limite_superior_ipca)]
outliers_iqr_ipca_count = outliers_iqr_ipca.shape[0]


coluna_salario = 'salario_minimo'


media_salario = df[coluna_salario].mean()
desvio_salario = df[coluna_salario].std()


limite_inferior_salario = media_salario - 3 * desvio_salario
limite_superior_salario = media_salario + 3 * desvio_salario


outliers_std_salario = df[(df[coluna_salario] < limite_inferior_salario) | (df[coluna_salario] > limite_superior_salario)]
outliers_std_salario_count = outliers_std_salario.shape[0]

print(outliers_iqr_ipca_count, outliers_std_salario_count)



# Gráfico de inflação ao longo do tempo
df.plot(x='referencia', y='ipca_variacao', kind='line', title="Evolução da Inflação (IPCA)")
plt.show()

# Gráfico do salário mínimo ao longo do tempo
df.plot(x='referencia', y='salario_minimo', kind='line', title="Evolução do Salário Mínimo")
plt.show()









