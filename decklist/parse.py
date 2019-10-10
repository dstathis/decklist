def parse_deck_string(deckstr):



def parse_deck_file(deckfile):
    with open(deckfile, 'r') as deckf:
        decks = deckf.read()
    return parse_deck_string(decks)
