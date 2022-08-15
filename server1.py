from socket import *
s_name = '127.0.0.1'
s_port = 10000
server = socket(AF_INET, SOCK_STREAM)
server.bind((s_name, s_port))
server.listen(1)
print("Server is ready to receive")
while True:
    connection, addr = server.accept()
    
    sentence = connection.recv(1024).decode()
    if sentence.isupper() == False:
        cap_sentence = sentence.upper()
        connection.send(cap_sentence.encode())
    else:
        low_sentence = sentence.lower()    
        connection.send(low_sentence.encode())
    connection.close()
