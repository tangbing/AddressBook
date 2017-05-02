#!/usr/bin/python
#!encoding:utf-8

import pickle
import os

baseUrl = '/Users/tb/Desktop/userList.txt'


def point():
    print("*******************************")
    print("显示提示信息:*")
    print("显示所有联系人:0")
    print("查找联系人:1")
    print("添加联系人:2")
    print("删除联系人:3")
    print("更改联系人资料:4")
    print("退出通讯录:5")
    print("*******************************")

point()

def addUser():
    #baseUrl()
    isHas = False
    name = input('input the name who added')
    f = open(baseUrl,'rb')
    userList = pickle.load(f)
    f.close()

    for user in userList:
        if user['name'] == name:
            print('已经存在此用户')
            isHas = True
            break

    if isHas != True:
            f = open(baseUrl,'wb')
            phone = input('input the phone who added')
            email = input('input the email who added')
            userList = [{'name':name, 'phone':phone, 'email':email}]
            pickle.dump(userList,f)
            f.close()


def searchAll():
    #baseUrl()

    f = open(baseUrl,'rb')
    searchUser = pickle.load(f)
    #print('======={0}'.format(searchUser))
    for user in searchUser:
        #print(user)
        print('name:{0} phone:{1} email:{2}'.format(user['name'], user['phone'], user['email']))
    f.close()

def searchUser():
    #baseUrl()
    isHas = False
    name = input('input the name who searchUser')
    f = open(baseUrl,'rb')
    searchUser = pickle.load(f)
    for user in searchUser:
        if user['name'] == name:
            print('--------查询结果为：-------')
            print('name:{0} phone:{1} email:{2}'.format(user['name'], user['phone'], user['email'], end=''))
            isHas = True
            break
    if isHas != True:
          print('查无此人')
    f.close()



def delete():
    #baseUrl()
    isHas = False
    name = input('input the name who delete')
    f = open(baseUrl, 'rb')
    searchUser = pickle.load(f)
    f.close()


    for user in searchUser:
        print('final:{0}'.format(user['name']))
        if user['name'] == name:
            wf = open(baseUrl, 'wb')
            # 字典删除
            searchUser.remove(name)
            # 磁盘删除
            pickle.dump(name,wf)
            print('删除成功')
            isHas = True
            wf.close()
            break

    if isHas != True:
        print('要删除的用户没有找到')





def update():
    #baseUrl()

    name = input('input the name who update')
    f = open(baseUrl, 'rb')
    searchUser = pickle.load(f)
    for user in searchUser:
        if user['name'] == name:
            # 先磁盘删除
            pickle.dump(user, f)
            phone = input('input the phone who update')
            email = input('input the email who update')
            # 初始化一个字典
            newUser = {name, phone ,email}
            # 再写入磁盘
            pickle.dump(newUser, f)

            break
        else:
            print('查无此人！')
    f.close()


number = input('Eneter an selector\n')
if number == '*':
     point()
elif number == '0':
     searchAll()
elif number == '1':
      searchUser()
elif number == '2':
     addUser()
elif number == '3':
     delete()
elif number == '4':
     update()
else:
    exit()







def basicUrl():
    pass
    # # 首先判断是否有这个目录
    # if os.path.exists(baseUrl) == False:
    #    f = open(baseUrl, 'wb')
    #    temp = {'total': 0}
    #    pickle.dump(temp)
    #    f.close()
    # else:
    #     print('path:{0}'.format(baseUrl))









