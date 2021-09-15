# работа со временем

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