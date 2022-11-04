import os
import ImageExtractionFromVideo as Extract
import OneImageDetection


NumberOfImages = sum(len(files) for r,d, files in os.walk("save") )
MaxMatches = 0
temp = 0
Matches = []

for i in range(NumberOfImages):
    Matches.append(ImageDetection("UserImg",classNames))

for i in range(0,len(Matches)):
    print(Matches[i])
