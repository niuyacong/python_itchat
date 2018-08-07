""" 
pip install -U wxpy


从豆瓣 PYPI 镜像源下载安装 (推荐国内用户选用):
pip install -U wxpy -i "https://pypi.doubanio.com/simple/"
"""

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
# 搜索名称包含 'wxpy'，且成员中包含 `游否` 的群聊对象

# bot = Bot(console_qr=True, cache_path=True)
# 如果你发现这样设置终端中的二维码变形了，可以尝试传入console_qr=1（或其他倍数）来进行调整字幅宽度。如果需要反色显示，可以使用负数来进行反色操作。
# wxpy_groups = bot.groups().search('不试')
bot.groups(update=True, contact_only=False)

print(bot.groups())
my_groups=bot.groups().search('来')

#找出名字包括“铲屎官”的群。假设我们有2个微信群，分别叫“铲屎官1群”、“铲屎官2群”。如果有3个或以上的铲屎群，上面这句代码也能全部找出来，并在后面的代码中实现多群同步。
my_groups[0].update_group(members_details=True)
#更新“铲屎官1群”的成员列表信息
my_groups[1].update_group(members_details=True)
#更新“铲屎官2群”的成员列表信息
@bot.register(my_groups, except_self=False)
#注册消息响应事件，一旦收到铲屎群的消息，就执行下面的代码同步消息。机器人自己在群里发布的信息也进行同步。
@bot.register(my_groups, except_self=False)
def sync_my_groups(msg):
    my_name=msg.member.name+':'
    #给转发的消息加上前缀，显示群成员名字和冒号。群成员名字从备注、群昵称、微信昵称里面按顺序自动获取。
    sync_message_in_groups(msg, my_groups, prefix=my_name) 
    #同步“铲屎官1群”和“铲屎官2群”的消息。包括文字、图片、视频、语音、文件、分享、普通表情、地图等。
bot.join()