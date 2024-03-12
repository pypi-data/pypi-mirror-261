#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2023/12/12 11:34:29
@Author  :   ChenHao
@Contact :   jerrychen1990@gmail.com
'''

from typing import List
from loguru import logger
from xagents.config import *
from xagents.kb.core import KnowledgeBase, KnowledgeBaseFile, get_config_path
from xagents.kb.loader import _EXT2LOADER
from xagents.kb.vector_store import list_vecstores as lv
from xagents.kb.splitter import _SPLITTERS
from langchain.vectorstores.utils import DistanceStrategy



def list_vecstores():
    return lv()


def list_distance_strategy():
    return [e.name for e in DistanceStrategy]


def list_knowledge_base_names()->List[str]:
    """列出所有知识库名称

    Returns:
        str: 知识库名称列表
    """
    kb_names = os.listdir(KNOWLEDGE_BASE_DIR)
    return kb_names

def list_knowledge_bases()->List[KnowledgeBase]:
    """列出所有知识库
    Returns:
        List[KnowledgeBase]: 知识库列表
    """
    
    kb_names = os.listdir(KNOWLEDGE_BASE_DIR)
    kbs = []
    for name in kb_names:
        config_path = get_config_path(name)
        kb = KnowledgeBase.from_config(config=config_path)
        kbs.append(kb)
    return kbs    

    
    





def get_knowledge_base(name: str) -> KnowledgeBase:
    """
    根据名称获取知识库实例
    """
    logger.debug(f"get knowledge base with name:{name}")
    kb_names = list_knowledge_base_names()
    if name not in kb_names:
        msg =  f"kb_name {name} not in {kb_names}"
        logger.warning(msg)
        raise ValueError(msg)
    
    config_path = get_config_path(name)
    kb = KnowledgeBase.from_config(config=config_path)
    return kb




def list_kb_files(kb_name: str) -> List[KnowledgeBaseFile]:
    kb = get_knowledge_base(kb_name)
    kb_files = kb.list_files()
    return kb_files

def get_knowledge_base_file(kb_name: str, file_name: str)->KnowledgeBaseFile:
    kb_files = list_kb_files(kb_name)
    kb_file_dict = {f.file_name: f for f in kb_files}
    assert file_name in kb_file_dict, f"{file_name} not in {kb_files}"
    return kb_file_dict[file_name]


def list_valid_exts():
    return list(_EXT2LOADER.keys())


def list_splitters() -> List[str]:
    return list(e.__name__ for e in _SPLITTERS)


def create_knowledge_base(name: str, desc: str,
                          embedding_config: dict, vecstore_config: dict,
                          distance_strategy: DistanceStrategy = DistanceStrategy.MAX_INNER_PRODUCT
                          ):
    """
    创建知识库
    """
    logger.info(f"Creating knowledge base {name}...")
    kb_names = list_knowledge_base_names()
    if name in kb_names:
        msg = f"Knowledge base {name} already exists, can not create!"
        logger.warning(msg)
        raise ValueError(msg)
    kb = KnowledgeBase(name=name, embedding_config=embedding_config,
                       description=desc, vecstore_config=vecstore_config, distance_strategy=distance_strategy)
    kb.save()
    return kb




if __name__ == "__main__":
    print(list_knowledge_base_names())
    print(list_vecstores())
    print(list_distance_strategy())
