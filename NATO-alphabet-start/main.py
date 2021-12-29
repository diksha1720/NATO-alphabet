import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


user_input = input("Enter a word :").upper()
result = [data_dict[c] for c in user_input]
print(result)


