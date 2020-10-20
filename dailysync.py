# -*- coding: utf-8 -*-
r"""
requirement inside qwiklabs is to call multiprocessing to call rsync

server is like
python 3.5.x
debian

structure is nested directories which may or may not contain files like .txt, .jpg ...

tool must call rsync linux tool to backup files via delta method

a\
a\b\
a\b\x.txt

##/root/original # key input
##/root//backup # key output 


# =============================================================================
student-03-4b4fdfc48f17@linux-instance:~/scripts$ cat dailysync.py
#!/usr/bin/env python
import subprocess
src = "/data/prod/"
dest = "/data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])

student-03-4b4fdfc48f17@linux-instance:~/scripts$ cat multisync.py
#!/usr/bin/env python3
from multiprocessing import Pool
def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
# =============================================================================
"""
#!/usr/bin/ python3

import subprocess
import os
#from multiprocessing import Process, Pool
import multiprocessing
from concurrent import futures

#src = "/mnt/c/users/emmam/documents/git_practice/backup"
#dest = "/mnt/c/users/emmam/documents/git_practice/backup_backup"

fp_l = list()
jobs = list()
#f_delim=r"\"

def subproc_wf():
    """
    subprocess wrapper function
    
    pool?
    concurrent.futures # executor=futures.ThreadPoolExecutor()
    
    """

def fp_name_fixer(source):
    """
    name fixer for replacing src to dest
    a\
    a\b\
    """
    d=source+"_backup"
    return(d)

def subproc_rsync(s,d):
    """
    calls subprocess to rsync in linux
    """
    #return(subprocess.call(["rsync", "-arv", s, d]))
    return(print(" ".join(["rsync", "-arv", s, d])))
    
def error_handler(e):
    print("!!!FAIL!!!")
    _wrns ="!!!e: {}\ntype(e):{}\nInside: {}!!!".format(e,type(e),__name__)
    #log.error
    #"e: {}\ntype(e):{}\nInside: {}").format(e,type(e),__name__)"
    return((print(_wrns),_wrns))

#error_handler(AssertionError("fail"))

    
def try_make_dir(dest1):
    if not os.path.exists(dest1):
        print("creating dir '{}'".format(dest1))
        try:
            os.mkdir(dest1)
            return(0)
        except Exception as e:
            error_handler(e)
        return(9)
    else:
        print("{} exists".format(dest1))
        return(0)
        
#try_make_dir(r"hellooO?!?!?>?")

def mkdir_walk(basedir):
    try:
        # =============================================================================
        # top level backup directory creation
        # =============================================================================
        os.chdir(basedir)
        top_dest = fp_name_fixer(basedir)
        print("copying to {}".format(top_dest))
        try_make_dir(top_dest)
        print(top_dest)
#        basedir
#        top_dest
        #[(r,d,f) for r, d, f, in os.walk(os.getcwd())]
        # =============================================================================
        # begin walk
        # =============================================================================
        for _item in os.walk(basedir):
            root, dirs, files = _item[0], _item[1], _item[2]
            print("root is now {}".format(root))
            nested_dest = root.replace(basedir , top_dest)
            try_make_dir(nested_dest)
            for files_item in files:
                _file_source0, _file_dest0 = os.path.join(root, files_item), os.path.join(nested_dest, files_item)
                subproc_rsync(_file_source0, _file_dest0)
    except Exception as e:
        error_handler(e)
        
mkdir_walk(r"C:\Users\emmam\Documents\git_practice\backup")

if __name__ == "__main__":
    print("in main dailysync.py")
    executor=futures.ThreadPoolExecutor() # init executor
if 0:
    #####
    # Create directory if it does not exist
    #####
    if not os.path.exists(dest):
        print("creating dir '{}'".format(dest))
        try:
            os.mkdir(dest)
        except Exception as e:
            print("e: {}\ntype(e):{}\nInside: {}".format(e,type(e),__name__))
        for fn in files:
            print(fn)
            source_fp = os.path.join(root, fn)
            target_fp = fp_name_fixer(source_fp)
            print(target_dir)
            if not os.path.exists(target_dir):
                print("creating path: {}".format(target_dir))
                os.mkdir(target_dir[:-1])
            #fp_l.append((source_fp, target_fp))
            ##p = multiprocessing.Process(target=subprocess.call, args = ("rsync", "-arv", source_fp, target_fp))
            #executor.submit(subproc_rsync([source_fp, target_fp]))
            ##print(["rsync", "-arv", source_fp, target_fp])
            ##jobs.append(p)
            ##p.start()
print("done")
