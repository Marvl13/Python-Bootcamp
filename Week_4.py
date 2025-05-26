# Task 1 - Simplified
filePath = "numbers.txt"
with open(filePath, 'w') as file:
    for num in range(1,51):
        file.write(str(num) + "\n")
with open(filePath, 'r') as file:
    sum = 0
    for line in file:
        print(line)
        sum += int(line)
    print(f"The sum of the numbers in the 'numbers.txt' file is {sum}")

# Task 1 - Advanced
filePath = "numbers.txt"
sum = 0
count = 0
numberRange = int(input("Enter the range for the numbers in the text file "))
max = numberRange
min = 1
with open(filePath, 'w') as file:
    for num in range(1,numberRange+1):
        file.write(str(num) + "\n")
with open(filePath, 'r') as file:
    for line in file:
        print(line)
        count += 1
        sum += int(line)
        

avg = sum / count
print(f"The sum of the numbers in the 'numbers.txt' file is {sum}.")
print(f"The average of the numbers in the file is {avg}.")
print(f"The max number in the file is {max}.")
print(f"The min number in the file is {min}.")

# Task 2
import random
def temperatureStats(list):
    min = random.choice(list)
    max = 0
    average = 0
    sum = 0
    for item in list:
        sum += item
        if min > item:
            min = item
        if max < item:
            max = item
    average = sum / len(list)
    return min, max, average
    # print(f"The minimum temperature is {min} {tempMeasurement}")
    # print(f"The maximum temperature is {max} {tempMeasurement}")
    # print(f"The average temperature is {average} {tempMeasurement}")
def temperatureSummary(list, tempMeasurement = 'Celsius'):
    values = temperatureStats(list)
    if tempMeasurement.title() == "Celsius":
        tempMeasurement = "degrees Celsius"
    elif tempMeasurement.title() == "Fahrenheit":
        tempMeasurement = "degrees Fahrenheit"
    print(f"The minimum temperature is {values[0]} {tempMeasurement}")
    print(f"The maximum temperature is {values[1]} {tempMeasurement}")
    print(f"The average temperature is {values[2]} {tempMeasurement}")

Temps = [25, 23, 43, 12, 24, 15]
temperatureSummary(Temps, "Celsius")

# Task 3
# You can determine product similarity by using a 0-1 scale that considers two main factors: category match (which can worth 60% of the similarity score) and price similarity (can worth 40%).

# A product in the same category as the target product receives 0.6 points automatically. If it's in different categories, it gets 0 points.

# For price similarity, if the product being compared has the same price as the target product, it. gets the full 0.4 points.  If their prices vary, then we do a simple calculation where we get the maximum price between the two products, and the difference between both prices. Next, use a formula like: (1 - (price difference / maximum price)) to give us the price similarity score. On getting the score, we multiply it by 0.4 to get the price point, i.e: 0.4 x (result from the formula).

# Now we have the category and price points, we sum them and associate/assign to the target product.

def calculateSimilarity(product_1, product_2):
    similarity1 = 0
    while True:
        try:
            if product_1['category'] == product_2['category']:
                similarity = 0.6
        except (NameError, IndexError, AttributeError):
            print("Please rename your category key to 'category, after which, run the code again.'")
            break
        
        try:
            if product_1['price'] == product_2['price']:
                similarity = 0.4
            else:
                maximum = max(product_1['price'],product_2['price'])
                if maximum == product_1['price']:
                    difference = product_1['price'] - product_2['price']
                else:
                    difference = product_2['price'] - product_1['price']
                price_similarity_score = 1 - (difference / maximum)
                pricePoint = 0.4 * price_similarity_score
        except (NameError, IndexError, AttributeError):
            print("Please rename your price key to 'price', after which, run the code again.'")
            break

    print(f"The similarity score is {sum(similarity,pricePoint)}")
