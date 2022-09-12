import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import Gui

max_download_number = 10


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = Gui.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    sys.exit(app.exec_())



    # url = "http://bttcj.com/inc/jsonsapi.php?ac=videolist&pg=%1"
    # request = requests.get(url, headers)
    # get_result = request.json()
    # print(get_result)
    # lst = get_result['data']
    # print("请输入文件存放路径")
    # store_path = input()
    # for y in lst:
    #     title = y['vod_title']
    #     title = title.replace('[', '')
    #     title = title.replace(']', '')
    #     title = title.replace('！', '')
    #     title = title.replace('，', '')
    #     title = title.replace('。', '')
    #     title = title.replace(' ', '')
    #     print(title)
    #     path = y['vpath']
    #     path = path.lstrip('第1集$')
    #     path = path.rstrip('$ckplayer')
    #     print(path)
    #     command = "ffmpeg -i " + path + " -c copy F:/SYS-ACDE/Http/test" + title + ".mp4"
    #     print(command)
    #     os.system(command)
