import pandas as pd

NATO_df=pd.read_csv('nato_phonetic_alphabet.csv')

NATO_dict ={row['letter']:row['code'] for (index, row) in NATO_df.iterrows()}

word = input('Enter a word to be returned in NATO-alphabet: ')

new_list = [letter.upper() for letter in word]

result = [NATO_dict[str(i)] for i in new_list]

print(result)
