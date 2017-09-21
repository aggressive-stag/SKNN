class sloppyKNN():
    def eucDist(self,x1,y1,x2,y2):
        return ((x1-x2)**2 + (y1-y2)**2)**.5
#----------------------------------------------------------------
    def train(self, label, feature1, feature2):
        self.label = label          #COLOR
        self.feature1 = feature1    #X COORD
        self.feature2 = feature2    #Y COORD
#----------------------------------------------------------------
    def predict(self, unknownfeature1, unknownfeature2):
        predictions = []                                #INITIALIZATIONS
        for i in range(len(unknownfeature1)):           #RUNS ENTIRE ARRAY LEN
            label1index = self.closest(unknownfeature1[i],unknownfeature2[i])
            label2index = self.secClosest(unknownfeature1[i],unknownfeature2[i],label1index)
            if(label[label1index] == label[label2index]):
                predictions.append(label[label1index])      #ADDS LABEL TO PREDICTION LIST
                self.label.append(label[label1index])       #ADDING THE PARTS TO MAKE IT A
                self.feature1.append(unknownfeature1[i])    #PART OF THE FEATURES
                self.feature2.append(unknownfeature2[i])
            else:
                predictions.append("UNKNOWN")
                #self.label.append(l)                       #UNSAFE FEATURE ADDITION
                #self.feature1.append(unknownfeature1[i])
                #self.feature2.append(unknownfeature2[i])
            #print("CASE ", end = "")    #FOR DEBUG SEEING BEST 2 INDEXES
            #print(i)
            #print("The best index is: ", end = "")
            #print(label1index, end = "")
            #print(" which is color ", end = "")
            #print(label[label1index])
            #print("The 2nd index is: ", end = "")
            #print(label2index, end = "")
            #print(" which is color ", end = "")
            #print(label[label2index])
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
        return best_index                           #RETURNS INDEX OF BEST FEATURE
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
        return best_index                           #RETURNS INDEX OF BEST FEATURE
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
print(label)
print(xfeat)
print(yfeat)

predictionLabels = ["Red","Red","Yellow"]
predictionXfeats = [4,0,-2]
predictionYfeats = [2,-1,0]
print("\nINCOMING TEST DATA")
print(predictionLabels)
print(predictionXfeats)
print(predictionYfeats)

print("\nSKNN IS CLASSIFYING TEST DATA")
classifier = sloppyKNN()
classifier.train(label,xfeat,yfeat)
predictions = classifier.predict(predictionXfeats,predictionYfeats)
print("\nSKNN HAS PREDICTED")
print(predictions)