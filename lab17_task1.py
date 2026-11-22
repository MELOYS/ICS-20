import pandas as pd
import numpy as np

df = pd.read_csv('vectors', sep=r'\s+',
                 names=['Vector', 'X', 'Y'])

print('Вхідні дані:')
print(df)

length = np.sqrt(df['X']**2 + df['Y']**2)

df2 = pd.DataFrame({
    'Vector': df['Vector'],
    'Length': length
})

print('\nДовжини векторів:')
print(df2)

df2.to_csv('vector_len.csv', index=False)

print('\nДані збережено у файл vector_len.csv')