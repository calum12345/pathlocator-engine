#!/usr/local/bin/python3

from binarytree import Tree
import path

if __name__ == "__main__":
    currentNode = path.start
    while True:
        print(currentNode.description)
        if currentNode.isDeadEnd == True:
            exit()
        while True:
            choice = input("Type either '1' or '2' to choose the first option or the second option respectively\n")
            if choice == '1' or choice == '2':
                break
        if choice == '1':
            currentNode = currentNode.option1
        else:
            currentNode = currentNode.option2
