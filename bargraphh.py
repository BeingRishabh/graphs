import matplotlib.pyplot as plt 

#x cordinates of left sides of the bar 
left = [1,2,3,4,5]

#heights of bar
height =[10,24,36,40,5]

#lables for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

#ploting a bar chart
plt.bar(left, height, tick_label = tick_label,
		width = 0.8, color = ['red', 'green'])

#naming the x axis
plt.xlabel('x - axis')

#naming the y axis
plt.ylabel('y - axis')

#plot title
plt.title('My First Bar Chart :]')

#function to show the plot
plt.show()