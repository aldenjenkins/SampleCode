"""
Author: Alden Jenkins
Title: Priority Process Execution
Date: 4/11/16


Idea: Not all processes should be treated the same on a computer. Some processes 
      require more processing time to be efficiently completed than others. This program
      knows this and treats certain processes with a higher priority than others.
      Processes marked with an 'H' receive twice the processing time-slice of a low 
      priority process (marked with an 'L').


********* Text-file-to-be-read-from's contents: *******
3
P1,4,H
P2,5,L
P3,3,L
P4,7,H
P5,8,L
P6,9,L
P7,3,H
P8,2,H
P9,4,L
"""

# Given: A list of processes with execution times and priority ratings
# Find: A schedule of the processes using time slices

import queue
import random

# Open the file using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        # Notify the User of their bad input
        except IOError:
            print("Invalid filename, please try again ... ")
    return inFile

# Get the time slice value and the processes from the file into the queue
# Queue will contain a string with process ID and exec time separated by a comma
def getProcs(cpuQ):
    infile = openFile()
    # Get the first line in the file containing the time slice value
    line = infile.readline()                        
    # Strip the \n from the line and convert to an integer
    tslice = int(line.strip())                      
    # Loop through the file inserting processes into the queue
    for line in infile:                             
        proc = line.strip()
        cpuQ.put(proc)
    infile.close()
    return tslice, cpuQ

# Function to print the contents of the queue

def printQueue(tslice, cpuQ):
    print("The time slice is ", tslice, " \n The contents of the queue are: ")
    for i in range(cpuQ.qsize()):
        proc = cpuQ.get()
        cpuQ.put(proc)
        print(proc)


# Function to execute the processes in the queue

def scheduleProcs(tslice, cpuQ):
    while (cpuQ.empty() == 0):       
        t = tslice         
        # Get next process from queue
        proc = cpuQ.get()                           
        # Separate the process ID and the execution time from the process info
        PID, exectime, priority = proc.split(",")             
        # Convert exectime to an integer
        if priority == "H":
            t *= 2
        # Unecessary else, but good practice for application security 
        else:
            t = tslice
        exectime = int(exectime)                 
        print("Getting next process - Process ", PID," has ", exectime," instructions to execute and has a priority level of: ", priority)
        # Initialize the timer
        timer = 0          
                                 
        # While proc still has time in slice and still has code to execute
        while (timer < t) and (exectime > 0):  
            # Execute an instruction of process
            exectime -= 1                         
            # Count one tick of the timer
            timer += 1                       
            print("Executing instruction ", exectime," of process ", PID,".  Timer = ", timer)

        # If proc still has instructions to execute put it back in the queue
        if (exectime > 0):                          
            # Create string with new exec time and process ID
            proc = PID + "," + str(exectime)  + "," + priority      
            # Put the process back in the queue
            cpuQ.put(proc)                          
            print("Put process ", PID," back in queue with ", exectime," instructions left to execute\n")
        else:
            print("*** Process ", PID, " Complete ***\n")
    return

def main():
    # Create the scheduling queue
    cpuQ = queue.Queue()

    # Get the processes from the data file
    tslice, cpuQ = getProcs(cpuQ)

    # Print the queue
    printQueue(tslice, cpuQ)

    # Schedule the processes
    scheduleProcs(tslice, cpuQ)


main()
