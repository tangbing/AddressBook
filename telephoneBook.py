#!/usr/bin/python
#!encoding:utf-8


import os
import pickle


itemList = []
baseUrl = '/Users/mac/Desktop/userList.data'

def menu():
    print("*******************************")
    print("显示所有联系人:0")
    print("查找联系人:1")
    print("添加联系人:2")
    print("删除联系人:3")
    print("更改联系人资料:4")
    print("退出通讯录:5")
    print("*******************************")

def customRead():
    if os.path.exists(baseUrl) == True:
        p = open(baseUrl,'rb')
        global itemList
        itemList = pickle.load(p)
        #print('read:{0}'.format(itemList))
        print('读文件成功')
        p.close()
    else:
        fp = open(baseUrl, 'w')
        fp.close()
        print('磁盘没有文件创建文件')


def customWrite():
    p = open(baseUrl,'wb')
    global itemList
    pickle.dump(itemList, p)
    print('写入文件成功')
    p.close()

def searchAll():
    #print('searchAll:itemList:{0}'.format(itemList))
    if len(itemList) <=0:
        print('没有查询到')
        return
    for user in itemList:
        #print('searchAll:{0}'.format(user))
        print('phone:{0} name:{1} email:{2}'.format(user['phone'], user['name'], user['email']))
    print('查询所用成功')

def searchUser():
    isHas = False
    phone = input('input the phone who searchUser')
    for user in itemList:
        if user['phone'] == phone:
            print('--------查询结果为：-------')
            print('phone:{0} name:{1} email:{2}'.format(user['phone'], user['name'], user['email'], end=''))
            isHas = True
            break
    if isHas != True:
        print('查无此人')


def addUser():
    isHas = False
    phone = input('input the phone who added')
    for user in itemList:
        if user['phone'] == phone:
            print('已经存在此用户')
            isHas = True
            break

    if isHas != True:
            name = input('input the name who added')
            email = input('input the email who added')
            itemList.append({'name':name, 'phone':phone, 'email':email})
            print('添加成功')


def deleteUser():
    phone = input('input the phone who delete')
    isHas = False

    for user in itemList:
        if user['phone'] == phone:
            # 字典删除
            itemList.remove(user)
            print('删除成功')
            isHas = True
            break

    if isHas != True:
        print('要删除的用户没有找到')

def updateUser():
    isHas = False
    phone = input('input the phone who update')
    for user in itemList:
        if user['phone'] == phone:
            # 先删除找到的
            itemList.remove(user)
            name = input('input the name who update')
            email = input('input the email who update')
            # 初始化一个字典
            itemList.append({'name': name, 'phone': phone, 'email': email})
            print('修改成功')
            isHas = True
            break
    if isHas != True:
        print('查无此人！')




customRead()
while True:
    menu()
    number = input('Eneter an selector\n')
    if number == '0':
        searchAll()

    elif number == '1':
        searchUser()

    elif number == '2':
        addUser()
        customWrite()

    elif number == '3':
        deleteUser()
        customWrite()

    elif number == '4':
        updateUser()
        customWrite()
    else:
        exit()






