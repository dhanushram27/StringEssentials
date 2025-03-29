from collections import Counter

string = "Dhanush ram"
char_freq = Counter(string)
char_freq = Counter(c.lower() for c in string if c != ' ')

print(char_freq)
