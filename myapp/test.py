from datetime import datetime

diff_date = -20
name = 'Data_in_out_05-01-17.csv'
name = name.split('_')
name = name[3].split('.')
date =  name[0]
name = name[0].split('-')
year = '20'+name[2]

remin = datetime(int(year), int(name[0]), int(name[1])) - datetime.now()
remin = str(remin)
remin = remin.split(' ')
remin = int(remin[0])

if remin > diff_date:
    print remin