#!/usr/bin/python
# https://bytes.com/topic/python/answers/870172-python-search-text-file-string-replace
import fileinput
import json
import sh


def function1():
    for line in fileinput.FileInput("mount.txt", inplace=1):
        parsed_json = json.loads(line)
        line = line.replace("old", "new")
        print(line)


def function2():
    N = 1
    with open("mount.txt") as myfile:
        head = [next(myfile) for x in range(N)]

    parsed_json = json.loads(head[0])
    new_width = 200
    new_height = 200
    parsed_json['width'] = new_width
    parsed_json['height'] = new_height

    first_row = True
    for line in fileinput.FileInput("mount.txt", inplace=1):
        if first_row:
            print(json.dumps(parsed_json))
            first_row = False
        else:
            print(line)


def function3():
    first_row = True
    for line in fileinput.FileInput("mount.txt", inplace=1):
        if first_row:
            parsed_json = json.loads(line)
            first_row = False
            line = line.replace(line, json.dumps(parsed_json))
            print(line)


def function4():
    first = "new string"
    sh.sed("-i", "1s/.*/" + first + "/", "mount.txt")


def replace_first_line(src_filename, target_filename, replacement_line):
    f = open(src_filename)
    first_line, remainder = f.readline(), f.read()
    t = open(target_filename, "w")
    t.write(replacement_line + "\n")
    t.write(remainder)
    t.close()


def replace_first_line1(src_filename, target_filename):
    f = open(src_filename)
    first_line, remainder = f.readline(), f.read()
    parsed_json = json.loads(first_line)
    new_width = 200
    new_height = 200
    parsed_json['patch_w'] = new_width
    parsed_json['patch_h'] = new_height
    t = open(target_filename, "w")
    replacement_line = json.dumps(parsed_json)
    t.write(replacement_line + "\n")
    t.write(remainder)
    t.close()


replace_first_line1("source.csv", "target.csv")
