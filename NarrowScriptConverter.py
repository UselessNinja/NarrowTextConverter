#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################
# Script made by Daalehner for Hiraeth and Fire Emblem Universe #
#  The code is free to use and modify as long as you credit me  #
#################################################################

import os, sys, re

def printerr(str, code):
    print(str)
    exit(code)

def dictconv():
    dc = {
    "a": "[0x81]", "b": "[0x82]", "c": "[0x83]", "d": "[0x84]", "e": "[0x85]",
    "f": "[0x86]", "g": "[0x87]", "h": "[0x88]", "j": "[0x89]", "k": "[0x8A]",
    "n": "[0x8B]", "o": "[0x8C]", "p": "[0x8D]", "q": "[0x8E]", "r": "[0x8F]",
    "s": "[0x90]", "t": "[0x95]", "u": "[0x96]", "v": "[0x97]", "x": "[0x98]",
    "y": "[0x99]", "z": "[0x9A]", "A": "[0x9B]", "B": "[0x9C]", "C": "[0x9D]",
    "D": "[0x9E]", "E": "[0x9F]", "F": "[0xA0]", "G": "[0xA2]", "H": "[0xA3]",
    "J": "[0xA4]", "K": "[0xA5]", "L": "[0xA6]", "O": "[0xA7]", "P": "[0xA8]",
    "Q": "[0xA9]", "R": "[0xAC]", "S": "[0xAD]", "U": "[0xAE]", "V": "[0xAF]",
    "X": "[0xB0]", "Y": "[0xB1]", "Z": "[0x82]",
    "{": "[0x7B]", "|": "[0x7C]", "}": "[0x7D]",
    '\x91': "[0x91]", '\x92': "[0x92]", '\x93': "[0x93]", '\x94': "[0x94]",
    '\x81': "[0x81]", '\x82': "[0x82]", '\x83': "[0x83]", '\x84': "[0x84]", '\x85': "[0x85]", 
    '\x86': "[0x86]", '\x87': "[0x87]", '\x88': "[0x88]", '\x89': "[0x89]", '\x8A': "[0x8A]",
    '\x8B': "[0x8B]", '\x8C': "[0x8C]", '\x8D': "[0x8D]", '\x8E': "[0x8E]", '\x8E': "[0x8F]",
    '\x90': "[0x90]", '\x95': "[0x95]", '\x96': "[0x96]", '\x97': "[0x97]", '\x98': "[0x98]",
    '\x99': "[0x99]", '\x9A': "[0x9A]", '\x9B': "[0x9B]", '\x9C': "[0x9C]", '\x9D': "[0x9D]",
    '\x9E': "[0x9E]", '\x9F': "[0x9F]", '\xA0': "[0xA0]", '\xA2': "[0xA2]", '\xA3': "[0xA3]",
    '\xA4': "[0xA4]", '\xA5': "[0xA5]", '\xA6': "[0xA6]", '\xA7': "[0xA7]", '\xA8': "[0xA8]",
    '\xA9': "[0xA9]", '\xAC': "[0xAC]", '\xAD': "[0xAD]", '\xAE': "[0xAE]", '\xAF': "[0xAF]",
    '\xB0': "[0xB0]", '\xB1': "[0xB1]", '\xB2': "[0x82]",
    '\x7B': "[0x7B]", '\x7C': "[0x7C]", '\x7D': "[0x7D]", '\x7F': "[0x7F]",
    '\xB3': "[0xB3]", '\xB4': "[0xB4]", '\xB5': "[0xB5]", '\xB6': "[0xB6]",
    '\xB7': "[0xB7]", '\xB8': "[0xB8]", '\xB9': "[0xB9]", '\xBA': "[0xBA]"
    }
    return dc

def specommands(command):
    dictcommands = {
        #They only work while writing in serif. The only exeption is [ALPHA] which has a menu font variant. 
        #(Menu font is used in Character Names, Item Names, Class Names, etc...)
        "[CV]": "[0x7B]", "[AR]": "[0x7C]", "[PG]": "[0x7D]", "[DR]": "[0x7F]", #CV: Mounted, AR: Armored, PG: Flying, DR: Dragon
        "[SW]": "[0xB3]", "[LC]": "[0xB4]", "[AX]": "[0xB5]", "[BW]": "[0xB6]", #SW: Sword, LC: Lance, AX: Axe, BW: Bow
        "[LT]": "[0xB7]", "[AN]": "[0xB8]", "[DK]": "[0xB9]", "[SF]": "[0xBA]", #LT: Light, AN: Anima, DK: Dark, SF: Staff
        "[ALPHA]": "[0xAA]", "[INF]": "[0x7B][0x7C]", "[WYV]": "[0x7D][0x7F]" #ALPHA: α, INF: Infantry (Mounted + Armored), WYV: Wyvern (Flying + Dragon)
    }
    return dictcommands.get(command)

def getscript():
    fp = []
    for file in os.listdir("."):
        if file.endswith(".txt"):
            fp.append(os.path.join(".", file))
    if fp.__len__() == 0:
        printerr("No Script Found", 84)
    if fp.__len__() > 1:
        printerr("Please put only one script in the folder", 84)
    return fp

def narrowscriptconverter(fp):
    f = open(fp[0], "r", encoding="utf8")
    newfilec = ""
    trans = str.maketrans(dictconv())
    do_translate = False

    for line in f:
        if (re.search(r'^(\[\w+\])$', line)):
            try:
                id_ = int("0x" + re.sub(r'[\[\]]', '', line.strip()), 16)
                if (id_ == 0xA):
                    newfilec += line
                else:
                    newfilec += line
                    if (id_ >= 0x020E and id_ <= 0x04E4 or id_ >= 0x08D8 and id_ <= 0x08FB #Those Ranges are based on Hiraeth's script
                    or id_ >= 0x0903 and id_ <= 0x0DFF or id_ >= 0x0E20 and id_ <= 0x0EFD #but they are compatible with Vanilla and
                    or id_ >= 0x0F0A and id_ <= 0x0F13 or id_ >= 0x0F23 and id_ <= 0x0F74 #Skill System versions.
                    or id_ >= 0x1001 or id_ == 0x0F1B):
                        do_translate = True
                    else:
                        do_translate = False
            except ValueError:
                newfilec += line
        elif do_translate == True:
            translatedline = ""
            stringsplit = re.split(r'(\[\w+\])', line)
            for split in stringsplit:
                if re.search(r'^(\[\w+\])$', split):
                    if specommands(split) != None:
                        translatedline += specommands(split)
                    else:
                        translatedline += split
                else:
                    translatedline += ''.join(split.translate(trans))
            newfilec += translatedline
        else:
            newfilec += line
    f.close()
    f = open(fp[0], "w", encoding="utf8")
    f.write(newfilec)
    print("Conversion done")
    exit (0)

def main():
    fp = getscript()
    narrowscriptconverter(fp)
    return

if __name__ == '__main__':
    main()