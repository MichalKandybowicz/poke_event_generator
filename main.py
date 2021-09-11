
import random
import secrets


class RandomEvent:
    def __init__(self, dzicz: str, pokemon: str, choices=3,):
        self.pokemon = pokemon
        self.action_choices = choices
        self.texts()
        self.random_part_1 = random.choice(self.part_1[dzicz])
        self.random_part_2 = random.choice(self.part_2)
        self.random_part_3 = random.choice(self.part_3)
        self.random_part_4 = random.choice(self.part_4[dzicz])

    def print_event(self):
        print(self.random_part_1, self.random_part_2, self.random_part_3, self. random_part_4, '\n')
        actions = random.sample(self.player_reacton.keys(), k=self.action_choices)
        for action in actions:
            random_reaction = random.choice(self.player_reacton[action])
            print(action, '-', random_reaction)

    def texts(self):
        self.part_1 = {
            "łąka": [
                'Idąc ścierzką', 'Podczas wycieczki'
            ],
            "las": [
                'Idąc wąską, krętą, ścierzką', 'Między skałami w głębi lasu', 'Podczas wycieczki'
            ],
            "tunel": [
                'Idąc ścierzką w kanionie szukając wejścia do starych jaskiń',
                'W ciemnym zaułku daleko od szlaku',
                'Podczas wycieczki po tunelach'
            ],
            "miasto": ['Idąc ścierzką', 'W ciemnym zaułku', 'Podczas wycieczki'],
            "wyspy": ['Płynąc łodzią', 'Idąc w zdłoż plarzy', 'Spacerując po brzegu wyspy'],
        }
        self.part_2 = [
            'widzisz',
            'spotykasz',
            'zauważasz',
            'dostrzegasz',
            'dosięgasz wzrokiem',
            'spostrzegasz',
            'widzisz z oddali',
        ]
        self.part_3 = [
            f'obcego trenera,',
            f'nieznanego {self.pokemon}a,',
            f'niewielkiego {self.pokemon}a,',
            f'dzikiego {self.pokemon}a',
        ]

        self.part_4 = {
            "łąka": [
                'w trakcie posiłu, widocznie też cię zobaczył bo podniósł głowę,',
                'stojącyą w wysokiej trawie bacznie obserwując.'
            ],
            "las": [
                'skrytego w cieniu.',
                'idącego między drzewami w niewielkiej odległości od ciebie,',
            ],
            "tunel": [
                'stojącego do ciebie plecami na środku jaskini.',
                'śpiącego w szerokim tunelu.',
            ],
            "miasto": [
                'idącego powoli szeroką aleją.',
                'siedzącego na środku parku.'
            ],
            "wyspy": [
                'płynącego w twoją stronę.',
                'siedzącego między skałami na plarzy.',
            ],
        }

        self.player_reacton = {
            'Starasz się zblirzyć': [
                'Niestety ten widząc cię odrazu ucieka gubiąc {przedmiot}',
                'Niestety ten widząc cię odrazu ucieka goniąc go twój pokemon wpada w pułapkę i traci punkty zdrowia',
                'Przeciwnik atakuje, wychodząc z starcia zwycięsko zyskuje {exp}',
                'Przeciwnik atakuje, dzięki wygranej twoja dróżyna zyskuję przywiązanie',
                'Przeciwnik atakuje a twój pokemon staje w twojej obronie, niestety przegrywa tracąc {hp}',
                ],
            'Ukrywasz się': [
                'Biegnąc do kryjówki znajdujesz plecak a w nim {przedmiot}',
                'Potykasz się i gubisz 100 yenów'
                'Niestety zbyt długo siedzisz w kryjówce, tracisz 10 punktów akcji',
                'Niestety zbyt długo siedzisz w kryjówce, twoje pokemony niecierpliwią się i tracą nieco przywiązania',
                'Twoje pokemony zniesmaczone twoiją postawą tracą przywiązanie',
                'Po chwili niebezpieczeństwo mija wychodzisz z ukrycia i idziesz dalej'
            ],
            'Omijasz szerokim łukiem': [
                'Niestety skupiony na obserwowaniu nie patrzysz pod nogi potykasz się i tracisz przez to {pa}',
                'Droga była dłuższa ale dzięki temu znajdujesz drogocenny kamień który sprzedasz za {yeny}',
                'Droga była dłuższa ale dzięki temu po drodze napotykasz na {przedmiot}'
            ],
            #

        }


def main(dzicz, pokemon):
    for i in range(10):
        wyprawa = RandomEvent(dzicz, pokemon)
        wyprawa.print_event()
        print('----------------------')



if __name__ == '__main__':
    main('tunel', 'Bulbazaur')

