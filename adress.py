from abc import ABC, abstractmethod


class LetterFrequencyCalculator(ABC):
    address = "weird.txt"

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(LetterFrequencyCalculator):
    def __init__(self, address):
        super().__init__(address)

    def calculateFreqs(self):
        frequencies = [0] * 26
        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        index = ord(char.lower()) - ord('a')
                        frequencies[index] += 1

        result_list = []
        for i in range(len(frequencies)):
            letter = chr(i + ord('a'))
            frequency = frequencies[i]
            if frequency > 0:
                result_list.append(f"{letter} = {frequency}")

        return result_list


class DictCount(LetterFrequencyCalculator):
    def __init__(self, address):
        super().__init__(address)

    def calculateFreqs(self):
        frequencies = {}
        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        frequencies[char] = frequencies.get(char, 0) + 1

        return frequencies


file_address = "weird.txt"

list_calculator = ListCount(file_address)
list_result = list_calculator.calculateFreqs()
print("List Count Frequencies:")
for item in list_result:
    print(item)

dict_calculator = DictCount(file_address)
dict_result = dict_calculator.calculateFreqs()
print("\nDictionary Count Frequencies:")
for key, value in dict_result.items():
    print(f'"{key}" 0 Updated Dict -> "{key}" {value}')
