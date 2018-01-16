from graphics import *
from random import randint
mid = 500   #MIDDLE VALUE FOR GRAPHICS
dist = 20   #DISTANCE BETWEEN POINTS MODIFIER
speed = 0   #1=1 SECOND ETC
class sloppyKNN():
    def eucDist(self,x1,y1,x2,y2):
        return ((x1-x2)**2 + (y1-y2)**2)**.5    #ALGORITHM FOR KNN

    def quicksort(self, arr):
    	if not arr:
    		return []
    	return self.quicksort([x for x in arr if x < arr[0]]) \
            + [x for x in arr if x == arr[0]] \
            + self.quicksort([x for x in arr if x > arr[0]])

#----------------------------------------------------------------
    def resetCounter(self):
        self.order = [0]
        self.label = ["black"]
        self.feature1 = [0]
        self.feature2 = [0]

    def train(self, label, feature1, feature2):
        self.label = label          #COLOR
        self.feature1 = feature1    #X COORD
        self.feature2 = feature2    #Y COORD
        self.order = self.order[-1]+1	#LAST ELEM
        for i in range(len(label)):
            self.makePoint(feature1[i], feature2[i], label[i])
            time.sleep(speed)  #DELAYS FOR ANIMATION PURPOSES
#----------------------------------------------------------------
    def predict(self, unknownfeature1, unknownfeature2, unknownBig):
    	#for i in range()
        self.tempX = unknownfeature1
        self.tempY = unknownfeature2
        self.tempBig = unknownBig
        for i in range(int(len(self.tempX))):
        	if(self.tempX[i] in self.feature1):
        		if(self.tempY[i] == self.feature2[self.feature1.index(self.tempX[i])]):
        			del self.tempX[i]
        			del self.tempY[i]
        			del self.tempBig[i]
        self.sortedTempBig = self.quicksort(self.tempBig)
        for i in range(int(len(self.sortedTempBig))):
        	indexOrder = self.tempBig.index(self.sortedTempBig[i])
        	#self.tempX[indexOrder], self.tempX[i] = self.tempX[i] , self.tempX[indexOrder]
        	#self.tempY[indexOrder], self.tempY[i] = self.tempY[i] , self.tempY[indexOrder]
        	#print(self.tempX[indexOrder])
        	#self.tempBig[i], self.tempBig[indexOrder] = self.tempBig[indexOrder] , self.tempBig[i]

        #print(self.tempBig)
        #print(self.sortedTempBig)
        for i in range((int)(len(unknownfeature1)/1)):           #RUNS ENTIRE ARRAY LEN
            #print(self.tempBig[i])
            indexOrder = self.sortedTempBig.index(self.tempBig[i])
            #print(indexOrder)
            self.makePoint(self.tempX[indexOrder],self.tempY[indexOrder], "black")
            msg = Text(Point(mid,mid/10), str(i))   #PRINTS I TO UPPER MIDDLE OF WIN
            msg.setSize(36)    #LARGEST SIZE
            msg.draw(win)
            time.sleep(speed)
            label1index = self.closest(self.tempX[indexOrder],self.tempY[indexOrder])
            label2index = self.secClosest(self.tempX[indexOrder],self.tempY[indexOrder],label1index)
            self.makeLine(label1index,self.tempX[indexOrder],self.tempY[indexOrder])    #ANIMATES THE
            self.makeLine(label2index,self.tempX[indexOrder],self.tempY[indexOrder])    #KNN
            msg.undraw()    #CLEAN UP
            if(label[label1index] == label[label2index]):
                self.label.append(label[label1index])       #ADDING THE PARTS TO MAKE IT A
                self.feature1.append(self.tempX[indexOrder])    #PART OF THE FEATURES
                self.feature2.append(self.tempY[indexOrder])
                self.makePoint(self.tempX[indexOrder],self.tempY[indexOrder],label[label1index])    #UPDATES COLOR GRAPHIC
                time.sleep(speed)
            else:
                self.label.append("black")                       #UNSAFE FEATURE ADDITION
                self.feature1.append(self.tempX[indexOrder])
                self.feature2.append(self.tempY[indexOrder])
        for i in range((int)(len(unknownfeature1)/2)):
        	pass
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
classifier.resetCounter()
classifier.train(label,xfeat,yfeat) #TRAINS CLASSIFIER BY USING FILE
#----------------------------------------------------------------


print("\n\n\nSKNN WILL NOW CREATE RANDOM FEATS")
msg = Text(Point(mid,mid/10), "CREATING BOARD")   #PRINTS I TO UPPER MIDDLE OF WIN
msg.setSize(36)    #LARGEST SIZE
msg.draw(win)
randxFeats = [] #INITIALIZATION
randyFeats = []
randBigFeats = []
bigBoard = []   #HOLDS UNMADE RANDOM FEATURE DATA POINTS
randIndex = 0
unneededcounter = 0
for ten in range(0,int(mid/(dist/2))-1): #CREATES bigBOARD
    for one in range(0,int(mid/(dist/2))-1):
        bigBoard.append(ten*1000+one)    #CREATES BIG NUMBERS BUT AVOID LIST OF LIST
while(bigBoard):
	unneededcounter += 1
	randIndex = randint(0, len(bigBoard)-1)
	randBigFeats.append(bigBoard[randIndex])	#USED FOR SORTING
	randyFeats.append(((bigBoard[randIndex])%1000)-(mid/dist)+1)
	randxFeats.append((((bigBoard[randIndex])-(randyFeats[-1]+(mid/dist)))/1000)-(mid/dist)+1)
	del bigBoard[randIndex]
msg.undraw()        
print("IT TOOK " + str(unneededcounter) + " GUESSES TO GET " + str(len(randyFeats)) + " SPOTS")
randPred = classifier.predict(randxFeats,randyFeats,randBigFeats)
win.getMouse()
win.close()