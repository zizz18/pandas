import pandas as pd

#svod = pd.read_csv("Свод.csv", delimiter=';', encoding='1251', low_memory=False)
month = pd.read_csv("январь.csv", delimiter=';', encoding='1251', low_memory=False)

print(month.columns.tolist())
#print(svod[['Наименование ДОО', 'Январь']].iloc[1:6])
#print(svod[svod['Январь'].isin(['60'])])
#print(svod[['Наименование ДОО', 'Январь']][1:6])
'''
zn = svod['Январь'][1]
dn = svod['Наименование ДОО'][0]
print(zn)
dn = dn.replace('/', '') # замена в строке
print(dn)
svod.at[0,'Наименование ДОО'] = dn # присваивание значения ячейке
print(svod['Наименование ДОО'][0:5]) # вывод среза
print(svod[['Январь']][0:10])
'''
