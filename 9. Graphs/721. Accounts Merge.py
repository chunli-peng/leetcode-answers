class Solution:
    """
    Approach 4: Union Find by Rank + Hash Table
    time: O(n*α(mn)) for union find, where α is This inverse Ackermann function, and α<5 for practical input.
        O(nlogn) for sorted(), totally, O(nlogn)
    space: O(n) for variable <parent>, <rank> in UnionFind.
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_acc = {}  # {email_address: index_account}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i

        acc_to_email = defaultdict(list)  # {index_account: [email_address, ...]}
        for email, i in email_to_acc.items():
            leader = uf.find(i)
            acc_to_email[leader].append(email)

        res = []
        for i in acc_to_email:
            res.append([accounts[i][0]] + sorted(acc_to_email[i]))
        return res

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        """Find and Return the parent of the point <x>"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Unite the point <x> and <y>"""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            elif self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            self.parent[root_y] = root_x
