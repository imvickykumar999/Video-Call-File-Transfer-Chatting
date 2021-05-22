import os

try:
    os.mkdir('chat')
except Exception as e:
    print('error in mkdir chat')
    print(e)

try:
    os.mkdir('files')
except Exception as e:
    print('error in mkdir files')
    print(e)

# input()

# os.system('pip install requirements.txt')
