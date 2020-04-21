import requests
from bs4 import BeautifulSoup
import re
def numbers_from_string(data):
    result = "".join(re.findall(r'\d+', data))
    return result
def parsepenza():
    r = requests.get('https://coronavirus-monitor.info/country/russia/penzenskaya-oblast/')
    soup = BeautifulSoup(r.text, 'html.parser')
    result1 = soup.find(class_ = 'info_blk stat_block confirmed').text.split('+')
    result2 = soup.find(class_ = 'info_blk stat_block cured').text.split('+')
    result3 = soup.find(class_ = 'info_blk stat_block deaths').text.split('+')
    zarazh1 = "☣{0} заражений".format(numbers_from_string(result1[0]))
    health1 = "♻{0} выздоровлений".format(numbers_from_string(result2[0]))
    death1 = "💀{0} смертей".format(numbers_from_string(result3[0]))
    if len(result1) == 2:
        zarazh0 = "☣{0} заражений🆕{1} новых за сутки".format(numbers_from_string(result1[0]), result1[1])
        statistic = ('🦠В Пензенской области: {0}{1}{2}🦠#stayhome🏡'.format(zarazh0, health1, death1))
        print('If_one_true')
        if len(result2) == 2:
            health0 = "♻{0} выздоровлений🆕{1} новых за сутки".format(numbers_from_string(result2[0]), result2[1])
            statistic = ('🦠В Пензенской области: {0}{1}{2}🦠#stayhome🏡'.format(zarazh0, health0, death1))
            print('If_two_true')
            if len(result3) == 2:
                death0 = "💀{0} смертей🆕{1} новых за сутки".format(numbers_from_string(result3[0]), result3[1])
                statistic = ('🦠В Пензенской области: {0}{1}{2}🦠#stayhome🏡'.format(zarazh0, health0, death0))
                print('If_three_true')
    else:
        statistic = ('🦠В Пензенской области: {0}{1}{2}🦠#stayhome🏡'.format(zarazh1, health1, death1))
        print('Ifs_false')
    return(statistic)

#stat = parsepenza()
#print(stat)