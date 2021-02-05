import cv2
import os
def extractFrames(pathIn, pathOut):
    cap = cv2.VideoCapture(pathIn)
    count = 0
    laplist = []
    framelist = []
    countlist = []
    lapsum = 0
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray, cv2.CV_64F).var()
            tup = (count, fm, frame, ret)
            laplist.insert(count, tup)
            count += 1
        else:
            break
    for i in laplist:
        lapsum += i[1]
    lapavg = lapsum/frame_count
    for i in laplist:
        if(i[1]>120):
            print(i[1])
            print('Read %d frame: ' % i[0], i[3])
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.png".format(i[0])), i[2])
    cap.release()
    cv2.destroyAllWindows()

def extractFramesTen(pathIn, pathOut):
    fileName = pathIn [:-4]
    #opening the video
    cap = cv2.VideoCapture(pathIn)
    #frame counter
    count = 0
    #list that saves tupples with 4 attributes (count, laplacian val of the frame, frame, and boolean)
    laplist = []
    framelist = []
    countlist = []
    perfectlist = []
    #counts the best pictures if the laplacian value is higher then other frame
    perfectcount = 0
    #counts the total laplacian ##optional
    lapsum = 0
    check = 0
    #check the gap beetween the frame and see if the previous frame didn't get captured
    prevFrame = 0
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
    #captures all the frames and pushes them to laplist
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray, cv2.CV_64F).var()
            tup = (count, fm, frame, ret)
            laplist.insert(count, tup)
            count += 1
        else:
            break
    #optional, calc avg of laplacian and uses frames higher from the avg value
    for i in laplist:
        lapsum += i[1]
    lapavg = lapsum/frame_count
    #goes through the laplist and write the 10% frames into memory
    for i in laplist:
        perfectcount = 0
        #if the frame is better then the frames in this loop it adds 1 to count
        for j in laplist:
            if(i[1]>j[1]):
                perfectcount += 1
        #checking if the frame is better then 90% of the frames in the video
        if(perfectcount/frame_count>=0.9 and (i[0] - prevFrame)> 5):          
            print(i[1])
            print('Read %d frame: ' % i[0], i[3])
            cv2.imwrite(os.path.join(pathOut, (fileName + "frame{:d}.png").format(i[0])), i[2])
            prevFrame = i[0];
    cap.release()
    cv2.destroyAllWindows()

    
def main():
         
    arr = os.listdir('.')
    for i in range (len(arr)):
        if ".mp4" in arr[i]:
               extractFramesTen(arr[i], 'pictures')      
      
if __name__=="__main__":
    main()
    
