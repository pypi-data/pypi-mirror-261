#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2024/03/11 16:05:05
@Author  :   ChenHao
@Description  :   离线任务class
@Contact :   jerrychen1990@gmail.com
'''

from random import random
import sqlite3
from enum import Enum
from time import sleep
from typing import Callable
import uuid
from loguru import logger
from pydantic import BaseModel, Field
from snippets import jdumps,jloads

from xagents.config import DB_DIR

db_file = f"{DB_DIR}/job.db"


# logger.add(sys.stdout, level="DEBUG")
class JobStatus(str, Enum):
    PENDING="PENDING"
    RUNNING="RUNNING"
    SUCCESS="SUCCESS"
    FAILED="FAILED"
    

class JobInfo(BaseModel):
    job_id:str=Field(default=str(uuid.uuid4()), description="任务ID")
    status:JobStatus=Field(default=JobStatus.PENDING, description="任务状态")
    resp:dict=Field(default={}, description="任务结果")
    func_name:str=Field(description="函数名称")
    

class Job:
    def __init__(self, func:Callable, job_id:str, status:JobStatus,resp:dict):
        self.job_id:str = job_id
        self.status:JobStatus = status
        self.func=func
        self.resp=resp
        self.save()
    
    @classmethod
    def create_job(cls, func:Callable):
        job_info = JobInfo(func_name=func.__name__)
        job = Job(func=func, **job_info.model_dump(exclude={"func_name"}))
        return job
        
    def run(self, *args, **kwargs):
        logger.info(f"{self.job_id} start running")
        self.status = JobStatus.RUNNING
        self.save()
        
        try:
            self.resp = self.func(*args, **kwargs)
            self.status=JobStatus.SUCCESS
        except Exception as e:
            logger.error(f"Job {self.job_id} failed with error {e}")
            self.resp = e
            self.status=JobStatus.FAILED
        self.save()
        logger.info(f"{self.job_id} finished")
        
    def save(self):
        sql = f"""
        insert into JOB(ID, STATUS, RESP, FUNC_NAME)
        values('{self.job_id}', '{self.status}', '{jdumps(self.resp)}', '{self.func.__name__}')
        on CONFLICT(ID) do UPDATE SET
        ID='{self.job_id}', STATUS='{self.status}', RESP='{jdumps(self.resp)}'
        """
        # logger.info(f"{sql=}")
        logger.debug(f"updating job with sql:{sql}")
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute(sql)
        con.commit()

    
        
def get_job_info(job_id:str)->JobInfo:
    sql = f"select ID,STATUS, RESP, FUNC_NAME from JOB where ID='{job_id}'"
    logger.debug(f"executing sql:{sql}")
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    jobs = cur.execute(sql).fetchall()
    if not jobs:
        logger.warning(f"no job found with id {job_id}")
    else:
        item = jobs[0]
        # item[-2]=jloads(item[-2])
        # logger.info(item)
        kwargs = dict(zip(["job_id", "status", "resp", "func_name"], item))
        kwargs["resp"]=jloads(kwargs["resp"])
        job_info=JobInfo(**kwargs)

        return job_info
    
        
if __name__ == "__main__":
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    # cur.execute("drop table JOB")
    
    
#     cur.execute("""
# CREATE TABLE JOB (
#     ID VARCHAR(255) PRIMARY KEY,
#     STATUS VARCHAR(255) NOT NULL,
#     RESP VARCHAR(1024),
#     FUNC_NAME VARCHAR(1024)
# )""")
                
    
    import time
    from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED,FIRST_COMPLETED, as_completed
    
    
    
    
    def func(a):
        wt = random.randrange(1, 5)
        # print(wt)
        sleep(wt)
        return dict(rs=a**2)
    
    
    
    
    # lists=[4,5,2,3]
    lists = [1]
    jobs = [Job(func) for i in lists]

    # 创建一个最大容纳数量为2的线程池
    pool= ThreadPoolExecutor(max_workers=1)

    # 通过submit提交执行的函数到线程池中
    all_task=[pool.submit(j.run, i) for j,i in zip(jobs,lists)]


    # # # 通过result来获取返回值
    result=[i.result() for i in all_task]
    print(f"result:{result}")


    print("----complete-----")
    # # 线程池关闭
    pool.shutdown()
        
    
    
    
    
    
