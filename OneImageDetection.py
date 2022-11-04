import os
import cv2
import numpy as np
import ImageExtractionFromVideo


#ImageExtractionFromVideo.Extraction('Videos/*')
NumberOfMatches = 0
NumberOfImages = sum(len(files) for r,d, files in os.walk("save") )
for i in range(0,NumberOfImages):
    path = f"save/Videos/GreenMarker/{i}.png"
    orb = cv2.ORB_create(nfeatures=2000)

    ##" Import Image

    BaseImage = cv2.imread(path)



    imgUser = cv2.imread('UserImg/img.jpeg')

    #cv2.imshow('imgUser',imgUser)
    #cv2.waitKey(0)

    def findDes(image):
        desList=[]
        kp,des = orb.detectAndCompute(BaseImage,None)
        desList.append(des)
        return desList




    def findId(img, desList, thres = 12):
        kp2,des2 = orb.detectAndCompute(img,None)
        bf = cv2.BFMatcher()
        matchList=[]
        finalVal = -1
        try:
            for des in desList:
                matches = bf.knnMatch(des, des2, k=2)
                good = []
                for m,n in matches:
                    if m.distance <0.75*n.distance:
                        good.append([m])
                matchList.append(len(good))
        except:
            pass
        #print(matchList)
        if len(matchList)!=0:
            if max(matchList) >thres:
                finalVal = matchList.index(max(matchList))

        return finalVal


    desList = findDes(BaseImage)

    TestValue = findId(imgUser,desList)




    if(TestValue != -1):
        NumberOfMatches += 1
    else:
        None


if NumberOfMatches >=20:
    print("it's a matche")

else:
    print("not a match")




