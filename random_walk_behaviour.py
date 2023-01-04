"""
    Made By: Marwan Alhindi
    Created On: 23 July 2022
    From: Python Crash Course
    The purpose of this file is to generate a random walk behaviour by using classes and also matplotlib. You practiced in this file how to use classes and also how to interact with these classes with other libraries Eg. using the class with matplotlib library. You learnt how to plot, stylise the plot, and also how to plot multiple graphs using a while loop.

    The Data Visualization project starts in Chapter 15, in which you'll learn to generate data and create a series of functional and beautiful visualizations of that data using Matplotlib and Plotly. Chapter 16 teaches you to access data from online sources and feed it into a visualization package to create plots of weather data and a map of global earthquake activity. Finally, Chapter 17 shows you how to write a program to automatically download and visualize data. Learning to make visualizations allows you to explore the field of data mining, which is a highly sought-after skill in the world today.
"""

import matplotlib.pyplot as plt
from random import choice

#style of the plots
plt.style.use('classic')

class RandomWalk:
    """ 
        This class will generate a random movement that start from (0,0).
        It uses the choice method from random to make a random movement either in x axis, y axis or both
    """

    def __init__(self,num_steps= 5000):
        """ 
            Three atributes:
            1- x-coordinate of each step
            2- y-coordinate of each step
            3- the number of steps the user want (default 5000)
        """

        self.num_steps= num_steps
        self.x_axis= [0]
        self.y_axis= [0]
    
    def fill_walk(self):
        """
            This method is to fill the x and y coordinate with steps based on what the choice method from random module.
        """

        while len(self.x_axis) < self.num_steps:

            x_direction= choice([-1,1])
            x_steps= choice([0,1,2,3,4])
            x_movement= x_direction * x_steps

            y_direction= choice([-1,1])
            y_steps= choice([0,1,2,3,4])
            y_movement= y_direction * y_steps

            if (x_steps== 0) and (y_steps== 0):
                continue

            self.x_axis.append(self.x_axis[-1] + x_movement)
            self.y_axis.append(self.y_axis[-1] + y_movement)
    
    def printing_xy_coordinate(self):
        """
            This method is to print to the user the x and y coordinate that has been made from the fill_walk method.
        """
        
        print(self.x_axis)
        print('\n')
        print(self.y_axis)

active = True
while active:
    #this while loop generates random walks as long as the user does not quit the program. Close the figure to generate a new one by typing anything else than n.

    user_decision = input('Please provide y/n to keep running the program: ')
    if user_decision == 'n':
        active = False

    #instance of a class and generating x,y steps
    random_walk= RandomWalk(500000)
    random_walk.fill_walk()

    #plotting
    fig,ax = plt.subplots(figsize= (15,9))

    #title and labels
    ax.set_xlabel('x steps',fontsize= 20)
    ax.set_ylabel('y steps',fontsize= 20)
    ax.set_title('Random Walk Behaviour',fontsize= 20)

    #plotting first and last point
    plt.scatter(random_walk.x_axis,random_walk.y_axis,c= random_walk.y_axis,cmap=plt.cm.Reds, edgecolors= 'none')
    plt.scatter(random_walk.x_axis[-1],random_walk.y_axis[-1],s= 200,c= 'blue',edgecolors= 'none')
    plt.scatter(0,0,s= 200,c= 'blue',edgecolors= 'none')

    plt.show()
    #incase you want to save the plot instead of showing it:
    # plt.savefig('randomWalk.png')

