import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

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
plt.xlabel("Number of Developers")
plt.tight_layout()
plt.show()

# still working 