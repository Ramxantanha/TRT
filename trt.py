import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{red}[•] Join Over Facebook Group {white}')
    os.system('xdg-open https://facebook.com/groups/412423917720633//')
    time.sleep(0.05)
    import trt2
elif bit=='32bit':
    import trt32
else:
    print(f'{green}[×] Sorry System Not Support{white}')
