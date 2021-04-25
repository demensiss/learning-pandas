# 1. Utwórz DataFrame na podstawie list, oraz nadajmy nazwy naszym kolumnom.

import pandas as pd

films = ['Django', 'Władca pierścieni', 'Avengers']
my_films = pd.DataFrame(films)
my_films.columns = ['Filmy']
print(my_films)

# 2. Utwórz analogiczny DataFrame na podstawie słownika

d_films = {'Filmy': ['Django', 'Władca pierścieni', 'Avengers']}
my_films2 = pd.DataFrame(d_films)
print(my_films2)

# 3. Utwórz analogiczny DataFrame na podstawie Series

s_films = pd.Series(['Django', 'Władca pierścieni', 'Avengers'])
print(s_films)




