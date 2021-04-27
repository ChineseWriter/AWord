#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :WebTools.py
# @Time      :2021/4/24 14:15
# @Author    :Amundsen Severus Rubeus Bjaaland


import AWord

import requests


def GetSentence(URL: str = AWord.URL.Chinese, SentenceMode: str = AWord.SentenceMode.All, MinLength: int = 0,
                MaxLength: int = 30):
    Params = CreateParams(SentenceMode, MinLength, MaxLength)
    Response = requests.get(URL, params=Params).json()
    OneSentence = AWord.Sentence()
    OneSentence.Id = Response["id"]
    OneSentence.Uuid = Response["uuid"]
    OneSentence.Hitokoto = Response["hitokoto"]
    OneSentence.Text = Response["hitokoto"]
    OneSentence.Type = Response["type"]
    OneSentence.From = Response["from"]
    OneSentence.Creator = Response["creator"]
    OneSentence.CreatorId = Response["creator_uid"]
    OneSentence.CommitFrom = Response["commit_from"]
    OneSentence.CreateTime = float(Response["created_at"])
    OneSentence.Length = Response["length"]
    return OneSentence


def CreateParams(SentenceMode: str = AWord.SentenceMode.All, MinLength: int = 0, MaxLength: int = 30) -> dict:
    Params = dict()
    if SentenceMode == AWord.SentenceMode.All:
        pass
    else:
        Params["c"] = SentenceMode
    Params["charset"] = "utf-8"
    Params["encode"] = "json"
    Params["min_length"] = MinLength
    Params["max_length"] = MaxLength
    return Params
