#!/bin/usr/python
# find the filenames with string "User not found" from 1500 json files
import json
import os
import os.path


file_list = os.listdir("jsons")
count = 0 
for file_name in file_list:
    with open(os.path.join("jsons", file_name), "r") as src_file:
        data = src_file.read()
        if "User Not Found" in data:
            count = count + 1
            print file_name

print "total number of time string found:",count  
