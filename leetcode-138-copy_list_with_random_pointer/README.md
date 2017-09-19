The difficulty is to duplicate random pointers. To track the position of nodes random pointers point to, we can put the duplicated nodes after the original nodes. 
To track all the nodes in the linked list, we will walk through all nodes three times. 
The first round is to copy all nodes and put duplicated nodes after the original nodes. 
The second round is to copy thr random nodes.
The third round is to separate duplicated nodes from original nodes.
