class Twitter:
    """
    Approach 1: Max Heap + Hash table
    time: O(1) for postTweet(), follow(), unfollow(),
        O(n*logn) for build heap, where n is followee numbers of the follower,
        O(m*logn) for pop and push, where m is numbers of most recent tweets,
        totally, O((m+n)logn) for getNewsFeed().
    space: O(N^2) for follow_map, where N is total users,
        O(M) for tweet_map, where M is the total number of tweets.
    """
    def __init__(self):
        self.time = 0  # negative time for max heap
        self.tweet_map = defaultdict(list)  # userId: list of [time, tweetIds]
        self.follow_map = defaultdict(set)  # userId: set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        self.follow(userId, userId)  # users follow themselves
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1  # index of the final element
                time, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(max_heap, [time, tweetId, followeeId, index-1])

        while max_heap and len(res) < 10:
            _, tweetId, followeeId, index = heapq.heappop(max_heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(max_heap, [time, tweetId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
