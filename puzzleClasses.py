#!/usr/bin/python3

import numpy as np

class puzzleContainer:

    # The 3d puzzle container will be empty and retain it's x/y/z dimensions
    def __init__(self,x,y,z):
        self.container = np.zeros((x,y,z))
        self.x = x
        self.y = y
        self.z = z

    def size(self):
        return self.container.size

    # to print, reverse through z & y and iterate through x
    def print(self):
        for k in reversed(range(0,self.z)):
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

    # Our actual pieces are in a 3d array of their own, the 1st dimension being each 2d object,
    # and the other 2 dimensions being the x & y coordinates
    def __init__(self,num,x,y):
        self.pieces = np.zeros((num,x,y))
        self.x = x
        self.y = y

    def size(self):
        return self.pieces.size

    # To print the array, reverse through y & iterate through x
    def print(self,num):
        for j in reversed(range (0,self.y)):
            for i in range (0,self.x):
                if self.pieces[num,i,j] == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
            print ("")
        print("")

    # Use this to mark each x/y coordinate in each puzzle piece.
    def mark(self,num,x,y):
        self.pieces[num,x,y] = 1

    # Completely clear the number (if needed)
    def clearNumber(self,num):
        self.pieces[num] = 0

    def piece(self,num):
        return self.pieces[num]

    def transformedContainer(self,containerSize,num,locationX,locationY,locationZ,orientationX,orientationY,orientationZ):
        #create empty container
        #add transformed piece #num to container at locationX,locationY,locationZ
        #return puzzleContainer with transformed piece
        return True
