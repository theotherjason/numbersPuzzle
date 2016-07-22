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
        #print(self.container)
        for k in reversed(range(0,self.y)):
            for j in reversed(range(0, self.y)):
                for i in range(0, self.x):
                    # print(self.pieces[num,i,j])
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
        #print(self.pieces[num])
        for j in reversed(range (0,self.y)):
            for i in range (0,self.x):
                #print(self.pieces[num,i,j])
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


def main():
    numberCase =  puzzleContainer(5,5,5)
    numberCase.print()
    print("The size of the puzzleContainer is",numberCase.size(), "\n")

    numberPieces = puzzlePieces(10,3,5)

    #define 0
    numberPieces.mark(0,0,0)
    numberPieces.mark(0,1,0)
    numberPieces.mark(0,2,0)
    numberPieces.mark(0,0,1)
    numberPieces.mark(0,2,1)
    numberPieces.mark(0,0,2)
    numberPieces.mark(0,2,2)
    numberPieces.mark(0,0,3)
    numberPieces.mark(0,2,3)
    numberPieces.mark(0,0,4)
    numberPieces.mark(0,1,4)
    numberPieces.mark(0,2,4)

    numberPieces.print(0)

    #define 1
    numberPieces.mark(1,0,0)
    numberPieces.mark(1,1,0)
    numberPieces.mark(1,2,0)
    numberPieces.mark(1,1,1)
    numberPieces.mark(1,1,2)
    numberPieces.mark(1,1,3)
    numberPieces.mark(1,0,4)
    numberPieces.mark(1,1,4)

    numberPieces.print(1)

    #define 2
    numberPieces.mark(2,0,0)
    numberPieces.mark(2,1,0)
    numberPieces.mark(2,2,0)
    numberPieces.mark(2,0,1)
    numberPieces.mark(2,0,2)
    numberPieces.mark(2,1,2)
    numberPieces.mark(2,2,2)
    numberPieces.mark(2,2,3)
    numberPieces.mark(2,0,4)
    numberPieces.mark(2,1,4)
    numberPieces.mark(2,2,4)

    numberPieces.print(2)

    #define 3
    numberPieces.mark(3,0,0)
    numberPieces.mark(3,1,0)
    numberPieces.mark(3,2,0)
    numberPieces.mark(3,2,1)
    numberPieces.mark(3,0,2)
    numberPieces.mark(3,1,2)
    numberPieces.mark(3,2,2)
    numberPieces.mark(3,2,3)
    numberPieces.mark(3,0,4)
    numberPieces.mark(3,1,4)
    numberPieces.mark(3,2,4)

    numberPieces.print(3)

    #define 4
    numberPieces.mark(4,2,0)
    numberPieces.mark(4,2,1)
    numberPieces.mark(4,0,2)
    numberPieces.mark(4,1,2)
    numberPieces.mark(4,2,2)
    numberPieces.mark(4,0,3)
    numberPieces.mark(4,2,3)
    numberPieces.mark(4,0,4)
    numberPieces.mark(4,2,4)

    numberPieces.print(4)

    #define 5
    numberPieces.mark(5,0,0)
    numberPieces.mark(5,1,0)
    numberPieces.mark(5,2,0)
    numberPieces.mark(5,2,1)
    numberPieces.mark(5,0,2)
    numberPieces.mark(5,1,2)
    numberPieces.mark(5,2,2)
    numberPieces.mark(5,0,3)
    numberPieces.mark(5,0,4)
    numberPieces.mark(5,1,4)
    numberPieces.mark(5,2,4)

    numberPieces.print(5)

    #define 6
    numberPieces.mark(6,0,0)
    numberPieces.mark(6,1,0)
    numberPieces.mark(6,2,0)
    numberPieces.mark(6,0,1)
    numberPieces.mark(6,2,1)
    numberPieces.mark(6,0,2)
    numberPieces.mark(6,1,2)
    numberPieces.mark(6,2,2)
    numberPieces.mark(6,0,3)
    numberPieces.mark(6,0,4)
    numberPieces.mark(6,1,4)
    numberPieces.mark(6,2,4)

    numberPieces.print(6)

    #define 7
    numberPieces.mark(7,2,0)
    numberPieces.mark(7,2,1)
    numberPieces.mark(7,2,2)
    numberPieces.mark(7,2,3)
    numberPieces.mark(7,0,4)
    numberPieces.mark(7,1,4)
    numberPieces.mark(7,2,4)

    numberPieces.print(7)

    #define 8
    numberPieces.mark(8,0,0)
    numberPieces.mark(8,1,0)
    numberPieces.mark(8,2,0)
    numberPieces.mark(8,0,1)
    numberPieces.mark(8,2,1)
    numberPieces.mark(8,0,2)
    numberPieces.mark(8,1,2)
    numberPieces.mark(8,2,2)
    numberPieces.mark(8,0,3)
    numberPieces.mark(8,2,3)
    numberPieces.mark(8,0,4)
    numberPieces.mark(8,1,4)
    numberPieces.mark(8,2,4)

    numberPieces.print(8)

    #define 9
    numberPieces.mark(9,0,0)
    numberPieces.mark(9,1,0)
    numberPieces.mark(9,2,0)
    numberPieces.mark(9,2,1)
    numberPieces.mark(9,0,2)
    numberPieces.mark(9,1,2)
    numberPieces.mark(9,2,2)
    numberPieces.mark(9,0,3)
    numberPieces.mark(9,2,3)
    numberPieces.mark(9,0,4)
    numberPieces.mark(9,1,4)
    numberPieces.mark(9,2,4)

    numberPieces.print(9)

    numberPieces.clearNumber(9)

    numberPieces.print(9)

    print(numberPieces.piece(1)+numberPieces.piece(2))




if __name__ == "__main__": main()