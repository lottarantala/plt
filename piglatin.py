
class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        
        words = self.phrase.split()
        translated_words = []
        
        for word in words:
            if word[0] in 'aeiou':
                if word[-1] == 'y':
                    translated_word = word + 'nay'
                else:
                    translated_word = word + 'ay'
            else:
                first_vowel_idx = len(word)
                for i, char in enumerate(word):
                    if char in 'aeiou':
                        first_vowel_idx = i
                        break
                translated_word = word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay'
            translated_words.append(translated_word)
        
        return ' '.join(translated_words)

