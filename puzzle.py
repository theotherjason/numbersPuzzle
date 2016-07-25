#!/usr/bin/python3

import puzzleClasses

def main():
    numberCase =  puzzleClasses.puzzleContainer(5, 5, 5)
    numberCase.print()
    print("The size of the puzzleContainer is",numberCase.size(), "\n")

    numberPieces = puzzleClasses.puzzlePieces(10,3,5)

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