from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json


class TestTweetsApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.usuarios_cientistas()

    def test_tweets_api(self):
        vitor, osvaldo, bia, anon = Client(), Client(), Client(), Client()
        vitor.force_login(User.objects.get(username='@vitor'))
        osvaldo.force_login(User.objects.get(username='@osvaldo'))
        bia.force_login(User.objects.get(username='@bia'))
        self._follow(vitor, '@bia')
        self._follow(osvaldo, '@bia')
        self._follow(osvaldo, '@vitor')
        self._follow(vitor, '@osvaldo')
        self._unfollow(vitor, '@osvaldo')
        self._tweet(bia, 'Penso, logo existo!')
        self._tweet(vitor, 'oi')
        self._tweet(vitor, 'tudo bom?')
        self._tweet(osvaldo, 'E=mc2')
        self._tweet(osvaldo, 'xau')
        self._assert_tweets_home(bia, ['Penso, logo existo!'])
        self._assert_tweets_home(vitor, ['tudo bom?', 'oi', 'Penso, logo existo!'])
        self._assert_tweets_home(osvaldo, ['xau', 'E=mc2', 'tudo bom?', 'oi', 'Penso, logo existo!'])
        self._assert_tweets_home(anon, ['xau', 'E=mc2', 'tudo bom?', 'oi', 'Penso, logo existo!'])
        self._assert_tweets_user(anon, '@osvaldo', ['xau', 'E=mc2'])
        self._assert_tweets_user(vitor, '@osvaldo', ['xau', 'E=mc2'])

    def _follow(self, client, username):
        r = client.post('/api/follow', {'username': username})
        self.assertEquals(200, r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _unfollow(self, client, username):
        r = client.post('/api/unfollow', {'username': username})
        self.assertEquals(200, r.status_code)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _tweet(self, client, text):
        r = client.post('/api/tweet', {'text': text})
        self.assertEquals(200, r.status_code)
        tweet = json.loads(r.content.decode('utf-8'))
        self.assertEquals(text, tweet['text'])

    def _assert_tweets_home(self, client, expectedtweets):
        r = client.get('/api/list_tweets')
        self.assertEquals(200, r.status_code)
        tweets = json.loads(r.content.decode('utf-8'))
        actualtweets_texts = [t['text'] for t in tweets['tweets']]
        self.assertEquals(actualtweets_texts, expectedtweets)

    def _assert_tweets_user(self, client, username, expectedtweets):
        r1 = client.get('/api/get_user_details', {'username': username})
        r2 = client.get('/api/list_tweets', {'username': username})
        self.assertEquals(200, r1.status_code)
        self.assertEquals(200, r2.status_code)
        userdetails = json.loads(r1.content.decode('utf-8'))
        tweets = json.loads(r2.content.decode('utf-8'))
        actualtweets_texts = [t['text'] for t in tweets['tweets']]
        self.assertEquals(actualtweets_texts, expectedtweets)

        for k in ['username', 'avatar', 'description', 'ifollow']:
            self.assertIsNotNone(userdetails[k])
