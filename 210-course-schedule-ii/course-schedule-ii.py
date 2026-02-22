class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the adjacency list 
        courses_and_prereqs = {i: [] for i in range(numCourses)}
        for nxt, pre in prerequisites: 
            courses_and_prereqs[pre].append(nxt)

        visited = set()
        visiting = set()
        output = []

        # the order formed: [course -> prerequisites]
        def dfs(node): 
            # if it's the current node being visited, that means there's a cycle (or it means the node is the result of a prerequisite that requires itself to also be a prerequisite)  
            if node in visiting: 
                return False 
            
            # if this node has already been visited, then that means it's already added into the order formed
                # return True because we want the search to be going, it's not invalid 
            if node in visited: 
                return True 

            visiting.add(node)

            # look at the course this prerequisite serves
            for neighbor in courses_and_prereqs[node]: 
                # if there is a cycle detected: 
                if not dfs(neighbor):
                    return False # when a neighbor return False, it will eventually return all the previous dfs calls, and eventually reach the outer for loop below, where it will end up returning []
                
            # since this is happening outside the for loop which contains the dfs, the order of arrangements goes from course then prerequisites 
            visiting.remove(node)
            visited.add(node)
            output.append(node)

            # return True because we need to identify when it is not True, i.e. when there is a cycle detected 
            return True 

        # this is happening because we don't have a guarantee that all courses are gonna be connected to each other 
        for i in range(numCourses): 
            if not dfs(i): 
                return []
        
        return output[::-1]

        




        