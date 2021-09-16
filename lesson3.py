# работа со временем
"""
from datetime import datetime, date, timedelta
import locale
 
locale.setlocale(locale.LC_ALL, 'russian')
dt = datetime.now()
delta = timedelta(days=1)

print((dt-delta).strftime('%A %d %B %Y'))
print(dt.strftime('%A %d %B %Y'))

delta = timedelta(days=30)
print((dt-delta).strftime('%A %d %B %Y'))

string = "01/01/25 12:10:03.234567"
print(datetime.strptime(string, '%m/%d/%y %H:%M:%S.%f'))

# чтение из файла
with open('c:/Users/яков/Downloads/referat.txt', encoding='utf-8') as f:
    string = f.read() 
with open('referat2.txt', 'w', encoding='utf-8') as referat:
    referat.write(string.replace('.','!'))

len_string = len(string)
count_string = len(string.split())
"""
# табличный" формат csv

import csv

list_dict = [ 
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
    ]
fields = ['name','age','job']
with open('export.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f,fields,delimiter=';')
    writer.writeheader()
    for i in list_dict:
        writer.writerow(i)


    
    
 