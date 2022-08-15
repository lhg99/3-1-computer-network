from socket import *
name = '127.0.0.1'
port = 10000

client = socket(AF_INET, SOCK_STREAM)
client.connect((name, port))
sentence = input('input lower or capital sentence: ')
client.send(sentence.encode())
fix_sentence = client.recv(1024)
print("From server: ", fix_sentence.decode())
client.close()
