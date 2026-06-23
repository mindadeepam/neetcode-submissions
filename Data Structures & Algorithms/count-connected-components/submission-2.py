class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for item in edges:
            s,d = item
            adj[s].append(d)
            adj[d].append(s)
        visited = [False]*n 
        ans = 0


        def dfs(curr):
            print(curr)
            visited[curr] = True

            for node in adj[curr]:
                if not visited[node]:
                    dfs(node)



        # go through each num
        for num in range(n):
            if visited[num]:
                continue
            else:
                # visited[num] = True
                ans+=1
                # do dfs and see which nodes it visits
                print(f"ans plus 1 -> {ans}, going to dfs with {num}")
                dfs(num)
        return ans
    