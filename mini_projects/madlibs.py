# ================================  MADLIB  ====================================
# ==============================================================================
# Create a simple story with user input details

import random

name = input("Name: ")
age = input("Age: ")
noun1 = input("Noun 1: ")
noun2 = input("Noun 2: ")
noun3 = input("Noun 3: ")
noun4 = input("Noun 4: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
verb3 = input("Verb 3: ")
verb4 = input("Verb 4: ")

story_1 = f"I am an 84-year-old {name} who stands 5'4” tall from the {noun1}-crazy state of Indiana. \
Recently, my {noun2} and I were {verb1} dinner at a local {noun3}. Our waiter was a young man, around 6'8”. \
Naturally, I {verb2} him if he played basketball. \
He looked down at me, replied, “Yes, I do,” and then asked me if I {verb3} {noun4}."

story_2 = f"My name is {name} and failed the first quarter of a class in middle {noun1}, so I {verb1} a fake report card. \
I did this every quarter that year. I forgot that they {verb2} home the end-of-year {noun2}, and my mom got it before I could {verb3} with my fake. \
She was PISSED—at the school for their error. The teacher also retired that year and had already {verb4} out his {noun3}, \
so they had to take my mother's “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” I've never told her the {noun4}."

story_3 = f"During my sophomore year of high school, we were {verb1} silent work and my history teacher said that we could listen to music but if it was too loud he would “{verb2} our {noun1}.” \
so I'm doing my work quietly with my music on low, and this obnoxious kid {verb3} next to me had his music really loud. I could hear it over my music but ignored it. \
My teacher thought it was me. So he comes up to me & ripped my BRAND NEW {noun2} headphones, looking ruthless. \
He suddenly {verb4} it was the guy next to me and he was completely embarrassed. He {verb2} in the next day with a new pair and an {noun3} taped to them. \
He couldn't look me in the eye for the rest of the {noun4}."

# Genereate random story with user inputs
story_list = [story_1, story_2, story_3]
print(random.choice(story_list))