# https://takeuforward.org/data-structure/maximum-occurring-character-in-a-string/


s = 'takeuforward'
max_frequency = 0
most_common_character = ''

for char in s:
    frequency = s.count(char)
    if frequency > max_frequency:
        max_frequency = frequency
        most_common_character = char
print(most_common_character)
