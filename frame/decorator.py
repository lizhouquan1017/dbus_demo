#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def checkword(func, target=True):
    def wrapper(*args, **kwargs):
        flag = func(*args, **kwargs)
        if flag == target:
            assert True
        else:
            assert False

    return wrapper
