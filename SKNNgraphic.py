from graphics import *
from random import randint
mid = 400   #MIDDLE VALUE FOR GRAPHICS
dist = 20   #DISTANCE BETWEEN POINTS MODIFIER
speed = 0   #1=1 SECOND ETC
win = GraphWin('SKNN THOUGHTS', mid*2, mid*2)
yAxis = Line(Point(0,mid),Point(mid*2,mid))
yAxis.draw(win)
xAxis = Line(Point(mid,0),Point(mid,mid*2))
xAxis.draw(win)
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
                #self.label.append(l)                       #UNSAFE FEATURE ADDITION
                #self.feature1.append(unknownfeature1[i])
                #self.feature2.append(unknownfeature2[i])
        return predictions              #RETURNS ARRAY OF BEST LABELS
#----------------------------------------------------------------
    def closest(self,x,y):
        best_dist = self.eucDist(x,y,self.feature1[0],self.feature2[0])        #CREATES A BASE CASE
        best_index = 0
        for i in range(0,len(self.feature1)):                  #RUNS ENTIRE ARRAY LEN
            dist = self.eucDist(x,y,self.feature1[i],self.feature2[i])
            #print("The distance from point ", end = "")     #FOR DEBUG SEEING DISTANCES
            #print(i, end = "")
            #print(" is ", end = "")
            #print(dist)
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
        rad = 10    #MODIFIER FOR SIZE OF POINT
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
with open("DataUsable.txt", "r") as file: 
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
print("INCOMING FEATURE DATA")
print(label)    #FROM THE DATA FILE
print(xfeat)
print(yfeat)

predictionLabels = ["red","red","yellow","red"] 
predictionXfeats = [4,0,-2,7]
predictionYfeats = [2,-1,0,-5]
print("\nINCOMING TEST DATA")
print(predictionLabels) #FROM THIS DATA 
print(predictionXfeats)
print(predictionYfeats)

print("\nSKNN IS CLASSIFYING TEST DATA")
classifier = sloppyKNN()
classifier.train(label,xfeat,yfeat) #TRAINS CLASSIFIER BY USING FILE
predictions = classifier.predict(predictionXfeats,predictionYfeats) #PREDICTS DATA
print("\nSKNN HAS PREDICTED")
print(predictions)

print("\n\n\nSKNN IS NOW CREATED RANDOM FEATS")
randxFeats = [] #INITIALIZATION
randyFeats = []
for i in range(0,5000): #CREATES RANDOM DATA TO ADD TO GRAPH
    randxFeats.append(randint(-19,19))
    randyFeats.append(randint(-19,19))
randPred = classifier.predict(randxFeats,randyFeats)    
print("RANDOM PREDICTIONS")
print(randxFeats)
print(randyFeats)
print(randPred)
win.getMouse()
win.close()