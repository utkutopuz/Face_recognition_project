import cv2
import imageio

# based on opencv
face_cascade= cv2.CascadeClassifier('haarcascade-frontalface-default.xml')  #face detect

eye_cascade= cv2.CascadeClassifier('haarcascade-eye.xml')  # eye detect

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #images have been turned into black and white format
    faces= face_cascade.detectMultiScale(gray, 1.3, 5) 
    for(x, y, w, h) in faces: #tuple with 4 elements, x and y the coordinates , w and h are for the length of the frame
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2) #frame=colors of the picture , (x+w,y+h) coordinates of the right-hand side , Rgb (255=red) , 2 pixel thickness
        gray_face = gray[y:y+h, x:x+w]  # frame rectangle as a parameter
        color_face = frame[y:y+h, x:x+w]
        eyes= eye_cascade.detectMultiScale(gray_face, 1.1, 3) #eye-recognition
        for(ex, ey , ew, eh) in eyes:
            cv2.rectangle(color_face, (ex,ey), (ex+ew,ey+eh), (0, 255, 0), 2) # RGB (0,255,0)= green , 2 Pixel thickness
    return frame

reader = imageio.get_reader('input.mp4') #read the input video
fps = reader.get_meta_data()['fps'] #demonstration of the scanned frame per second in videos 
writer = imageio.get_writer('outputt.mp4', fps=fps) #face detected video is being written
for i, frame in enumerate(reader):
    frame= detect(frame)
    writer.append_data(frame)  # demonstration of the scanned frame per second in videos 
    print(i)

writer.close()
