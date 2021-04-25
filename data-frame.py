import pandas as pd

# Tworzenie DataFrame z pliku
names = pd.read_excel('D:\python\pandas-tutorial\db\imiona.xlsx')
print(names)

# Tworzenie pustego DataFrame
set = pd.DataFrame()
print(set)

# Tworzenie DataFrame na podstawie listy i nazywanie kolumny

list = [1,2,5,7]
my_list = pd.DataFrame(list)
my_list.columns = ['Liczby']
print(my_list)

# Tworzenie wielokolumnowych list

list2 = [[1,2,5,7],[11,22,55,77]]
df = pd.DataFrame(list2)
df.columns = ['One', 'Two', 'Tree', 'Four']
print(df)

# Tworzenie DataFrame na podstawie słownika

dictionary = {'Imie': ['Ania', 'Michal', 'Przemek'], 'Wiek': [18,25,40]}
print(pd.DataFrame(dictionary))

# Tworzenie DataFrame na podstawie series

s = pd.Series([11,33,55,99])
print(s)

