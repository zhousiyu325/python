#!/usr/bin/python
# -*- coding:utf-8 -*-

passwd_list = ['*#*#', '12345']

def account_login():
    tries = 3
    while tries >0:
        password = raw_input("input password:")
        password_correct = password == passwd_list[-1]
        password_reset = password == passwd_list[0]

        if password_correct:
           print "successful login"

        elif password_reset:
            new_password = raw_input('Enter a new password :')
            passwd_list.append(new_password)
            print "Password has changed successfully!"
            account_login()
        else:
            print 'Wrong password or invalid input!'
            tries = tries - 1
            print tries, 'times left'
    else:
        print "your accout has been suspended"

account_login()