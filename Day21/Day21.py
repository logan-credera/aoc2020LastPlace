# You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.
#
# You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.
#
# Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.
#
# For example, consider the following list of foods:
#
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)
# The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.
#
# The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.
#
# Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?


data = open("input.txt", "r")
# copy the data to a list
lst = data.read().split("\n")[:-1]

datadict = {}
for line in lst:
    ingredients = line.split('(')[0][:-1].split(' ')
    allergens = line.split('contains ')[1].split(')')[0].split(', ')

    for a in allergens:
        if a not in datadict.keys():
            datadict[a] = ingredients
        else:
            keep = []
            for i in ingredients:
                if i in datadict[a]:
                    keep.append(i)
            datadict[a] = keep
print(datadict)


possible = []
for k in datadict.keys():
    for i in datadict[k]:
        if i not in possible:
            possible.append(i)
print(possible)

count = 0
for line in lst:
    ingredients = line.split('(')[0][:-1].split(' ')
    for i in ingredients:
        if i not in possible:
            count += 1
print(count)


# Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.
#
# In the above example:
#
# mxmxvkd contains dairy.
# sqjhc contains fish.
# fvjkl contains soy.
# Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.
#
# Time to stock your raft with supplies. What is your canonical dangerous ingredient list?

# {'wheat': ['znrzgs', 'dhfng'],
# 'shellfish': ['dhfng', 'znrzgs', 'nqbnmzx'],
# 'eggs': ['pgblcd', 'nqbnmzx'],
# 'sesame': ['dstct', 'nqbnmzx', 'pgblcd', 'dhfng'],
# 'dairy': ['dhfng'],
# 'soy': ['znrzgs', 'nqbnmzx', 'ntggc'],
# 'peanuts': ['nqbnmzx', 'dstct', 'dhfng', 'xhkdc', 'ghlzj'],
# 'fish': ['znrzgs', 'nqbnmzx', 'ntggc', 'xhkdc']}
# ['znrzgs', 'dhfng', 'nqbnmzx', 'pgblcd', 'dstct', 'ntggc', 'xhkdc', 'ghlzj']

ans = []
while len(ans) < len(possible):
    for k in datadict.keys():
        if len(datadict[k]) == 1:
            temp = datadict[k][0]
            ans.append([k, temp])
            for j in datadict.keys():
                if temp in datadict[j]:
                    datadict[j].remove(temp)
            del datadict[k]
ans.sort(key=lambda x:x[0])
print([a[1] for a in ans])

# dhfng,pgblcd,xhkdc,ghlzj,dstct,nqbnmzx,ntggc,znrzgs
