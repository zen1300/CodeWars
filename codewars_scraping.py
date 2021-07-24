import requests
from bs4 import BeautifulSoup


class User:
    def __init__(self, name, pos, clan, honor):
        self.name = name
        self.position = pos
        self.clan = clan
        self.honor = honor


class Leaderboard:
    def __init__(self):
        self.positions = {}
        self._fill_positions()

    def _fill_positions(self):
        r = requests.get('https://www.codewars.com/users/leaderboard')
        soup = BeautifulSoup(r.text)
        rows = soup.find_all('tr')
        index = 1
        for user in rows:
            if index < 500:
                try:
                    name = user['data-username']
                    clan = user.contents[2].text
                    honor = int(''.join(user.contents[3].text.split(',')))
                    self.positions[index] = User(name, index, clan, honor)
                    index += 1
                except KeyError:
                    pass

c = Leaderboard()