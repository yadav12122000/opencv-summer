import cv2
import socket 
import pickle
import threading

def sender():
    s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65536)
    serverip="192.168.43.229" #Server IP
    serverport=3050
    #url = "http://192.168.43.1:8080/video"         #Server Port
    cap = cv2.VideoCapture(0)
    while True:
        ret,photo = cap.read()
        photo = photo[50:450 , 50:550]
        ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY),80])
        msg = pickle.dumps(buffer)
        s.sendto(msg,(serverip , serverport))
        cv2.namedWindow('sender2', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('sender2', 250,250)
        cv2.imshow('sender2', photo)
        if cv2.waitKey(10) == 13:
            cap.release()
            break

    cv2.destroyAllWindows()

def receiver():
    sr=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    ip="192.168.43.229"     
    port = 3000     
    sr.bind((ip,port))

    while True:
        x=sr.recvfrom(65536)
        if x == 0:
            pass
        else:
            # print(x)
            clientip = x[1][0]
            data=x[0]
            data=pickle.loads(data)
            data = cv2.imdecode(data, cv2.IMREAD_COLOR)
            cv2.imshow('receiver2', data)
            if cv2.waitKey(10) == 13:
                break
    cv2.destroyAllWindows()



t1 = threading.Thread(target=sender)
t2 = threading.Thread(target=receiver)
t1.start()
t2.start()
