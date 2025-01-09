class DSU:
    def __init__(self,n):
        rank = [0]*(n+1)#the items which has more number of connected nodes than the other will be parent node
        parent = []*(n+1)
        size = [1]*(n+1)#the node which has more child nodes in the whole tree will be parent of other
        for i in range(n+1):
            parent[i] = i
    def find(self,node):#find the parent node for a particular node
        if node == parent[node]:return node
        return find(parent[node])
    def union(self,u,v):
        u,v = self.find(u),self.find(v)
        def union_rank():#using rank to get the parent particular node
            if u == v:return
            if rank[u]<rank[v]:
                parent[u] = v
            elif rank[u]>rangek[v]:
                parent[v] = u
            else:
                parent[v] = u
                rank[u] += 1
        def union_size():#using size to get the parent of particular node
            if u == v :return
            if size[v]<size[u]:
                parent[v]=u
                size[u] += size[v]
            elif size[u]<size[v]:
                parent[u]=v
                size[v] += size[u]
            else:
                parent[v]=u
                size[u] += size[v]

if __name__ == "__main__":

    dsu = DSU(7)
