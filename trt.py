import os,platform
os.system('git pull')
 
trt=platform.architecture()[0]
if trt=="32bit":
    __import__("t")
elif trt=="64bit":
    __import__("trt1")
