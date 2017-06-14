from twitter_api.meta_extractor import HistExtractor


class TwitterUser:
    def __init__(self, twitter_user):

        self.db_cols = {"mongo": ["status", 'twitter_id', "all_text"],
                        "mysql": ["description", "profile_img",
                                  "followers", "location",
                                  "twitter_id", "friends",
                                  "created_date", "user_name",
                                  "status_count"]}
        self._parse_user(twitter_user=twitter_user)

        self.histgram_extractor = HistExtractor()

    def _parse_user(self, twitter_user):
        self.description = twitter_user.description
        self.profile_img = twitter_user.profile_image_url
        self.followers = twitter_user.followers_count
        self.location = twitter_user.location
        self.twitter_id = twitter_user.id
        self.friends = twitter_user.friends_count
        self.created_date = twitter_user.created_at
        self.user_name = twitter_user.name
        self.status_count = twitter_user.statuses_count
        self.status = [{
                           "id": elt.id,
                           "text": elt.text,
                           "retweet_count": elt.retweet_count,
                           "date": elt.created_at,
                           "retweeted": elt.retweeted
                       } for elt in twitter_user.timeline(count=200)]

    def get_data(self, db=None):
        assert db in [None, "mongo", "mysql"]
        result_dict = {
            "description": self.description,
            "profile_img": self.profile_img,
            "followers": self.followers,
            "location": self.location,
            "twitter_id": self.twitter_id,
            "friends": self.friends,
            "created_date": self.created_date,
            "user_name": self.user_name,
            "status_count": self.status_count,
            "status": self.status,
            "all_text": " ".join([elt["text"] for elt in self.status])

        }
        result_dict["histogram"] = self.histgram_extractor.get_histogram_from_string(result_dict["full_text"])
        result_dict["twentywords"] = [k for k, v in sorted(result_dict["histogram"].items(),
                                                           key=lambda x: x[1], reverse=True)][0:20]

        if not db:
            return result_dict
        else:
            return {k: v for k, v in result_dict.items() if k in self.db_cols[db]}
