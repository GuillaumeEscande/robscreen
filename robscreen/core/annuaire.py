#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Annuaire():
    
    __instance = None
        
    PAGE_ACCEUIL = 100
    PAGE_HELP = 110
    PAGE_MODE = 200
    PAGE_PARAMS = 300
    PAGE_WIFI = 400
    
    @staticmethod
    def getInstance():
        if Annuaire.__instance is None :
            Annuaire.__instance = Annuaire()
        return Annuaire.__instance

    def __init__(self):
        self.__page_dict = dict()
        
        
    def addPage(self, identifier, page):
        self.__page_dict[identifier] = page
        
    def getPage(self, identifier):
        return self.__page_dict[identifier]
