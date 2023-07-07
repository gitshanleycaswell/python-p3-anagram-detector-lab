class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        return [w for w in words if self._is_anagram(w)]
        
    def _is_anagram(self, word):
        return sorted(self.word) == sorted(word.lower()) and self.word != word.lower()

hello = Anagram('hello')
