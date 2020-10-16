import re
import csv
import json


class Minutes():

    def minutes_to_integer(self, running_time):
        if running_time == 'N/A':
            return None
        if isinstance(running_time, list):
            return int(running_time[0].split(" ")[0])
        else:
            return int(running_time.split(" ")[0])


class Money():

    amounts = r"thousand|million|billion"
    number = r"\d+(,\d{3})*\.*\d*"
    word_re = rf"\${number}(-|\sto\s|–)?({number})?\s({amounts})"
    value_re = rf"\${number}"

    def money_conversion(self, money):
        if money == "N/A":
            return None

        if isinstance(money, list):
            money = money[0]

        word_syntax = re.search(self.word_re, money, flags=re.I)
        value_syntax = re.search(self.value_re, money)

        if word_syntax:
            return self.parse_word_syntax(word_syntax.group())

        elif value_syntax:
            return self.parse_value_syntax(value_syntax.group())

        else:
            return None

    def parse_value_syntax(self, string):
        value_string = re.search(self.number, string).group()
        value = float(value_string.replace(',', ''))
        return value

    def parse_word_syntax(self, string):
        value_string = re.search(self.number, string).group()
        value = float(value_string.replace(",", ""))
        word = re.search(self.amounts, string, flags=re.I).group().lower()
        word_value = self.word_to_value(word)
        return value*word_value

    def word_to_value(self, word):
        value_dict = {"thousand": 1000,
                      "million": 1000000, "billion": 1000000000}
        return value_dict[word]


class Files():

    def save_data_json(self, title, data):
        with open(title, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def load_data_json(self, title):
        with open(title, encoding='utf-8') as file:
            return json.load(file)

    def save_data_csv(self, title, data):
        keys = data[0].keys()
        with open(title, 'w', newline='') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
