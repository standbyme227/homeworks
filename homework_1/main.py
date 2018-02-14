import re
from bs4 import BeautifulSoup
from utils import get_week_list

source = open('melon.html', 'rt').read()
soup = BeautifulSoup(source, 'lxml')



if __name__ == '__main__':
    result = get_week_list()
    for item in result:
        print(item)