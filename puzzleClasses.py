#!/usr/bin/python3

import numpy as np

class puzzleContainer:
    def __init__(self,x,y,z):
        self.container = np.zeros((x,y,z))
        self.x = x
        self.y = y
        self.z = z

    def size(self):

        return self.container.size

    def print(self):
        for k in reversed(range(0,self.y)):
            for j in reversed(range(0, self.y)):
                for i in range(0, self.x):
                    if self.container[i, j, k] == 1:
                        print("#", end="")
                    else:
                        print(" ", end="")
                print("")
            print("")
        print("")

    def add(self,transformedContainerObject):
        #add two containers
        #check for any >1 entries & return error if false
        #otherwise return true
        return True


class puzzlePieces:
    def __init__(self,num,x,y):
        self.pieces = np.zeros((num,x,y))
        self.x = x
        self.y = y

    def size(self):
        return self.pieces.size

    def print(self,num):
        for j in reversed(range (0,self.y)):
            for i in range (0,self.x):
                if self.pieces[num,i,j] == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
            print ("")
        print("")

    def mark(self,num,x,y):
        self.pieces[num,x,y] = 1

    def clearNumber(self,num):
        self.pieces[num] = 0

    def piece(self,num):
        return self.pieces[num]

    def transformedContainer(self,containerSize,num,locationX,locationY,locationZ,orientationX,orientationY,orientationZ):
        #create empty container
        #add transformed piece #num to container at locationX,locationY,locationZ
        #return puzzleContainer with transformed piece
        return True
