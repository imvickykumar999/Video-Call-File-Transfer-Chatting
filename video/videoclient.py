
def vclient(host = '192.168.1.102'):
    import cv2
    import socket
    import pickle
    import struct

    cap=cv2.VideoCapture(0)
    # host = input('\nEnter Host IP : ')

    clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientsocket.connect((host,5000))

    while cv2.waitKey(33) != 27:
        ret,frame=cap.read()
        c_data = pickle.dumps(frame)

        # print(len(c_data))
        message_size = struct.pack("L", len(c_data))
        clientsocket.sendall(message_size + c_data)

    cap.release()
    cv2.destroyAllWindows()

host = input('\nEnter Host IP : ')
vclient(host)
