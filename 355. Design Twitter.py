from collections import defaultdict, deque
from functools import partial
import heapq


# NOTE: tweetId is not increasing, tweetId = 3 may post later than tweedId = 5
class Twitter(object):
    only_record_last = 10
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.tweets = defaultdict(partial(deque, maxlen=self.only_record_last))
        self.relation = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.count += 1
        self.tweets[userId].appendleft((self.count, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        n = self.only_record_last - len(self.tweets[userId])
        H = [(-1, -1)] * n + list(self.tweets[userId])[::-1]
        for followeeId in self.relation[userId]:
            for t in self.tweets[followeeId]:
                if t > H[0]:
                    heapq.heapreplace(H, t)
                else:
                    break
        return list(map(lambda x: x[1],
                        sorted((t for t in H if t[0] > 0), reverse=True)))

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId != followerId:
            self.relation[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
t        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.relation[followerId]:
            self.relation[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
obj.postTweet(1, 3)
print(obj.getNewsFeed(1))
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
