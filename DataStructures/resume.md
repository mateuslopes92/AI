# Resume of study of data structures and sorts

## Arrays
in python lists is implemented as dynamic array

my_array = [32, 5, 7, 96]

internal memory representation (run by cpu but use ram to store variables)
0x00500 [  32  ]
0x00504 [  5  ]
0x00508 [  7  ]
0x0050A [  96  ]


## Linked list
Very similar to array but store the values randomly in the memory and have a link for the next item,
also could be with reference for last and next item(doubled linked list)

my_array = [32, 5, 7, 96]

0x00500 [  32 [0x00A1] ]
0x00A1 [  5  [0x00C5] ]
0x00C5 [  7  [0x00C5] ]
0x00D7 [  96  [0x00C0] ]

The benefits over array:
1. You dont need to pre pre-allocate space
2. Insertion is easier (only swap the links)


## Hash table
Hash table use a hash function to identify the items allocated in the memory
The hash function could be using asc table or any other function
A good hash function needs to handle the collisions

in python use dictionary
my_hash_table = {
  'march 6': 310.0,
  'march 7': 310.1,
}

my_hash_table['march 6'] -> 609 -> 9
m 109
a 97
r 114
c 99
h 104
  32
6 54

sum 609 -> MOD(609, 10) -> 9 where 10 is size of the array


## Stack
implemented with LIFO last in first out

can be implemented as list(array)

my_stack = [1, 2]
my_stack.append(3)
[1, 2, 3]
my_stack.pop()
return 3 and new state is [1, 2]


## Queue
implemented with FIFO first in first out

can be implemented as list(array)
or as dequeue from colletions and
queue from LifoQueue

my_queue = [1, 2]
my_queue.insert(0, 3)
[3, 1, 2]
my_queue.pop()
return 2 and new state is [3, 1]


## Tree (General Tree)
Trees can be represented and divided in Root Node, Node and Leaf Nodes

For an easy representation will try reproduce the structure in levels
- Eletronics <- Level 1
  - Laptops <- Level 2
    - Macbook <- Level 3
    - Surface
    - Thinkpad

In code could be a class like this

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self, child):
    child.parent = self
    self.children.append(child)

root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Surface"))
laptop.add_child(TreeNode("Thinkpad"))


## Binary Tree O(log n)
Binary Tree is like a Tree but with a constraint that has at most 2 child nodes
Left nodes are smaller values and right side are the bigger ones
