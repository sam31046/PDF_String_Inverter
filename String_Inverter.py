#!/usr/bin/env
# -*- coding: UTF-8 -*-
__author__ = "Jhong,Dong-You"


def String_Inverter(string):
    new_string = ""
    for character in string:
        new_string = character + new_string
    return new_string


if __name__ == '__main__':
    print(String_Inverter(input("Please enter a string you want to invert:\n")))
