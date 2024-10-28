import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Lenovo\Downloads\dataset\Big_Black_Money_Dataset.csv")

print("Dados carregados com sucesso!")
print(df.head())

columns_to_check = ['Country', 'Amount (USD)', 'Industry', 'Source of Money']
null_counts = df[columns_to_check].isnull().sum()
print(null_counts) 

print("antes de alterar")
print(df['Date of Transaction'].dtype)
print("Valor mínimo:", df['Amount (USD)'].min())
print("Valor máximo:", df['Amount (USD)'].max())

plt.boxplot(df['Amount (USD)'])
plt.title("Distribuição de Amount (USD) antes da remoção de outliers")
plt.show()

df['Date of Transaction'] = pd.to_datetime(df['Date of Transaction'])

Q1 = df['Amount (USD)'].quantile(0.25)
Q3 = df['Amount (USD)'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Amount (USD)'] >= (Q1 - 1.5 * IQR)) & (df['Amount (USD)'] <= (Q3 + 1.5 * IQR))]

print("depois de alterar:")
print(df['Date of Transaction'].dtype)
print(df['Date of Transaction'].head())
print("Valor mínimo:", df['Amount (USD)'].min())
print("Valor máximo:", df['Amount (USD)'].max())

plt.boxplot(df['Amount (USD)'])
plt.title("Distribuição de Amount (USD) após remoção de outliers")
plt.show()
