from random import choice
import os
path = os.path.dirname(os.path.abspath(__file__))
nouns_loc = os.path.join(path, 'nouns.txt')
adjectives_loc = os.path.join(path, 'adjectives.txt')
verbs_loc = os.path.join(path, 'verbs.txt')

def generate_nick_name():
    # Load word lists
    with open(nouns_loc) as noun_list:
        nouns = [line.rstrip() for line in noun_list]

    with open(adjectives_loc) as adjective_list:
        adjectives = [line.rstrip() for line in adjective_list]

    with open(verbs_loc) as verb_list:
        verbs = [line.rstrip() for line in verb_list]

    # Select random words
    adjective = choice(adjectives)
    verb = choice(verbs)
    noun = choice(nouns)

    # Randomly choose between adjective + noun or verb + noun
    if choice([True, False]):
        return f"{adjective} {noun}"
    else:
        return f"{verb} {noun}"

