#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2024/03/07 16:17:27
@Author  :   ChenHao
@Description  :   
@Contact :   jerrychen1990@gmail.com
'''
import os
from typing import List
import requests
from requests.auth import HTTPBasicAuth
auth=HTTPBasicAuth('zhipu','zhipu')
from loguru import logger


class XClient:
    def __init__(self, host:str, port=8001):
        self.host=host
        self.port=port

    def call_service(self, path:str,method='POST', **kwargs)->dict:
        url = f" http://{self.host}:{self.port}/{path}"
        if method == "POST":
            resp = requests.post(url=url,  auth=auth, **kwargs)
        else:
            resp = requests.get(url=url, auth=auth, **kwargs, )
        logger.debug(f"request to {url} with {method=}, {kwargs}")    
        
        resp.raise_for_status()
        resp = resp.json()
        code = resp["code"]
        msg = resp["msg"]
        resp_data = resp["data"]
        logger.debug(f"get resp:{code=}, {msg=}, {resp_data=}")
        return resp_data
                

    def health(self):
        return self.call_service(path="health", method="GET")
    
    def list_kb(self):
        return self.call_service(path="kb/list", method="GET")
    
    def get_kb(self, kb_name:str):
        return self.call_service(path=f"kb", params=dict(kb_name=kb_name), method="GET")
    
    def create_kb(self, kb_name:str, description: str=None,vecstore_config:dict=dict(vs_cls='XFAISS'), embedding_config:dict=dict(model_cls="ZhipuEmbedding", batch_size=16, norm=True)):
        data = dict(kb_name=kb_name, vecstore_config=vecstore_config, embedding_config=embedding_config)
        data = dict(kb_name=kb_name, description=description)
        json_data = dict(vecstore_config=vecstore_config, embedding_config=embedding_config)
        return self.call_service(path="kb/create", data=data, json=json_data)
    
    
    def delete_kb(self, kb_name:str):
        data = dict(kb_name=kb_name)
        return self.call_service(path="kb/delete", data=data)
    
    
    def build_index(self, kb_name:str):
        data = dict(kb_name=kb_name)
        return self.call_service(path="kb/build_index", data=data)
    
    def list_kb_files(self, kb_name:str):
        data = dict(kb_name=kb_name)
        return self.call_service(path="kb_file/list", data=data, method="GET")

    def create_kb_file(self, kb_name:str, file_path:str):
        file_name = os.path.basename(file_path)
        with open(file_path, "r") as f:
            files = {'file': (file_path, f)}
            data = dict(kb_name=kb_name, file_name=file_name)
            return self.call_service(path="kb_file/create", data=data, files=files)
        
    def delete_kb_file(self, kb_name:str, file_name:str):
        data = dict(kb_name=kb_name, file_name=file_name)
        return self.call_service(path="kb_file/delete", data=data)
    
    
    def get_kb_file_chunks(self,kb_name:str, file_name:str):
        data = dict(kb_name=kb_name, file_name=file_name)
        return self.call_service(path="kb_file/chunks", data=data, method="GET")
    
    def cut_kb_file(self,
                    kb_name: str,
             file_name: str,
             splitter_cls:str="BaseSplitter",
             splitter: str = "\n",
             max_len: int = 200,
             min_len:int =  10,
             parse_table: bool = False):
        data = dict(kb_name=kb_name, file_name=file_name, splitter_cls=splitter_cls, splitter=splitter, max_len=max_len, min_len=min_len, parse_table=parse_table)
        return self.call_service(path="kb_file/cut", data=data)
    
        

        
    def search_kb(self,
                  kb_name: str ,
                          query: str,
                          file_names:List[str]=None,
                          top_k: int =3,
                          score_threshold:float=0.0,
                          pre_content_len: int =0,
                          next_content_len: int =0
                          ):
        data = dict(kb_name=kb_name, query=query, file_names=file_names, top_k=top_k, score_threshold=score_threshold, pre_content_len=pre_content_len, next_content_len=next_content_len)
        return self.call_service(path="kb/search", data=data)
        


        
        
                
        

        

    
