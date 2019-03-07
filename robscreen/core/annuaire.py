#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Annuaire():
    
    __instance = None
        
    PAGE_HOME = 100
    PAGE_HOMES_START = 110

    PAGE_MODE = 200
    PAGE_MODES_DEMO = 210
    PAGE_MODES_EXIT = 299

    PAGE_PARAM = 300
    
    PAGE_WIFI = 400
    PAGE_WIFIS_MAISON = 410
    PAGE_WIFIS_HOTSPOT = 420
    PAGE_WIFIS_OFF = 430
    PAGE_WIFIS_EXIT = 499

    PAGE_DEFAULT = PAGE_HOME
    
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
