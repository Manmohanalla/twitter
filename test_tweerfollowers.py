import unittest

from tweetfollowers import TwitterFollowers,TwitterUserKeyword
import tweetfollowers as t


class TwythonAuthTestCase(unittest.TestCase):
    
    def test_no_followers(self):
        # All followers with screen_name
        result = twitter.get_followers('ManmohanAlla')
        # True if empty list as ManmohanAlla has no followers
        self.assertEqual([], result)
    
    def test_keys(self):

        self.assertEqual('-----------',t.consumer_key) 
        self.assertEqual('-----------',t.consumer_secret)
        self.assertEqual('-----------------------',t.auth_token)
        self.assertEqual('-----------',t.auth_token_secret)

    def test_invalid_user(self):
        # All followers with unexisting screen_name
        result = twitter.get_followers('-ManmohanAlla')
        # Ok if exception is raised 
        self.assertRaises(result)
        # All tweets with unexisting screen_name
        result = keyword.tweet_keyword('-ManmohanAlla','word')
        # Ok if exception is raised 
        self.assertRaises(result)

    def test_empty_string(self):
        # All followers with empty screen_name
        result = twitter.get_followers('')
        self.assertEqual([],result)
        # All tweets with empty screen_name
        result = keyword.tweet_keyword('','word')
        self.assertEqual([],result)
        # passing empty string to word
        result = keyword.tweet_keyword('MakeThunder','')
        # All tweets
        tweets = keyword.tweets('MakeThunder')
        expected = [i['text'] for i in tweets]
        # Equals if result returns all tweets
        self.assertEqual(expected,result)

        result = keyword.tweet_keyword('','')
        # true if result is empty list
        self.assertEqual([],result)

if __name__ == '__main__':
    
    keyword = TwitterUserKeyword()
    twitter = TwitterFollowers()
    unittest.main()