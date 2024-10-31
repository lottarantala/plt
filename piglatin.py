
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
            # Handle punctuation
            if not word[-1].isalpha():
                punctuation = word[-1]
                word = word[:-1]
            else:
                punctuation = ''
            
            if '-' in word:
                subwords = word.split('-')
                translated_subwords = [self.translate_subword(subword, vowels) for subword in subwords]
                translated_word = '-'.join(translated_subwords)
            else:
                translated_word = self.translate_subword(word, vowels)
            
            translated_words.append(translated_word + punctuation)
        
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

