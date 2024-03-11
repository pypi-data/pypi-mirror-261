#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2023/12/11 14:28:24
@Author  :   ChenHao
@Contact :   jerrychen1990@gmail.com
'''

def format_prompt(template: str, **kwargs):
    for k, v in kwargs.items():
        template = template.replace("{k}", str(v))
    return template
