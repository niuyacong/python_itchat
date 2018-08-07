#coding=utf-8
import itchat
from itchat.content import *

import asyncio
# (TEXT,MAP,isGroupChat=True)([TEXT,MAP,CARD,NOTE])
@itchat.msg_register([TEXT,MAP,CARD,NOTE],isGroupChat=True)
def text_reply(msg):
    group=itchat.get_chatrooms(update=True,)
   
    from_user = ''
    for g in group:
        if g['NickName'] == '来123':#从群中找到指定的群聊
            from_group = g['UserName']
            ChatRoom = itchat.update_chatroom(from_group, detailedMember=True)
            for menb in ChatRoom['MemberList']:
                #print(menb['NickName'])
                if menb['NickName'] == "柒年":#从群成员列表找到用户,只转发他的消息
                    from_user = menb['UserName']
                    for j in group:
                        if j['NickName'] == '来':#把消息发到这个群
                            to_group = j['UserName']
                            if msg['ToUserName'] == from_group:
                                if msg['FromUserName'] == from_user:
                                    itchat.send('%s'%(msg['Content']),to_group)


# @itchat.msg_register(PICTURE,RECORDING,ATTACHMENT,VIDEO,isGroupChat=True)
# def download_files(msg):
#     msg['Text']('F:\\'+msg['FileName'])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO],isGroupChat=True)
def group_pic(msg):
    group=itchat.get_chatrooms(update=True,)
    from_user = ''
    for g in group:
        if g['NickName'] == '来123':#从群中找到指定的群聊
            from_group = g['UserName']
            ChatRoom = itchat.update_chatroom(from_group, detailedMember=True)
            for menb in ChatRoom['MemberList']:
                if menb['NickName'] == "柒年":#从群成员列表找到用户,只转发他的消息
                    from_user = menb['UserName']
                    for j in group:
                        if j['NickName'] == '来':#把消息发到这个群
                            to_group = j['UserName']
                            if msg['ToUserName'] == from_group:
                                if msg['FromUserName'] == from_user:
                                    msg['Text'](msg['FileName']) 
                                    if msg['Type']=="Picture":
                                        itchat.send_image(fileDir=msg['FileName'],toUserName=to_group)
                                    if msg['Type']=="Recording":
                                        itchat.send_file(fileDir=msg['FileName'],toUserName=to_group)
                                    if msg['Type']=="Attachment":
                                        itchat.send_file(fileDir=msg['FileName'],toUserName=to_group)
                                    if msg['Type']=="Video":
                                        itchat.send_video(fileDir=msg['FileName'],toUserName=to_group)
async def init(loop):
    itchat.auto_login(hotReload=True)
    itchat.run()


loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()