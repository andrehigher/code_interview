# Describe how you use a single array a single array to implement three stacks?

# We could use an array and populate for each 3 elements an specific stack. For example, an array: [1,2,3,4,5,6,7,8,9] would be the stacks [1,4,7], [2,5,8] and [3,6,9]. The problem here is that if stacks have different sizes, we could have an array with many empty spaces which is not desired. E.g.: [1,4,7], [2], [3,6,9,12,15,18]

# Another approach is to keep the the length of stacks in the beginning of the array and control the pop and push operations over it. For example, in the beggining we have: [0,0,0] which means we don't have any elements in the stack. If we would like to push an element in the stack #2, so we update the count number and then add the element there such as: [0,1,0,7]. So we know that 7 is the first element of the stack #2. If we would like to add the first element to the stack #1, it would be: [1,1,0,8,7]. The complexity to add an element is O(n) since if we need to add an element in the stack #1 probably we need to move every other elements in other stacks.

