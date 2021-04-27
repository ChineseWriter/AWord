#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Main.py
# @Time      :2021/4/24 13:45
# @Author    :Amundsen Severus Rubeus Bjaaland


import AWord
import requests


if __name__ == "__main__":
    Result = AWord.GetSentence()
    print(Result)
    print(len(Result))
    print(Result.Uuid)
    # print(requests.get("https://hitokoto.cn/", params={"uuid": Result.Uuid}).text)
