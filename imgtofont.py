""" 
识别图片上的文字
GitHub项目中的wiki找到tesseract exe文件
下载好的语言包放入到安装目录中的testdata下即可。在windows系统你还需要将testdata目录也加入环境变量。
命令行运行：
tessract
tessract test.png outfile -l chi_sim(最后一个是语言包的包名，语言包的下载压在git上，下载好的语言包放到tessract.data文件夹中即可)
1、pip install pillow
2、pip install pytesseract


如遇错误：pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your path
打开pytesseract.py 即安装路径"\python\Anaconda\lib\site-packages\pytesseract\pytesseract.py"
修改tesseract_cmd = 'D:\\play_install\\Tesseract-OCR\\tesseract.exe' 为tesseract的安装路径



"""

from PIL import Image
import pytesseract

class Languages:
    CHS='chi_sim',
    CHT='chi_tra',
    ENG='ENG'


def img_to_str(image_path="2.jpg",lang=Languages.CHT):
    return pytesseract.image_to_string(Image.open(image_path),lang)

print(img_to_str())



""" 
百度云免费试用的文字识别
https://cloud.baidu.com
进入百度云 开一个文字识别的应用，有开发文档
"""
from aip import AipOcr

# APP_ID = '你的 App ID'
# API_KEY = '你的 Api Key'
# SECRET_KEY = '你的 Secret Key'

APP_ID = '11647195'
API_KEY = '0DsQ0dXLoh4FVMlBrzRIt7Pe'
SECRET_KEY = 'NrGhXK0Ke9FSWE1ZggNgVsuGvskbtE47'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('2.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
print(client.basicGeneral(image))

