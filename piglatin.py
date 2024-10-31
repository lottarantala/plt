from error import PigLatinError

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
        vowels = 'aeiou'


        for word in words:
            word, start_punctuation, end_punctuation = self.check_punctuation(word)
            
            if '-' in word:
                subwords = word.split('-')
                translated_subwords = [self.translate_subword(subword, vowels) for subword in subwords]
                translated_word = '-'.join(translated_subwords)
            else:
                translated_word = self.translate_subword(word, vowels)
            
            translated_words.append(start_punctuation + translated_word + end_punctuation)
        
        return ' '.join(translated_words)

    def translate_subword(self, word, vowels):
        if word[0] in vowels:
            if word[-1] == 'y':
                return word + 'nay'
            else:
                return word + 'ay'
        else:
            first_vowel_idx = len(word)
            for i, char in enumerate(word):
                if char in vowels:
                    first_vowel_idx = i
                    break
            return word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay'

    def check_punctuation(self, word):
        valid_punctuation_marks = ".,!?;:'()"
        start_punctuation = ''
        end_punctuation = ''

        if not word[-1].isalpha():
            end_punctuation = word[-1]
            if end_punctuation not in valid_punctuation_marks:
                raise PigLatinError("Invalid punctuation mark")
            word = word[:-1]

        if not word[0].isalpha():
            start_punctuation = word[0]
            if start_punctuation not in valid_punctuation_marks:
                raise PigLatinError("Invalid punctuation mark")
            word = word[1:]

        return word, start_punctuation, end_punctuation