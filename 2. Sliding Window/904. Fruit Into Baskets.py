class Solution:
    """
    Approach 1: Sliding Window + Hash Table
    time: O(n),
    space: O(1), since <hashtable> has no more than 3 keys.
    """
    def totalFruit(self, fruits: List[int]) -> int:
        hashtable, n = defaultdict(int), len(fruits)
        left, res = 0, 0
        for right in range(n):
            hashtable[fruits[right]] += 1
            while len(hashtable) > 2:
                hashtable[fruits[left]] -= 1
                if hashtable[fruits[left]] == 0:
                    hashtable.pop(fruits[left])
                left += 1
            res = max(res, right-left+1)
        return res
