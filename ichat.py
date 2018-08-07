
""" 
安装：pip install itchat
"""

import itchat
itchat.auto_login(hotReload=True)

def send_onegroup(msg,gname):
    rooms=itchat.get_chatrooms(update=True,)
    rooms=itchat.get_chatrooms(gname)
    print(rooms)
    # if rooms is not None:
    #     for i in range(len(rooms)):
    #         username=rooms[0]['UserName']
    #         itchat.send(msg,toUserName=username)
    # else:
    #     print('no groups')

if __name__=="__main__":
    send_onegroup(msg='如果你看到这句话，请忽略。。',gname='来')