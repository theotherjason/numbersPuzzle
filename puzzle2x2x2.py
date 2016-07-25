#!/usr/bin/python3

import puzzleClasses

def main():
    numberCase =  puzzleClasses.puzzleContainer(2,2,2)
    numberCase.print()
    print("The size of the puzzleContainer is",numberCase.size(), "\n")

    numberPieces = puzzleClasses.puzzlePieces(3,2,2)

    #define 0
    numberPieces.mark(0,0,0)
    numberPieces.mark(0,1,0)
    numberPieces.mark(0,1,1)

    numberPieces.print(0)

    #define 1
    numberPieces.mark(1,1,0)
    numberPieces.mark(1,0,1)
    numberPieces.mark(1,1,1)

    numberPieces.print(1)

    #define 2
    numberPieces.mark(2,0,0)
    numberPieces.mark(2,1,0)

    numberPieces.print(2)

    print(numberPieces.piece(1)+numberPieces.piece(2))




if __name__ == "__main__": main()