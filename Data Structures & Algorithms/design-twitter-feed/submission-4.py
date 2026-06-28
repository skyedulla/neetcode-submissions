from collections import defaultdict
class Twitter:

    def __init__(self):
        self.user_posts = []
        self.user_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_map:
            self.user_map[userId].add(userId)

        self.user_posts.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for i in range(len(self.user_posts) - 1, -1, -1):
            if self.user_posts[i][0] in self.user_map[userId]:
                feed.append(self.user_posts[i][1])
            
            if len(feed) == 10:
                return feed
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map:
            self.user_map[followerId].add(followerId)
        self.user_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map:
            self.user_map[followerId].add(followerId)

        if followeeId in self.user_map[followerId] and followeeId != followerId:
            self.user_map[followerId].remove(followeeId)
        
