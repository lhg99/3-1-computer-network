from socket import *

login_info = ['a1234', 'b2345', 'c3456', 'd4567', 0, 0, 0, 0, 0, 0,
              ['qwer', 'asdf', 'zxcv', 0, 0, 0, 0, 0, 0]]

s_name = '127.0.0.1'
s_port = 10000
server = socket(AF_INET, SOCK_STREAM)
server.bind((s_name, s_port))
server.listen(1)

print("Server is ready to receive")
while True:
    connection, addr = server.accept()
    
    rec_sentence = connection.recv(1024).decode()
    for i in login_info:
            if rec_sentence == i:
                sentence1 = 'exist id!'
                connection.send(sentence1.encode())
                rec2_sentence = connection.recv(1024).decode()
                for j in login_info:
                    if rec2_sentence == i:
                        sentence3 = 'login success'
                        connection.send(sentence3.encode())
                    else:
                        sentence4 = 'login failed'
                        connection.send(sentence4.encode())
            else:
                sentence2 = 'login failed, adding info needed'
                connection.send(sentence2.encode())
                rec3_sentence = connection.recv(1024).decode()
                for i in range (1,10):
                    if login_info[i][i] == 0:
                        login_info[i] = rec3_sentence
                rec4_sentence = connection.recv(1024).decode()
                for i in range (1,10):
                    if login_info[i] == rec3_sentence:
                        login_info[i][i] = rec4_sentence
                    
    if rec_sentence == 'quit':
        connection.close()

connection.close()
