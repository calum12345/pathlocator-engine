from binarytree import Tree

start = Tree("hi there :). this is a test thing. welcome to the test thing. you can go outside or you can not go outside. enter '1' for the former, and '2' for the latter.", False)
outside = Tree("you win", True)
start.option1 = outside
inside = Tree("you died :(", True)
start.option2 = inside