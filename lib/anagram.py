# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word 
    
    @word.setter
    def word(self, word):
        if word == word:
            self._word = word.lower()

    def match(self, word_list):
        candidates = []
        for n in word_list:
            if sorted(n) == sorted(self.word):
                candidates.append(n)
        return candidates
