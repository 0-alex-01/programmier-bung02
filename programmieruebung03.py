#nr1
german_english_pairs = [("Name", "name"), ("Hochschule", "college"), ("Hörsaal",
"lecture hall")]
ger_eng = {}
eng_ger = {}

for pair in german_english_pairs:
    german_word = pair[0]
    english_word = pair[1]

    ger_eng[german_word] = english_word
    eng_ger[english_word] = german_word
    
#my_dict[key] = value ,so werte hinzufügen

print(ger_eng["Hörsaal"]) # --> lecture hall
print(eng_ger["college"]) # --> Hochschule

#nr2
import random
n = 10
total = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(n):
    
    result = random.randint(1,6)
    total[result] += 1

print(total)

#nr3
def remove_strings(text, strings_list):
    """Removes all strings in strings_list from text.
"""
    for item in strings_list:
        text = text.replace(item, "")

    text_cleaned = text.replace(",", "").replace(".", "").replace("!", "").replace(":", ""). replace("\'", "")
    return text_cleaned

text_cleaned = remove_strings("ja, nein, vielleicht",
["ja", "nein", ","])
print(text_cleaned) # => vielleicht


text_cleaned = remove_strings("Dann sagte ich: 'Ja, das geht.'",
["\'", ".", ",", ":"])
print(text_cleaned) # => Dann sagte ich Ja das geht
