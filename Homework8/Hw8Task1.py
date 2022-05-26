import requests


class SuperHero:

    def __init__(self, name):
        self.name = name
        self.intelligence = self._get_intelligence()

    def _get_intelligence(self):
        resp = requests.get('https://superheroapi.com/api/2619421814940190/search/' + self.name)
        info = resp.json()
        for item in info['results']:
            if item['name'] == self.name:
                return int(item['powerstats']['intelligence'])

    def name_smartest(self, *others):
        for other in others:
            if not isinstance(other, SuperHero):
                return 'Можно сравнивать только с другим экземпляром класса SuperHero'
        highest_intelligence = self.intelligence
        smartest = self
        for other in others:
            if other.intelligence > highest_intelligence:
                highest_intelligence = other.intelligence
                smartest = other
        return f'Самый умный супергерой - это {smartest}'

    def __str__(self):
        return self.name

    @staticmethod
    def tell_smartest(heroes_list):
        for hero in heroes_list:
            if not isinstance(hero, SuperHero):
                return 'Можно сравнивать только экземпляры класса SuperHero'
        highest_intelligence = 0
        smartest = 0
        for hero in heroes_list:
            if hero.intelligence > highest_intelligence:
                highest_intelligence = hero.intelligence
                smartest = hero
        return f'Самый умный супергерой - это {smartest}'


if __name__ == '__main__':
    hulk = SuperHero('Hulk')
    captain_america = SuperHero('Captain America')
    thanos = SuperHero('Thanos')

    # Через метод объекта
    print(hulk.name_smartest(captain_america, thanos))

    # Через метод класса, если хотим передавать всех сравниваемых героев одним списком,
    # а не брать одного из них, а остальных применять к нему в методе
    hero_list = [hulk, captain_america, thanos]
    print(SuperHero.tell_smartest(hero_list))
