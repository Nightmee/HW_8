#Зарезервовані слова list, dict, 1tuple, @set, Python Game

number1 = '5'
number2 = 6
print(type(number1))
print(type(number2))
print(id(number1))
print(id(number2))

print(int(number1) + number2)
print(number2 - int(number1))

num_1 = 12
num_2 = 30
num_3 = 3,14

print(type(str(num_1)))
print(type(str(num_2)))
print(type(str(num_3)))

name = 'Tymofii'
last_name = 'Gorlachov'
year = '2007'
country = 'Ukraine'
pet = 'cat'
book = 'How to open a restaurant'
play = 'Minecraft'
hobby = 'Programming'
eat = 'sushi'

print(f"\tHello i'm a {name, last_name},I was born in {year} I'm from {country}.\nMy favorite pet is {pet} I also like to read sometimes, \none of my favorite books is {book} \nWhat about games i like to play {play}, hobby is {hobby} \nEat hm i like almost all but {eat} is perfect")

alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

Freedom1 = alphabet[10] + alphabet[35] + alphabet[9] + alphabet[9] + alphabet[7] + alphabet[29] + alphabet[25]

print(f"{Freedom1}")

hope = alphabet[15] + alphabet[29] + alphabet[31] + alphabet[9]
that = alphabet[39] + alphabet[15] + alphabet[1] + alphabet[39]
you = alphabet[49] + alphabet[29] + alphabet[41]
used = alphabet[41] + alphabet[37] + alphabet[9] + alphabet[7]
HTML = alphabet[14] + alphabet[38] + alphabet[24] + alphabet[22]

print(f"I {hope} {that} {you} {used} {HTML}")