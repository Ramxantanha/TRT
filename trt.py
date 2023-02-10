import os,platform
os.system('git pull')
 
trt=platform.architecture()[0]
if trt=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif trt=="64bit":
    __import__("trt1")
