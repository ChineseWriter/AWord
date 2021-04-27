#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Require.py
# @Time      :2021/4/24 13:45
# @Author    :Amundsen Severus Rubeus Bjaaland


import copy


class URL(object):
    Chinese = "https://v1.hitokoto.cn/"
    International = "https://international.v1.hitokoto.cn/"


class SentenceMode(object):
    Animation = "a"
    Cartoon = "b"
    Game = "c"
    Literature = "d"
    Original = "e"
    FromInternet = "f"
    Other = "g"
    Movies = "h"
    Poem = "i"
    WangYiYun = "j"
    Philosophy = "k"
    Smart = "l"
    All = ""


class Sentence(object):
    def __init__(self, Id: int = 0, Uuid: str = "", Hitokoto: str = "", Type: str = "", From: str = "",
                 Author: str = "", Creator: str = "", CreatorId: int = 0, CommitFrom: str = "", CreateTime: float = 0.0,
                 Length: int = 0, Text: str = ""):
        assert isinstance(Id, int)
        assert isinstance(Uuid, str)
        assert isinstance(Hitokoto, str)
        assert isinstance(Type, str)
        assert isinstance(From, str)
        assert isinstance(Author, str)
        assert isinstance(Creator, str)
        assert isinstance(CreatorId, int)
        assert isinstance(CommitFrom, str)
        assert isinstance(CreateTime, float)
        assert isinstance(Length, int)
        assert isinstance(Text, str)
        self.__Id = Id
        self.__Uuid = Uuid
        self.__Hitokoto = Hitokoto
        self.__Type = Type
        self.__From = From
        self.__Author = Author
        self.__Creator = Creator
        self.__CreatorId = CreatorId
        self.__CommitFrom = CommitFrom
        self.__CreateTime = CreateTime
        self.__Length = Length
        self.__Text = Text

    def __len__(self):
        return copy.deepcopy(self.__Length)

    def __str__(self):
        return copy.deepcopy(self.__Text)

    @property
    def Id(self):
        return copy.deepcopy(self.__Id)

    @property
    def Uuid(self):
        return copy.deepcopy(self.__Uuid)

    @property
    def Hitokoto(self):
        return copy.deepcopy(self.__Hitokoto)

    @property
    def Type(self):
        return copy.deepcopy(self.__Type)

    @property
    def From(self):
        return copy.deepcopy(self.__From)

    @property
    def Author(self):
        return copy.deepcopy(self.__Author)

    @property
    def Creator(self):
        return copy.deepcopy(self.__Creator)

    @property
    def CreatorId(self):
        return copy.deepcopy(self.__CreatorId)

    @property
    def CommitFrom(self):
        return copy.deepcopy(self.__CommitFrom)

    @property
    def CreateTime(self):
        return copy.deepcopy(self.__CreateTime)

    @property
    def Length(self):
        return copy.deepcopy(self.__Length)

    @property
    def Text(self):
        return copy.deepcopy(self.__Text)

    @Id.setter
    def Id(self, ObjectId: int = 0):
        assert isinstance(ObjectId, int)
        self.__Id = ObjectId

    @Uuid.setter
    def Uuid(self, ObjectUuid: str = ""):
        assert isinstance(ObjectUuid, str)
        self.__Uuid = ObjectUuid

    @Hitokoto.setter
    def Hitokoto(self, ObjectHitokoto: str = ""):
        assert isinstance(ObjectHitokoto, str)
        self.__Hitokoto = ObjectHitokoto

    @Type.setter
    def Type(self, ObjectType: str = ""):
        assert isinstance(ObjectType, str)
        self.__Type = ObjectType

    @From.setter
    def From(self, ObjectFrom: str = ""):
        assert isinstance(ObjectFrom, str)
        self.__From = ObjectFrom

    @Author.setter
    def Author(self, ObjectAuthor: str = ""):
        assert isinstance(ObjectAuthor, str)
        self.__Author = ObjectAuthor

    @Creator.setter
    def Creator(self, ObjectAuthor: str = ""):
        assert isinstance(ObjectAuthor, str)
        self.__Author = ObjectAuthor

    @CreatorId.setter
    def CreatorId(self, ObjectCreatorId: int = 0):
        assert isinstance(ObjectCreatorId, int)
        self.__CreatorId = ObjectCreatorId

    @CreateTime.setter
    def CreateTime(self, ObjectCreateTime: float = 0.0):
        assert isinstance(ObjectCreateTime, float)
        self.__CreateTime = ObjectCreateTime

    @CommitFrom.setter
    def CommitFrom(self, ObjectCommitFrom: str = ""):
        assert isinstance(ObjectCommitFrom, str)
        self.__CommitFrom = ObjectCommitFrom

    @Length.setter
    def Length(self, ObjectLength: int = 0):
        assert isinstance(ObjectLength, int)
        self.__Length = ObjectLength

    @Text.setter
    def Text(self, ObjectText: str = ""):
        assert isinstance(ObjectText, str)
        self.__Text = ObjectText
