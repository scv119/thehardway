# leetcode: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

def connect(self, root):
    # time complexity: O(n), space complexity: O(n), n is the number of nodes
        if root == None:
            return
        queue = [root]
        next_level = []
        while len(queue) != 0:
            i = 0
            while i < len(queue):
                node = queue[i]
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
                i = i + 1
            if i == len(queue):
                for i in xrange(len(next_level) - 1):
                    next_level[i].next = next_level[i+1]
                queue = next_level
                next_level = []

def connect(self, root):
        # use a head as a dummy pointer to track the first element of child level
        # use cur to track all the elements in child level
        # root track whether this level has completed
        # once root == None: meaning this level has completed and use head to get next level's root, then current level's first child will be new root. Free head and cur to track the next level's first child node.
        head = cur = TreeLinkNode(0)
        while root != None:
            if root.left != None:
                cur.next = root.left
                cur = cur.next
            if root.right != None:
                cur.next = root.right
                cur = cur.next
            root = root.next
            if root == None:
                root = head.next
                cur = head
                head.next = None
