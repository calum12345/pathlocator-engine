class Tree:
    ##
    #this class is used as a data type to represent the paths the user can take. it's a binary tree. child nodes are option1 and option2
    def __init__(self, description, isDeadEnd: bool):
        self.description = description
        self.option1 = None
        self.option2 = None
        ## this marks if reaching this node should end the game and restart the program
        self.isDeadEnd = isDeadEnd
