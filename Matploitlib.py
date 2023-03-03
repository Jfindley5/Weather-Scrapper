#best top use dictionaryy type to create pandas dataframe
import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford",'Mercedes','ferrari'], #keys are car titles
  'passings': [3, 7, 2,5,10] #vaules are correspoding role of data, are list
}
myvar = pd.DataFrame(mydataset) #convert to a pandas datframe(object)
print(myvar)

#to create a csv file, write this myvar.to_csv('myvar.csv') beofore print statement
import pandas as pd
df = pd.read_csv('myvar.csv')
print(df)

import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford",'Mercedes','ferrari'],
  'passings': [3, 7, 2,5,10]
}
myvar = pd.DataFrame(mydataset)
myvar.to_csv('myvar.csv')
print(myvar)

#Access rows w/ loc funtion
import pandas as pd
df = pd.read_csv('myvar.csv')
print(df.loc[0])

#Give column names
import pandas as pd

data = {
  "calories": [420, 380, 390,410,550,770,200],
  "duration": [50, 40, 45,35,55,44,60]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3","day4","day5","day6","day7"])
print(df)

# treat numpy as a list
#this graph shows a simple line
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 8])
ypoints = np.array([0, 300])
plt.plot(xpoints, ypoints)
plt.show()

#barplot
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D","E"])
y = np.array([4, 8, 6, 10, 2])
plt.bar(x,y)
plt.show()

#barplot but horizontal becuase of the barh
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D","E"])
y = np.array([4, 8, 6, 10, 2])
plt.barh(x, y)
plt.show()

#to set color of the bar
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D","E"])
y = np.array([4, 8, 6, 10, 2])
plt.bar(x, y, color = "green")
plt.show()

#scatterplot
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2])
y = np.array([99,86,87,78,77,85,86])
plt.scatter(x, y)
plt.show()


#diffrent colors depending on what set theyre in
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,14,12,13,10,6])
y = np.array([100,105,84,105,90,100,79,112,91,80,85,103,97,89])
plt.scatter(x, y, color = '#88c999')
plt.show()

#chnage color of each dot
import matplotlib.pyplot as plt
import numpy as np
x = np.array([2,17,2,9,4,11,12,9,6])
y = np.array([111,86,103,87,94,78,77,85,86])
colors = np.array(["pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)
plt.show()

#sizes of dots
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6,8,12])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86,99,97])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75,900,530])
plt.scatter(x, y, s=sizes)
plt.show()

#Adjust the transparency of the dots w Alpha
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.show()

#pie chart value divided by the some of all values x/sum(x)
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()


#adding lables to the pie chart
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["BMW", "Ferrari", "Toyota", "Bugatti"]
plt.pie(y, labels = mylabels)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["BMW", "Ferrari", "Toyota", "Bugatti"]
plt.pie(y, labels = mylabels, startangle = 90)
plt.show()


#explox helps the widgets to standout
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["BMW", "Ferrari", "Toyota", "Bugatti"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()


#set the color with each wedge
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["BMW", "Ferrari", "Toyota", "Bugatti"]
mycolors = ["black", "cyan", "brown", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

#legend will help the use, guide them
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["BMW", "Ferrari", "Toyota", "Bugatti"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Cars:")
plt.show()






