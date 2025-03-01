import string

class PyTextAnalyzer:
    def process(self, text):
        self.__text = text
        self.__tokenized_text = self.__tokenize(text)
        count = self.words_count()
        print(f"amount of words: {count}")
        return self

    def get_words_list(self):
        if not self.__tokenized_text: raise ValueError("No words to get")
        return self.__tokenized_text   
    
    def get(self):
        if not self.__text: raise ValueError("No text to get")
        return self.__text   
    
    def map_words(self, fn):
        self.__tokenized_text = self.__map_recursive(fn, self.__tokenized_text, [])
        self.__text = ' '.join(self.__tokenized_text)
        return self
    
    def __map_recursive(self, fn, li, result):
        if not li:
            return result
        result.append(fn(li[0]))
        return self.__map_recursive(fn, li[1:], result)
    
    def filter_words(self, condition):
        self.__tokenized_text = self.__filter_recursive(condition, self.__tokenized_text, [])
        self.__text = ' '.join(self.__tokenized_text)
        return self
    
    def __filter_recursive(self, condition, li, result):
        if not li:
            return result
        if condition(li[0]):
            result.append(li[0])

        return self.__filter_recursive(condition, li[1:], result)
    
    def reduce_words(self, fn, acc=''):
        if not self.__tokenized_text: return acc 
        self.__text = self.__reduce_recursive(fn, self.__tokenized_text, acc)
        return self
    
    def __reduce_recursive(self, fn, li, acc):
        if not li:
            return acc
        return self.__reduce_recursive(fn, li[1:], fn(acc, li[0]))
    
    def __tokenize(self, text):
        text = self.__remove_punctuation(text)
        return text.split(" ")
    
    def __remove_punctuation(self, text):
        for char in string.punctuation:
            text = text.replace(char, '')
        return text
    
    def words_count(self):
        return len(self.__tokenized_text)
