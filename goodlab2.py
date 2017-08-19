# -*- coding: UTF-8 -*-

from __future__ import print_function
import os, sys, re
import shutil


usbName = os.listdir("/media/pi/")[0]
print("Is '%s' your usb name?(y/n): " % usbName, end='')
reply = raw_input()
if reply != 'y':
    sys.exit()

fileList = os.listdir("/media/pi/" + usbName)

# Get all available file extensions
availableExts = []
for name in fileList:
    mo = re.search("\.(\w+)$", name)
    if mo != None:
        ext = mo.group(1).lower()
        if ext not in availableExts:
            availableExts.append(ext)

# Print available extension names
print("Available extension names:", end='')
for ext in availableExts:
    print(" " + ext, end='')

print("\nWhat type of files do you want copy? ", end='')
userExt = raw_input().lower()

if userExt not in availableExts:
    print("There is no any %s files." % userExt)
    sys.exit()

print('')
if not os.path.exists("./goodlab2-files"):
    os.makedirs("./goodlab2-files")

for fileName in fileList:
    mo = re.search("\.(\w+)$", fileName)
    if mo != None:
        fileExt = mo.group(1).lower()
        if fileExt == userExt:
            src = "/media/pi/" + usbName + "/" + fileName
            dst = "./goodlab2-files/" + fileName
            shutil.copy2(src, dst)
            print("Copy file from %s to %s..." % (src, dst))

print("\nSuccesfully copy all %s files to ./goodlab2-files/" % userExt)
