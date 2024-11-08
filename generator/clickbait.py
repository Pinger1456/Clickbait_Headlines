"""
Clickbait Headline Generator, by Al Sweigart al@inventwithpython.com
A clickbait headline generator
for your soulless content farm website.
This code is available at
https://nostarch.com/big-book-small-python-programming
Tags: large, beginner, humor, word
"""

import random
from generators import Generator
from constants import when as when_options


def main():
    """Launches the Clickbait Headline Generator."""
    print('Clickbait Headline Generator')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            number_of_headlines = int(response)
            break  # Exit the loop once a valid number is entered.

    generator = Generator()
    for _ in range(number_of_headlines):
        clickbait_type = random.randint(1, 8)
        headline = ""
        if clickbait_type == 1:
            headline = generator.generate_are_millenials_killing_headline()
        elif clickbait_type == 2:
            headline = generator.generate_what_you_dont_know_headline()
        elif clickbait_type == 3:
            headline = generator.generate_big_companies_hate_her_headline()
        elif clickbait_type == 4:
            headline = generator.generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            headline = generator.generate_dont_want_you_to_know_headline()
        elif clickbait_type == 6:
            headline = generator.generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generator.generate_reasons_why_headline()
        elif clickbait_type == 8:
            headline = generator.generate_job_automated_headline()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    chosen_when = random.choice(when_options).lower()
    print(f'Post these to our {website} {chosen_when} or you\'re fired!')
