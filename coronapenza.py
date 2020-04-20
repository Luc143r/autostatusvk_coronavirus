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
    result2 = soup.find(class_ = 'info_blk stat_block cured').text
    result3 = soup.find(class_ = 'info_blk stat_block deaths').text
    statistic = ('🦠В Пензенской области: {0} заражений☣ {1} новых за сутки🆕 {2} выздоровлений♻ {3} смертей💀🦠#stayhome'.format(numbers_from_string(result1[0]), result1[1], numbers_from_string(result2), numbers_from_string(result3)))
    return(statistic)