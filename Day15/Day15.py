import itertools


class Ingredient:
    name = ""
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def score(self, amount):
        return [self.capacity * amount, self.durability * amount, self.flavor * amount, self.texture * amount], self.calories*amount

    def stats(self):
        return [self.capacity, self.durability, self.flavor, self.texture]

ingedients = dict()

def parseIngredient(line):
    name, rest = line.split(':')
    capacity, durability, flavor, texture, calories = rest.split(',')
    capacity = capacity[len("capacity "):].strip()
    durability = durability[len("durability "):].strip()
    flavor = flavor[len("flavor "):].strip()
    texture = texture[len("texture "):].strip()
    calories = calories[len("calories "):].strip()

    ingedients[name] = Ingredient(name, int(capacity), int(durability), int(flavor), int(texture), int(calories))

def scoreIngredients(ingredients, amounts):
    amountsList = list()
    # for amount in amounts:
    #     amountList = [x for x in amount for _ in range(len(ingedients.values()))]
    #     amountsList.append(amountList)

    highestScore = 0
    for amount in amounts:
        scoreList = list()
        calorieList = list()
        for x in range(len(amount)):
            score = ingredients.values()[x].score(amount[x])
            scoreList.append(score[0])
            calorieList.append(score[1])
       # print scoreList, calorieList

        summedScores = ([max(0, sum(c for c,d,f,t in scoreList)), max(0, sum(d for c,d,f,t in scoreList)), max(0, sum(f for c,d,f,t in scoreList)), max(0, sum(t for c,d,f,t in scoreList))])
        summedCalories = sum(c for c in calorieList)
        if summedCalories == 500:
            finalScore = 1
            for x in summedScores:
                finalScore *= x
            highestScore = max(highestScore, finalScore)

    print highestScore


#with open("TestInput.txt") as f:
with open("Input.txt") as f:
    for line in f.readlines():
        parseIngredient(line)

    highScore = 0
    amounts = itertools.ifilter(lambda a: sum(a) == 100, itertools.product(range(1, 101), repeat=len(ingedients)))

    scoreIngredients(ingedients, amounts)
