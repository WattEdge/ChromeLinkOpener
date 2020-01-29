#!/usr/bin/env python3

import sys
import os
import webbrowser
import subprocess
import time
from datetime import datetime

def main():
    filepath = "links.txt"
    max = 10
    tabsleep = 10
    fx = webbrowser.get("open -a /Applications/Google\ Chrome.app %s")
    startTime = datetime.now()

    with open(filepath) as fp:
       count = 0
       for line in fp:
           strippedline = line.strip()
           print(strippedline)
           fx.open_new_tab(strippedline)
           count = count+1
           if count == max:
               time.sleep(tabsleep)
               subprocess.call('killall Google\ Chrome',shell=True)
               time.sleep(2)
               count = 0
    time.sleep(tabsleep)
    subprocess.call('killall Google\ Chrome',shell=True)
    print("Script Finished!", datetime.now() - startTime)

if __name__ == '__main__':
   main()
