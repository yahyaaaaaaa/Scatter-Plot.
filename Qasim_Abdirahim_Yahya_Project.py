import numpy as xared
import matplotlib.pyplot as british

what_is_your_number = int(input("Enter number of data: "))  # put howamny datas you wanna graph
x = xared.arange(what_is_your_number)
y = []
for i in range(0, what_is_your_number):
    value = int(input("Enter value: "))  # the numbers in our data.
    y.append(value)
british.title('scatter plot')
y = xared.array(y)
british.scatter(x, y)
british.plot(x, y, color='black')
british.show()
