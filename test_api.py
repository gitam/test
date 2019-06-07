
from unittest import TestCase # unittest framewrok
import pprint
#import urllib3
import spotipy


class BaseSettings(TestCase):

    creep_urn = 'spotify:track:3HfB5hBU0dmBt8T0iCmH42'
    creep_id = '3HfB5hBU0dmBt8T0iCmH42'
    creep_url = 'http://open.spotify.com/track/3HfB5hBU0dmBt8T0iCmH42'
    el_scorcho_urn = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'
    el_scorcho_bad_urn = 'spotify:track:0Svkvt5I79wficMFgaqEQK'
    pinkerton_urn = 'spotify:album:04xe676vyiTeYNXw15o9jT'
    weezer_urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
    pablo_honey_urn = 'spotify:album:6AZv3m27uyRxi8KyJSfUxL'
    radiohead_urn = 'spotify:artist:4Z8W4fKeB5YxbusRsdQVPb'
    angeles_haydn_urn = 'spotify:album:1vAbqAeuJVWNAe7UR00bdM'

    def setUp(self):
        # install(level='DEBUG')
        # cls.ApiURL = 'https://api.spotify.com/v1/search'
        urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
        self.spotify = spotipy.Spotify()

    # @staticmethod
    # def test_opening_url(self):
    #     http = urllib3.PoolManager()
    #     r = http.request('GET', 'https://api.spotify.com/v1/search?q=tania%20bowra&type=artist')
    #     print(r.status)
    #     print(r.data)

    def test_artist_urn(self):
        artist = self.spotify.artist(self.radiohead_urn)
        self.assertTrue(artist['name'] == 'Radiohead')


if __name__ == '__main__':
    unittest.main()