import time
class Twitter:

    def __init__(self):
        self.wal = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.wal[userId].append([tweetId, time.time()])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        p = self.followers.get(userId)
        if p is not None:
            for user in p:
                if user != userId:
                    res.extend(self.wal[user])
        res.extend(self.wal[userId])
        res.sort(key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], res))[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.followers[followerId].remove(followeeId)
        except:
            return None
        

