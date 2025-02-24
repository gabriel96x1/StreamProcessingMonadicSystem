import string

class PyTextAnalyzer:

    def __init__(self, text):
        self.text = text
        self.tokenized_text = self.__tokenize(text)

    def process(self, text):
        self.text = text
        self.tokenized_text = self.__tokenize(text)

        #print(self.tokens())

        #reduce = self.reduce(lambda acc, word: acc + f" wachaaa-> {word}")
        #print(f"resultado de reduce: {reduce}")

        #filter = self.filter(lambda element: 'e' in element)
        #print(f"resultado de filter: {filter}")

        #map = (self.map(lambda element: '/' + element + '/'))
        #print(f"resultado de map: {map}")

        count = self.words_count()
        print(f"amount of words: {count}")


    def tokens(self):
        return self.tokenized_text        
    
    def map(self, fn):
        return self.__map_recursive(fn, self.tokenized_text, [])
    
    def __map_recursive(self, fn, li, result):
        if not li:
            return result
        result.append(fn(li[0]))
        return self.__map_recursive(fn, li[1:], result)
    
    def filter(self, condition):
        return self.__filter_recursive(condition, self.tokenized_text, [])
    
    def __filter_recursive(self, condition, li, result):
        if not li:
            return result
        if condition(li[0]):
            result.append(li[0])

        return self.__filter_recursive(condition, li[1:], result)    
    
    def reduce(self, fn, acc=''):
        if not self.tokenized_text: return acc 
        return self.__reduce_recursive(fn, self.tokenized_text, acc)
    
    def __reduce_recursive(self, fn, li, acc):
        if not li:
            return acc
        return self.__reduce_recursive(fn, li[1:], fn(acc, li[0]))
    
    def __tokenize(self, text):
        text = text.lower()
        text = self.__remove_punctuation(text)
        return text.split(" ")
    
    def __remove_punctuation(self, text):
        for char in string.punctuation:
            text = text.replace(char, '')
        return text
    
    def words_count(self):
        return len(self.tokenized_text)
