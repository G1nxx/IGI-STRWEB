import re

class Text_editor:
    def __init__(self):
        pass

    def count_sentences(self, text: str) -> (int|int|int|int):
        count_declarative = text.count('.') + text.count(";") + text.count(":\n")

        count_interrogative = text.count('?')
        count_exclamatory = text.count('!')
        count = count_declarative + count_exclamatory + count_interrogative
        return (count_declarative,
                count_interrogative,
                count_exclamatory,
                count)
    
    def count_words(self, text: str) -> int:
        count = 0
        for el in self.tokinize_words(text):
            if el == "":
                continue
            else:
                count += 1
        return count
    
    def tokinize_words(self, text: str) -> list[str]:
        text = text.replace(' - ', ' ')
        text = text.replace(' — ', ' ')
        text = text.replace("\n", ' ')
        list = text.split(' ')
        return list
    
    def tokinize_sentences(self, text: str) -> list[str]:
        text = text.replace(':\n', '. ')
        text = text.replace('?', '.')
        text = text.replace('!', '.')
        text = text.replace('\n', ' ')
        sentences = text.split('.')
        return sentences
    
    def find_len_of_text(self, text: str) -> int:
        symbols = "—-.,;\"'?!\n "
        text = text.replace(": ", '')
        for el in symbols:
            text = text.replace(el, '')
        return len(text)

# This class is made for executing different operations with data
class Executer:
    def __init__(self):
        self.text_editor = Text_editor()

    def read_from_file(self, _file_path: str) -> str:
        with open(_file_path, "r") as file:
            try:
                content = file.read()
            except FileNotFoundError:
                print("No such file")
            except Exception:
                print("Unknow error. Please, try again")
        return content
    
    def count_sentences(self, text: str) -> (int|int|int|int):
        return self.text_editor.count_sentences(text)

    def average_len_of_sentence(self, text: str) -> float:
        count = self.text_editor.count_sentences(text)[3]
        text_len = self.text_editor.find_len_of_text(text)
        return text_len / count
    
    def average_len_of_word(self, text: str) -> float:
        count = self.text_editor.count_words(text)
        text_len = self.text_editor.find_len_of_text(text)
        return text_len / count
    
    def count_words_in_sentences(self, text: str) -> list[(int, int)]:
        sentences = self.text_editor.tokinize_sentences(text)
        counter = 1
        val = []
        for el in sentences:
            if el == "":
                continue
            count = self.text_editor.count_words(el)
            val.append((counter,count))
            counter += 1
        return val
    
    def find_longest_word(self, text: str) -> (str|int):
        words = self.text_editor.tokinize_words(text)
        max_word = ""
        counter = 1
        pos = 1
        for word in words:
            if (len(max_word) < len(word)):
                max_word = word
                pos = counter
            counter += 1
        return (max_word, pos)
        

class Printer:
    def __init__(self):
        self.text_editor = Text_editor()

    def print_about_setences(self, counters: (int|int|int|int), average_len_sentence: float, average_len_word: float, word_count: list[(int, int)]):
        print("Count of all sentences: " + str(counters[3]))
        print("Count of declarative sentences: " + str(counters[0]))
        print("Count of interrogative sentences: " + str(counters[1]))
        print("Count of exclamatory sentences: " + str(counters[2]))
        print("Average length of sentence is: " + str(average_len_sentence))
        print("Average length of word is: " + str(average_len_word))
        for el in word_count:
            print("sentence № " + str(el[0]) + " \tCount of words: " + str(el[1]))

    def print_lowercase_words_and_punctuation(self, text: str):
        symbols = "()—-.,;\"'?!"
        words = self.text_editor.tokinize_words(text)
        for word in words:
            if len(word) == 0:
                continue
            if word[-1] in symbols:
                print("Punctuatinon: " + str(word[-1]))
                word = word[:-1]
                if len(word) == 0:
                    continue
            print("Word: " + word)

    def print_all_macs(self, text: str):
        words = self.text_editor.tokinize_words(text)
        fake_regex = "^..[:-].*$"
        true_regex = "([a-fA-F0-9]{2}(:)){5}[a-fA-F0-9]{2}$|([a-fA-F0-9]{2}(-)){5}[a-fA-F0-9]{2}$"
        c_all = 0
        c_not_fake = 0
        macs = []
        for word in words:
            if re.match(fake_regex, word):
                c_all += 1
            if re.match(true_regex, word):
                macs.append(word)
                c_not_fake += 1
        print("All macs: " + str(c_all))
        print("True macs: " + str(c_not_fake))
        for el in macs:
            print(el)

    def print_longest_word(self, word: (str|int)):
        print("The longest word is: " + word[0] + " with pos = " + str(word[1]))

    def print_every_even_word(self, text: str):
        words = self.text_editor.tokinize_words(text)
        checker = True
        for word in words:
            if word == "":
                continue
            if checker:
                print(word)
            checker ^= True
    
    def print_all_emojis(self, text: str):
        smile_regex = r"^((([:;]{1})-*){1}((\(+)|(\)+)|(\[+)|(\]+)))\ *$"
        words = self.text_editor.tokinize_words(text)
        emojis = []
        for word in words:
            if (re.match(smile_regex, word)):
                emojis.append(word)
        print("Count of emojis: " + str(len(emojis)))
        for el in emojis:
            print(el)


    

if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one")