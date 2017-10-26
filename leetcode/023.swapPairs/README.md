https://leetcode.com/problems/swap-nodes-in-pairs/description/

recursive:
swap first two nodes, then second node's next points to swap result of head.next.next

iterative:
use pre, pair1, pair2 to track the node before the pair, the first node in pair, the second node in pair
pair1.next = pair2.next 
pair2.next = pair1
pre.next = pair2
pre = pair1
iterated until pair1 or pair2 == None
