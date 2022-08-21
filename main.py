import json
import os

import requests
from bs4 import BeautifulSoup

urlList = list()


def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            urlList.append(line)


# 获取所有视频地址
def handle_url(url):
    # 请求地址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    r = requests.get(url, headers)
    r.encoding = 'UTF-8'
    # print(r.text)   #初学很必要，至少可以看到成功获取了所有网页源代码
    all_video = BeautifulSoup(r.text, 'lxml').select('div.video-box')  # 找到所有属性为video-box的div节点
    j = 0
    num = 1
    for video in all_video:
        video_url = video.select('video')[0].attrs.get('data-original').strip()
        video_url = 'https:' + video_url  # 拼接视频url
        print("video_url=", video_url)
        name = str(num)
        savefile(video_url, name)
        num = num + 1


# 保存视频
def savefile(video_url, name):
    print("开始下载···")
    video = requests.get(video_url)
    file_name = name + '.mp4'
    f = open('F:/SYS-ACDE/Http' + '/' +
             file_name, 'ab')
    f.write(video.content)
    f.close()
    print('视频下载完成', video_url)


def get_response(html_url):
    """
    发送请求函数
    :param html_url: 请求链接
    :return: 响应对象
    """
    # 伪装浏览器 headers ---> 开发者工具里面复制粘贴
    headers = {
        # 浏览器基本身份信息
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'
    }
    # 发送请求 <Response [200]> 响应对象
    response = requests.get(url=html_url, headers=headers)
    return response



def save(title, ts_url):
    """
    保存数据
    :param title: 视频标题
    :param ts_url: ts链接
    :return:
    """
    ts_content = get_response(ts_url).content
    with open('video\\' + title + '.mp4', 'ab') as f:
        f.write(ts_content)

def get_file_name():
    print("get_file_name")


def get_m3u8_link():
    print("get_m3u8_link")



if __name__ == '__main__':
    #
    # read_from_file('D://Workspace//Project//HttpCatch//urlList.txt')
    # for URL in urlList:
    #     print(URL)
    #     handle_url(URL)
    # savefile('https://video2.51daao.com/btt1/2022/03/20220326/cho8Rs08/index.m3u8', '测试')
    command = "ffmpeg -i https://video2.51daao.com/btt1/2020/07/20200722/LDqE9Oyy/index.m3u8 -c copy F:/SYS-ACDE/Http/test2.mp4"
    os.system(command)
