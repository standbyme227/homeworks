import re

import os, errno
import requests
from bs4 import BeautifulSoup
from pathlib import Path


def get_week_list(refresh_html=False):



    path_module = os.path.abspath(__name__) #__name__ 모듈이라는 파일이 있는 위치를 뽑아내기위한 abspath
    root_dir = os.path.dirname(path_module)
    path_data_dir = os.path.join(root_dir, 'data')


    os.makedirs(path_data_dir, exist_ok=True)

    url_week_chart = 'http://comic.naver.com/webtoon/weekday.nhn'
    file_path = os.path.join(path_data_dir, 'naver_webtoon_list.html')
    try:
        file_mode = 'wt' if refresh_html else 'xt'
        with open(file_path,file_mode) as f:
            response = requests.get(url_week_chart)
            source = response.text
            f.write(source)
    except FileExistsError as e:
        print(f'"{file_path}" file is already exists!')


    result = []
    for div in soup.find_all('div', class_='col'):
        week_webtoon = div.find('h4').text
        result.append(week_webtoon)
        for ul in div.find_all('ul'):
            # print(f'\n-------{week_webtoon}-------\n')
            for li in ul.find_all('li'):
                title = li.find('a', class_='title').text
                # li안을 find해서 class를 'title'로 갖는 'a'의 text를 찾아라
                id_link = li.find('a').get('href')
                match_id = re.search(r'\d+', id_link)
                webtoon_id = match_id.group()

                img_url = li.find('img').get('src')
                result.append({
                    'Id': webtoon_id,
                    'Title' : title,
                    'Img_url' : img_url,
                })
                webtoon_list = open('webtoon_list.html', 'wt', encoding='utf8').write(str(result))
                # print(f'제목 : {title}, Id : {webtoon_id}, Img_url : {img_url}')






# result = []
# for div in soup.find_all('div', class_='col'):
#     week_webtoon = div.find('h4').text
#
#     for ul in div.find_all('ul'):
#         # print(f'\n-------{week_webtoon}-------\n')
#         webtoon_list = []
#         for li in ul.find_all('li'):
#             title = li.find('a', class_='title').text
#             # li안을 find해서 class를 'title'로 갖는 'a'의 text를 찾아라
#             id_link = li.find('a').get('href')
#             match_id = re.search(r'\d+', id_link)
#             webtoon_id = match_id.group()
#
#             img_url = li.find('img').get('src')
#             webtoon_list.append({
#                 'title' : title,
#                 'id' : webtoon_id,
#                 'img_url' : img_url,
#             })
#             week_webtoon_dict = {week_webtoon : webtoon_list}
#     result.append(week_webtoon_dict)
#
# print(week_webtoon_dict[week_webtoon[webtoon_list['신의 탑']]])
#                 # print(f'제목 : {title}, Id : {webtoon_id}, Img_url : {img_url}')