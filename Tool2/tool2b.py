#Importing required modules...
import time
import math

class clock:
    def __init__(self):
        #Variable for the time spent
        self.secondT = 0.0

    #Function for the timer:
    def timer(self, hours, minutes, seconds, opt):

        #Gives user's input in seconds
        self.secondsOnTimer = (3600 * hours) + (60 * minutes) + seconds

        #Loop runs until time runs out
        while self.secondsOnTimer - 1 > 0:
            #Takes a second off for a second
            time.sleep(1)
            self.secondsOnTimer -= 1
            #Converts time from seconds to hours, minutes and seconds
            self.hour = math.floor(self.secondsOnTimer / 3600)
            self.minute = math.floor(self.secondsOnTimer / 60)
            self.second =  self.secondsOnTimer - ((self.hour * 3600) + (self.minute * 60))

            #Prints time in hours, minutes and seconds if option is yes
            if opt == True:
                print("{} Hour(s), {} Minute(s), {} Second(s)".format(self.hour, self.minute, self.second))
        #Tells them the time is up
        if opt == True:
            print("Time's Up!")


    #Starts stopwatch
    def stopwatch(self):
        #Function to run infinitely
        while True:
            #For each 100 milliseconds passed:
            time.sleep(.1)
            #Increment value representing time passed to second Variable
            self.secondT += .1
            #Display time
            print("{:.1f} seconds".format((self.secondT)))

