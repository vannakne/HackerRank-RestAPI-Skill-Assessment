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



def getTotalGoals(competition, year):
    st = time.time()
    score_h = []
    score_v = []
    p = 1
    url_winner = f'https://jsonmock.hackerrank.com/api/football_competitions?year={year}&name={competition}'
    get_winner = requests.request("GET", url_winner)
    team = get_winner.json()['data'][0]["winner"]
    url_home = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={p}&competition={competition}'
    get_page_h = requests.request("GET", url_home)
    total_p_h = get_page_h.json()["total_pages"]
    for p in range(1, total_p_h+1):
        url_home = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={p}&competition={competition}'
        res = requests.request("GET", url_home)
        data = res.json()['data']
        for score in data:
            score_h.append(int(score['team1goals']))
    for p in range(1, total_p_h+1):
        url_visit = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={p}&competition={competition}'
        res = requests.request("GET", url_visit)
        data = res.json()['data']
        for score in data:
            score_v.append(int(score['team2goals']))
    et = time.time()
    return sum(score_h) + sum(score_v), et - st


print(getTotalGoals("UEFA Champions League", 2011))
# print(getTotalGoals("Chelsea", 2014))
# print(getTotalGoals("Non Existing Clug", 2013))
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