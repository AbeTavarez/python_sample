myFruitList=["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2]="orange"
print(myFruitList)

print("========exe.2=======")

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

print("=====exe.3========")

myFavoriteFruitDictionary = {
    "Adam": "apple",
    "Ben": "banana",
    "Penny": "pineapple"
}
print(myFavoriteFruitDictionary)
print((type(myFavoriteFruitDictionary)))

print(myFavoriteFruitDictionary["Adam"])
print(myFavoriteFruitDictionary["Ben"])
print(myFavoriteFruitDictionary["Penny"])

t= ("a", "a")
print(type(t))
print(t)

for k, v in myFavoriteFruitDictionary.items():
    print(k,v)

word_bank="word bank"
for letter in word_bank:
    print(letter)