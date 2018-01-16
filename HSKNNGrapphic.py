from graphics import *
from random import randint
mid = 500   #MIDDLE VALUE FOR GRAPHICS
dist = 20   #DISTANCE BETWEEN POINTS MODIFIER
speed = 0   #1=1 SECOND ETC
class sloppyKNN():
    def eucDist(self,x1,y1,x2,y2):
        return ((x1-x2)**2 + (y1-y2)**2)**.5    #ALGORITHM FOR KNN
#----------------------------------------------------------------
    def train(self, label, feature1, feature2):
        self.label = label          #COLOR
        self.feature1 = feature1    #X COORD
        self.feature2 = feature2    #Y COORD
        for i in range(len(label)):
            self.makePoint(feature1[i], feature2[i], label[i])
            time.sleep(speed)  #DELAYS FOR ANIMATION PURPOSES
#----------------------------------------------------------------
    def predict(self, unknownfeature1, unknownfeature2):
        predictions = []                                #INITIALIZATIONS
        for i in range(len(unknownfeature1)):           #RUNS ENTIRE ARRAY LEN
            self.makePoint(unknownfeature1[i],unknownfeature2[i], "black")
            msg = Text(Point(mid,mid/10), str(i))   #PRINTS I TO UPPER MIDDLE OF WIN
            msg.setSize(36)    #LARGEST SIZE
            msg.draw(win)
            time.sleep(speed)
            label1index = self.closest(unknownfeature1[i],unknownfeature2[i])
            label2index = self.secClosest(unknownfeature1[i],unknownfeature2[i],label1index)
            self.makeLine(label1index,unknownfeature1[i],unknownfeature2[i])    #ANIMATES THE
            self.makeLine(label2index,unknownfeature1[i],unknownfeature2[i])    #KNN
            msg.undraw()    #CLEAN UP
            if(label[label1index] == label[label2index]):
                predictions.append(label[label1index])      #ADDS LABEL TO PREDICTION LIST
                self.label.append(label[label1index])       #ADDING THE PARTS TO MAKE IT A
                self.feature1.append(unknownfeature1[i])    #PART OF THE FEATURES
                self.feature2.append(unknownfeature2[i])
                self.makePoint(unknownfeature1[i],unknownfeature2[i],label[label1index])    #UPDATES COLOR GRAPHIC
                time.sleep(speed)
            else:
                predictions.append("UNKNOWN")
                self.label.append("black")                       #UNSAFE FEATURE ADDITION
                self.feature1.append(unknownfeature1[i])
                self.feature2.append(unknownfeature2[i])
        return predictions              #RETURNS ARRAY OF BEST LABELS
#----------------------------------------------------------------
    def closest(self,x,y):
        best_dist = self.eucDist(x,y,self.feature1[0],self.feature2[0])        #CREATES A BASE CASE
        best_index = 0
        for i in range(0,len(self.feature1)):                  #RUNS ENTIRE ARRAY LEN
            dist = self.eucDist(x,y,self.feature1[i],self.feature2[i])
            if dist < best_dist:                                #COMPARING CURRENT TO BEST
                best_dist = dist
                best_index = i
        return best_index                                    #RETURNS INDEX OF BEST FEATURE
#----------------------------------------------------------------
    def secClosest(self,x,y,best):
        if(best == 0):
            best_dist = self.eucDist(x,y,self.feature1[1],self.feature2[1])        #CREATES A BASE CASE
            best_index = 1
        else:
            best_dist = self.eucDist(x,y,self.feature1[0],self.feature2[0])        #CREATES A BASE CASE
            best_index = 0
        for i in range(0,len(self.feature1)):                  #RUNS ENTIRE ARRAY LEN
            if(best != i):
                dist = self.eucDist(x,y,self.feature1[i],self.feature2[i])
                if dist < best_dist:                                #COMPARING CURRENT TO BEST
                    best_dist = dist
                    best_index = i
        return best_index                            #RETURNS INDEX OF BEST FEATURE
#----------------------------------------------------------------
#GRAPHICS CLASS ADDITIONS
    def makePoint(self, x, y, color):
        rad = dist/2    #MODIFIER FOR SIZE OF POINT
        tempPoint = Circle(Point(mid+x*dist,mid-y*dist),rad)    #MAKES POINT
        tempPoint.setFill(color)    #SETS COLOR
        tempPoint.draw(win)         #PRINTS TO WIN
