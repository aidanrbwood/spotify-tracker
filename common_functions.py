#!/usr/bin/python3

import os.path

#def check_for_files():
usr = './user_info'
data = './databases'
if not os.path.isdir(usr):
	os.mkdir(usr)
if not os.path.isdir(data):
	os.mkdir(data)

