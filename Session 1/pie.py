import matplotlib.pyplot as plt

categories = ["Category A", "Category B", "Category C", "Category D", "Category E"]
percentages = [25, 30, 15, 30, 15]

explode = [0, 0.1, 0, 0, 0.5]
colors = ["red", "blue", "orange", "green", "black"]

plt.pie(percentages, explode = explode, labels = categories, colors = colors, shadow = True)
plt.title("Percentage Destribution")
plt.legend(categories)
plt.show()
