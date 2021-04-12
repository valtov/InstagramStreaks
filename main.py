from bs4 import BeautifulSoup
import json

dates = {}
for i in range(1,13):
    path = f'./messages/inbox/moonmen_bpuf_wbeaw/message_{i}.html'

    with open(path, 'r') as f:
        
        contents = f.read()

        soup = BeautifulSoup(contents, 'html.parser')


    for element in soup.find_all('div', {'class': 'pam'}):
        date1 = element.find('div', {'class':'_3-94 _2lem'}).text
        parse = ','.join(date1.split(',')[:2])
        if parse in dates:
            continue
        dates[parse] = True



with open('dates.txt', 'w') as f:
    f.write(str(dates.keys()))
