from binarytree import Tree

start = Tree("hi there :). this is a test thing. welcome to the test thing. you can go outside or you can not go outside. enter '1' for the former, and '2' for the latter.", False)
outside = Tree("you win", True)
start.option1 = outside
inside = Tree("you died :(", False)
start.option2 = inside
iLikeThatNumber = Tree("cool number, bro. nice choice", True)
ew = Tree("you are still dead", True)
inside.option1 = ew
inside.option2 = iLikeThatNumber