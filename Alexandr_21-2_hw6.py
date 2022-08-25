import re

file1 = open('names.txt', 'w', encoding='UTF-8')
file2 = open('mails.txt', 'w', encoding='UTF-8')
file3 = open('files.txt', 'w', encoding='UTF-8')
file4 = open('colors.txt', 'w', encoding='UTF-8')
with open('MOCK_DATA.txt', 'r', encoding='UTF-8') as m_d:
    content = m_d.read()

def names():
    names_list = re.findall(r'\b[A-Z][a-zA-Z\'\-\. ]+[\s]+[a-zA-Z\'\-\. ]+\b', content)

    print(f'Amount names: {len(names_list)}')


    for i in names_list:
        print(i)
        file1.write(f'\n{i}')






def mails():
    mails_list = re.findall(r'\w+@[a-z0-9._-]+\.[a-z]{2,}', content)
    print(f'Amount emails: {len(mails_list)}')


    for i in mails_list:
        print(i)
        file2.write(f'\n{i}')




def files():
    files_list = re.findall(r'\s(?:[A-Z]|[a-zA-Z])+\.\w{2,}', content)
    print(f'Amount files: {len(files_list)}')
    for i in files_list:
        print(i)
        file3.write(f'\n{i}')

def colors():
    colors_list = re.findall(r'#[a-z0-9]+', content)
    print(f'Amount colors: {len(colors_list)}')
    for i in colors_list:
        print(i)
        file4.write(f'\n{i}')

def start():
    print('Choose number from 1-5\n'
          '1 - Names\n'
          '2 - Emails\n'
          '3 - Files\n'
          '4 - Colors\n'
          '5 - Exit')

    while True:

        a = int(input('Number: '))
        if a == 1:
            names()
        elif a == 2:
            mails()
        elif a == 3:
            files()
        elif a == 4:
            colors()
        elif a == 5:
            print('Program completed')
            break
        else:
            print('Only numbers from 1 to 5')
start()

