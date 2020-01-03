# coding=UTF-8
import time

cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n"


filename = 'test_text.txt'
with open(filename, 'a') as file_object:
    file_object.write(cur_time)
    print(cur_time)