#----------------------------------------------------------------
    def makeLine(self, index1, featx, featy):
        tempLine = Line(Point(mid+self.feature1[index1]*dist,mid-self.feature2[index1]*dist), Point(mid+featx*dist,mid-featy*dist))
        tempLine.setWidth(5)
        tempLine.draw(win)
        time.sleep(speed)
        tempLine.undraw()   #PRINTS TO WIN/DELETES
#----------------------------------------------------------------
#CLASSIFIER HAS BEEN DEFINED
#----------------------------------------------------------------
with open("4Corners.txt", "r") as file: 
    A = []
    for line in file:
        A.append(line)                  #ADDS WHOLE LINE TO ARRAY A
    A = [line.strip() for line in A]    #TAKES OFF TRAILING "\n"
    A.sort()                            #SORTS DATA SO LABElS ARE GROUPED
    label =[]       #INITIALIZATIONS
    xfeat = []
    yfeat = []
    for i in A:
        l, x, y = i.split(":") #CREATING TEMP DATA TO APPEND TO OUR ARRAYS
        label.append(l)
        xfeat.append(int(x))
        yfeat.append(int(y))
file.close()                        #SAFETY
#----------------------------------------------------------------
#FILE HAS BEEN READ
#----------------------------------------------------------------
test = int(input("WHAT SHOULD THE SIZE OF DOTS BE?\n"))
dist = test


#----------------------------------------------------------------
win = GraphWin('SKNN THOUGHTS', mid*2, mid*2)
yAxis = Line(Point(0,mid),Point(mid*2,mid))
yAxis.draw(win)
xAxis = Line(Point(mid,0),Point(mid,mid*2))
xAxis.draw(win)
print("INCOMING FEATURE DATA")
print(label)    #FROM THE DATA FILE
print(xfeat)
print(yfeat)
classifier = sloppyKNN()
classifier.train(label,xfeat,yfeat) #TRAINS CLASSIFIER BY USING FILE
#----------------------------------------------------------------


print("\n\n\nSKNN WILL NOW CREATE RANDOM FEATS")
msg = Text(Point(mid,mid/10), "CREATING BOARD")   #PRINTS I TO UPPER MIDDLE OF WIN
msg.setSize(36)    #LARGEST SIZE
msg.draw(win)
randxFeats = [] #INITIALIZATION
randyFeats = []
bigBoard = []   #HOLDS UNMADE RANDOM FEATURE DATA POINTS
for ten in range(0,int(mid/(dist/2))-1): #CREATES bigBOARD
    for one in range(0,int(mid/(dist/2))-1):
        bigBoard.append(ten*100+one)    #CREATES BIG NUMBERS BUT AVOID LIST OF LIST
for i in range(0,mid**2):
    #temp1 = (int)((randint(0,int(mid/10)-1)+randint(0,int(mid/10)-1)+randint(0,int(mid/10)-1)+randint(0,int(mid/10)-1)+randint(0,int(mid/10)-1))/5)    #USES MID FOR EXPANDABLITY
    #temp2 = (int)((randint(0,int(mid/10)-1)+randint(0,int(mid/10)-1)+randint(0,int(mid/10)-1)+randint(0,int(mid/10)-1)+randint(0,int(mid/10)-1))/5)
    temp1 = randint(0,int(mid/(dist/2))-1)
    temp2 = randint(0,int(mid/(dist/2))-1)
    if((int)(temp1*100+temp2) in bigBoard):  #IF NEW RANDOM POINT IS IN BOARD THEN
        randxFeats.append((temp1)-(int(mid/dist))+1)    #CREATE FEATURE DATA
        randyFeats.append((temp2)-(int(mid/dist))+1)
        bigBoard.remove((temp1*100)+(temp2))            #AND REMOVE THE POINT ON BOARD
    if(not bigBoard):   #WHEN BOARD IS EMPTY KILL THE LOOP
        print(i)
        break;
msg.undraw()        
print(bigBoard) #SHOULD PRINT EMPTY ARRAY IF LOOP WORKED WELL
randPred = classifier.predict(randxFeats,randyFeats)
win.getMouse()
win.close()