from collections import deque

def canFinish( numCourses, prerequisites):
    adj=[[] for _ in range(numCourses)]
    ind=[0]*numCourses
    for i in range(len(prerequisites)):
        src=prerequisites[i][0]
        des=prerequisites[i][1]
        adj[des].append(src)
        ind[src]+=1
        

    q=deque()
        
    def bfs(adj,ind):
        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)
            
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for i in range(len(adj[node])):
                nei=adj[node][i]
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        return len(res)==numCourses
    return bfs(adj,ind)
print(canFinish(2,[[1,0]]))
        
        