import requests

token = '2619421814940190'
url = 'https://superheroapi.com/api/'

character_list = ['Hulk', 'Thanos', 'Captain America']

class Character():
    
    def __init__(self, name):
        self.name = name
    
    def get_intelligence(self):
        self.response = requests.get(url=f'{url}{token}/search/{self.name}')
        self.intelligence = self.response.json()['results'][0]['powerstats']['intelligence']
        return self.intelligence
    
def hwo_smartest(names):
        smartest = 'S.Tian'
        tmp_intel = 0
        for hero in character_list:
            tmp_hero = Character(hero)
            intelligence = int(tmp_hero.get_intelligence())
            if intelligence > tmp_intel:
                smartest = hero
                tmp_intel = intelligence
        return f'Самый умный из списка({", ".join(names)}): {smartest}. Его интеллект: {tmp_intel}'

if __name__== '__main__':
    print(hwo_smartest(character_list))
