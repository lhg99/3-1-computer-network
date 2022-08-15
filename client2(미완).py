from socket import *

name = '127.0.0.1'
port = 10000

client = socket(AF_INET, SOCK_STREAM)
client.connect((name, port))

while True:
    sentence1 = input('login ID: ')
    client.send(sentence1.encode())
    fix_sentence1 = client.recv(1024)
    if fix_sentence1 == 'exist id!':
        print(fix_sentence1.decode())
        sentence2 = input('pwd: ')
        client.send(sentence2.encode())
        fix_sentence2 = client.recv(1024)
        print(fix_sentence2.decode())
    else:
        print(fix_sentence1.decode())
        sentence3 = input('register id: ')
        client.send(sentence3.encode())
        sentence4 = input('register pwd: ')
        client.send(sentence4.encode())
        
client.close()
