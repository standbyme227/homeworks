import re

import os, errno
import requests
from bs4 import BeautifulSoup
from pathlib import Path


def get_week_list(refresh_html=False):


    # 프로젝트 컨테이너 폴더 경로
    path_module = os.path.abspath(__name__) #__name__ 모듈이라는 파일이 있는 위치를 뽑아내기위한 abspath
    print(f'path_module: {path_module}')
    root_dir = os.path.dirname(path_module)
    print(f'root_dir: {root_dir}')


    # root_dir = os.path.dirname(os.path.abspath(__name__))
    # print(f'root)dir: {root_dir}')
    # data폴더 경로
    path_data_dir = os.path.join(root_dir, 'data')
    print(f'path_data_dir: {path_data_dir}')


    os.makedirs(path_data_dir, exist_ok=True)
    # 폴더를 만든다. path_data_dir라는 건 아예 폴더의 path이기 때문에 만들어지며,
    # exist_ok=True라는건 겹치는게 있어도 오류는 나지않게 하기위해서이다.


    url_week_chart = 'http://comic.naver.com/webtoon/weekday.nhn'
    # 우리가 원하는 곳의 url

    # 'xt'모드(wt처럼 덮어쓰지 않는다.)와 try-except문을 쓸 경우
    file_path = os.path.join(path_data_dir, 'naver_webtoon_list.html')
    try:
        with open(file_path, 'xt') as f:
            # 연다음에 파일이 있는지를 검사해야하기 때문에. response를 안에다 넣었다.
            response = requests.get(url_week_chart)
            source = response.text
            f.write(source)
    except FileExistsError as e:
        print(f'"{file_path}" file is already exists!')



    # 파일이 없을 경우를 검사후 로직 실행 if문!!!
    file_path = os.path.join(path_data_dir, 'naver_webtoon_list.html')
    print(f'file_path: {file_path}')
    if not os.path.exists(file_path):
        response = requests.get(url_week_chart)
        source = response.text
        with open(file_path, 'wt') as f:
            f.write(source)
    else
        print(f'"{file_path}" file is already exists!')

    # url이 하나일 경우 이렇게하고 2개면 url을 변경해서 하면된다.



    # file_path = os.path.join(path_data_dir, 'url_week_chart.html')
    # with open(file_path, 'wt') as f:
    #     response = requests.get(url_week_chart)
    #     source = response.text
    #     f.write(source)



    # # url에서 받아온 html정보를 data폴더에 저장
    # response = requests.get(url_week_chart)
    # source = open(os.path.join(path_data_dir, 'naver_webtoon_list.html'), 'wt', encoding='utf8').write(response.text)
    # # source = open('naver_webtoon_list.html', 'rt', encoding='utf8').read()
    # soup = BeautifulSoup(source, 'lxml')



    # result = []
    # for div in soup.find_all('div', class_='col'):
    #     week_webtoon = div.find('h4').text
    #     result.append(week_webtoon)
    #     for ul in div.find_all('ul'):
    #         # print(f'\n-------{week_webtoon}-------\n')
    #         for li in ul.find_all('li'):
    #             title = li.find('a', class_='title').text
    #             # li안을 find해서 class를 'title'로 갖는 'a'의 text를 찾아라
    #             id_link = li.find('a').get('href')
    #             match_id = re.search(r'\d+', id_link)
    #             webtoon_id = match_id.group()
    #
    #             img_url = li.find('img').get('src')
    #             result.append({
    #                 'Id': webtoon_id,
    #                 'Title' : title,
    #                 'Img_url' : img_url,
    #             })
    #             webtoon_list = open('webtoon_list.html', 'wt', encoding='utf8').write(str(result))
    # # 이 리스트를 확인해서



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