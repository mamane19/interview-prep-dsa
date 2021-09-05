import collections
import unittest
def load_dictionary(path):
    """Parse a list of words, one per line."""
    with path.open() as fd:
        return frozenset(fd.read().splitlines())
def extract_letter(plate):
    """Returns a list with all the alphabet characters in a plate."""
    return [character for character in plate if character.isalpha()]
def is_valid_candidate(word, plate_letters):
    """Determines whether `word` could be a match for a given license plate."""
    # We need to keep duplicate letters, which means that we don't want to keep
    # *all* the words. Only those words that have *at least* the same number of
    # ocurrences for each letter as the license plate are useful to us.
    word_count = collections.Counter(word)
    letters_count = collections.Counter(plate_letters)
    for letter in letters_count:
        if not word_count[letter] >= letters_count[letter]:
            return False
    return True
def find_shortest_word(plate):
    """Find the shortest word with all the letters in a license plate."""
    # Map each letter to all candidate words that contain that letter.
    words = collections.defaultdict(set)
    plate_letters = extract_letter(plate.lower())
    for w in ALL_WORDS:
        if not is_valid_candidate(w, plate_letters):
            continue
    for letter in w:
        words[letter].add(w.lower())
    # Get the intersection of the sets corresponding to the letters in our plate.
    matches = set()
    for index, letter in enumerate(plate_letters):
        if index == 0:
            matches = words[letter]
        matches = matches.intersection(words[letter])
    # Sort before finding the minimum so that if 2+ words have the same length,
    # we return the first one lexicographically.
    return min(sorted(matches), key=len)