import cv2, socket, pickle, os,threading
def sender():
    s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65536)
    serverip="192.168.43.229" #Server IP
    serverport=3000 
    url = "http://192.168.43.1:8080/video"         #Server Port
    cap = cv2.VideoCapture(url)
    while True:
        ret,photo = cap.read()       
        photo = photo[300:800 , 700:1300]     
        ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY),80])
        msg = pickle.dumps(buffer)
        s.sendto(msg,(serverip , serverport))
        cv2.namedWindow('sender1', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('sender1', 250,250)
        cv2.imshow('sender1', photo)
        if cv2.waitKey(10) == 13:
            cap.release()
            break    
            
    cv2.destroyAllWindows()

def receiver():
    sr=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    ip="192.168.43.229"      #Host IP
    port=3050               #Host Port
    sr.bind((ip,port))
    
    while True:
        x=sr.recvfrom(65536)
        if x == 0:
            pass
        else:
            # print(x)
            clientip = x[1][0]
            data=x[0]
            # print(data)
            data=pickle.loads(data)
            # print(type(data))
            data = cv2.imdecode(data, cv2.IMREAD_COLOR)
            cv2.imshow('receiver1', data) 
            if cv2.waitKey(10) == 13:
                break
    cv2.destroyAllWindows()



t1 = threading.Thread(target=sender)
t2 = threading.Thread(target=receiver)
t1.start()
t2.start()