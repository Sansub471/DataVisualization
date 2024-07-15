# Loading data from CSV without Pandas

from matplotlib import pyplot as plt
import numpy as np
import csv

# Separate lesson for counter
# Counter class for counting
from collections import Counter

plt.style.use("fivethirtyeight")

with open('data.csv') as csv_file:
    # Read as dictionary
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()
    
    #row = next(csv_reader)
    #print(row['LanguagesWorkedWith'].split(';'))
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))


# 15 most common languages
# print a list of tuples
# print(language_counter.most_common(15))

languages = []
popularity = []

for item in language_counter.most_common(15):
    lan, pop = item
    languages.append(lan)
    popularity.append(pop)

print(languages)
print(popularity)

# plt.bar(languages, popularity)
# plt.bar(x,y)
# When there is too many items, it's better to use horizontal chart

languages.reverse()
popularity.reverse()
# plt.barh(y,x)
plt.barh(languages, popularity)
plt.title("Most Popular Languages")
# plt.xlabel("Programming Languages")
plt.xlabel("Number of Developers")
plt.tight_layout()
plt.show()