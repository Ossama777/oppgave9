#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:36:07 2021

@author: ossamakhalil
"""



ordliste = dict()
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for i,linje in enumerate(fila):
        ordene = linje.split()
        for ordet in ordene:
            ordet = ordet.lower()
            if ordet not in ordliste:
                ordliste[ordet] = i
            
    for ordet in ordliste:
        print(f"Ordet {ordet} forekommer på linje {ordliste[ordet]}")
        

