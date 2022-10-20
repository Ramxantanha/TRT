Jimport os,time,platform
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
    import TRT
elif bit=='32bit':
    print(f'{green}[•] subscribe krne Walo Ko Approvel Meli Ga {white}')
    os.system('xdg-open https://youtube.com/channel/UCm5PL8Gdg0i0BhR0HVOC5Pg/')
    import TRT32
else:
    print(f'{green}[×] Sorry System Not Support{white}')
