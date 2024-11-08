"""
This module contains the Generator class,
which generates various clickbait headlines.
"""
import random
from constants import (
    object_pronouns,
    possesive_pronouns,
    personal_pronouns,
    states,
    nouns,
    places,
    when
)


class Generator:
    """A class to generate various clickbait headlines."""

    def __init__(self):
        self.object_pronouns = object_pronouns
        self.possesive_pronouns = possesive_pronouns
        self.personal_pronouns = personal_pronouns
        self.states = states
        self.nouns = nouns
        self.places = places
        self.when = when

    @staticmethod
    def generate_are_millenials_killing_headline():
        """Generate a headline in the 'Are Millennials Killing...' format."""
        noun = random.choice(nouns)
        return f'Are Millennials Killing the {noun} Industry?'

    def generate_what_you_dont_know_headline(self):
        """Generate a 'What You Don't Know' format headline."""
        noun = random.choice(self.nouns)
        plural_noun = random.choice(self.nouns) + 's'
        chosen_when = random.choice(self.when)
        return (
            f'Without This {noun}, {plural_noun} '
            f'Could Kill You {chosen_when}'
        )

    def generate_big_companies_hate_her_headline(self):
        """Generate a 'Big Companies Hate Her' format headline."""
        pronoun = random.choice(self.object_pronouns)
        state = random.choice(self.states)
        noun1 = random.choice(self.nouns)
        noun2 = random.choice(self.nouns)
        return (
            f'Big Companies Hate {pronoun}! See How This {state} {noun1} '
            f'Invented a Cheaper {noun2}'
        )

    @staticmethod
    def generate_you_wont_believe_headline():
        """Generate a 'You Won't Believe' format headline."""
        state = random.choice(states)
        noun = random.choice(nouns)
        pronoun = random.choice(possesive_pronouns)
        place = random.choice(places)
        return (
            f'You Won\'t Believe'
            f'What This {state} {noun} Found in {pronoun} {place}'
        )

    @staticmethod
    def generate_dont_want_you_to_know_headline():
        """Generate a 'Don't Want You To Know' format headline."""
        plural_noun1 = random.choice(nouns) + 's'
        plural_noun2 = random.choice(nouns) + 's'
        return (
            f'What {plural_noun1} Don\'t Want '
            f'You To Know About {plural_noun2}'
        )

    @staticmethod
    def generate_gift_idea_headline():
        """Generate a 'Gift Idea' format headline."""
        number = random.randint(7, 15)
        noun = random.choice(nouns)
        state = random.choice(states)
        return f'{number} Gift Ideas to Give Your {noun} From {state}'

    @staticmethod
    def generate_reasons_why_headline():
        """Generate a 'Reasons Why' format headline."""
        number1 = random.randint(3, 19)
        plural_noun = random.choice(nouns) + 's'
        number2 = random.randint(1, number1)
        return (
            f'{number1} Reasons Why {plural_noun} Are More Interesting'
            f' Than You Think (Number {number2} Will Surprise You!)'
        )

    @staticmethod
    def generate_job_automated_headline():
        """Generate a 'Job Automated' format headline."""
        state = random.choice(states)
        noun = random.choice(nouns)

        i = random.randint(0, 2)
        pronoun1 = possesive_pronouns[i]
        pronoun2 = personal_pronouns[i]
        verb = 'Were' if pronoun1 == 'Their' else 'Was'

        return (
            f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} '
            f'Job. {pronoun2} {verb} Wrong.'
        )
