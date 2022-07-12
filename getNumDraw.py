#!/bin/python3

import math
import os
import random
import re
import sys
import time

import requests
import json
#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#



def getTotalGoals(year):
    st = time.time()
    home_s = []

    for s in range(0, 11):
        url_score = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={s}&team2goals={s}'
        res = requests.request("GET", url_score)
        multiple = res.json()["total"]
        home_s.append(multiple)
    et = time.time()
    return sum(home_s), et - st


print(getTotalGoals(2011))
print(getTotalGoals(2012))
print(getTotalGoals(2010))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     team = input()
#
#     year = int(input().strip())
#
#     result = getTotalGoals(team, year)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()