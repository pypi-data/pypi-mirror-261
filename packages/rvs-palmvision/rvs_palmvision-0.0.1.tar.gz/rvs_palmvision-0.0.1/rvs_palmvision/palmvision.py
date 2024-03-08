import cv2
import mediapipe as mp
import time


class Palmvision():
    def __init__(self, mode=False, maxHands = 2, modelComplexity=1 , detectionCon=0.8, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findpalm(self, img, draw=True):
     
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw: 
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo=0, draw= True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id, lm)
                h, w, c=img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
            
                    cv2.circle(img, (cx,cy), 7, (255, 0, 0), cv2.FILLED)

        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    detector = Palmvision()
    while True:
        success, img = cap.read()
        img = detector.findpalm(img)
        lmList = detector.findPosition(img) 
        if len(lmList) !=0:
            print(lmList[8])
        cTime = time.time()
        fps = 2/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3,(255,0,255), 3)


        cv2.imshow("Inmage", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()