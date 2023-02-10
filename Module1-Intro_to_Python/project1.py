"""
This file perform. 

Author: Alex Cornwall
   
"""
#imports argv module from sys
from sys import argv
 # Global variables that are associated with data collection regions
AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}

#Global variables that are associated with data collection types
COLUMNS = {
    0: 'Elevation',
    1: 'Aspect',
    2: 'Slope',
    3: 'Horizontal_Distance_To_Hydrology',
    4: 'Vertical_Distance_To_Hydrology',
    5: 'Horizontal_Distance_To_Roadways',
    6: 'Hillshade_9am',
    7: 'Hillshade_Noon',
    8: 'Hillshade_3pm',
    9: 'Horizontal_Distance_To_Fire_Points'
}

def pull_data(area_dict, cols):
    """This takes a list of float values from a previous action in the code (cols).
    It then appends that list into a dictionary specified by the function argument (area_dict).

    :param area_dict: requires a preconstructed dictionary (Data, Rawah, Neota, Comanche, Cache)
    :type area_dict: a dictionary within the file
    
    :param cols: calls a prefilled variable from the code.
    :type cols: list
    ...
    :return: each column in the list appended to its own column with is a dictionary.
    :rtype: appended dictionary
    """
    for c in area_dict.keys():
        area_dict[c].append(float(cols[c]))
            
def call_report(stats_repos, area_dict, Name):
    """[Summary]

    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]
    """
    #writing in my wilderness area name titles so there is a clear dilineation between the data sets
    stats_repos.write('--------------------------------------\n')
    stats_repos.write('{}\n'.format(Name))
    stats_repos.write('--------------------------------------\n')
    #Does the calculations for Minimum, Maximum, and the mean for each key in the inputed dictionary
    #I used the global Columns dictionary to specify column names associated with data in the file output
    #and a line break to create division between data sets
    for c in area_dict.keys():
        stats_repos.write("Minimum {}: {}\n".format(COLUMNS[c], min(area_dict[c])))
        stats_repos.write("Maximum {}: {}\n".format(COLUMNS[c], max(area_dict[c])))
        stats_repos.write("Mean {}: {}\n".format(COLUMNS[c], round((sum(area_dict[c])/len(area_dict[c])))))
        stats_repos.write("\n")    
    
def main():
    
    """This function ensures that the code is run when executed on a command line.

    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]
  
    """
    #establishing dictionaries to be used in the program: it'd be good to come back to this file and see if I can code this in.
    Data = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    
    Rawah = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    
    Neota = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    
    Comanche = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    
    Cache = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
        
    #creates a method to enter input on the command line.  specifically the data file I want processed
    script, file_name = argv
    #Opens the data file. It needs to be encoded to read properly.
    file = open(file_name, encoding="UTF-8")
    #creates and opens a file for writing to.
    stats_repos = open('./data/Data_summary.txt', 'w')    
    
    #Takes each line of the file one at a time
    for row in file:
        #splits the line at , delimiters into a list stored into cols until it loops back 
        cols = row.split(",")
        #checks the four columns in the list to determine what area the data was collected from.
        rawah, neota, comanche, cache = int(cols[10]), int(cols[11]), int(cols[12]), int(cols[13])
        #runs the pull_data function on each line as it comes through and appends it to the Data library
        #the Data library consists of all the data and write as Total at the end.
        pull_data(Data, cols)
        #the four columns utilized above are each binary 0/1. Only one of the columns will have a 1 value which signals location.
        #This if/elif statement checks the region code and sorts each line into the 4 specific dictionaries.
        if rawah == 1:
            pull_data(Rawah, cols)
            
        elif neota == 1:
            pull_data(Neota, cols)
            
        elif comanche == 1:
            pull_data(Comanche, cols)
             
        elif cache == 1:
            pull_data(Cache, cols)
 #next 5 line are for writing all the dictionaries with text region headers into Data_summary.txt
    call_report(stats_repos, Data, AREAS[0])
    call_report(stats_repos, Rawah, AREAS[1])
    call_report(stats_repos, Neota, AREAS[2])
    call_report(stats_repos, Comanche, AREAS[3])
    call_report(stats_repos, Cache, AREAS[4])
    
    
    
    #closing out both files i'm reading from and to
    stats_repos.close()
    file.close()


#works with the main function to run main() if the program is run from the command line.
if __name__ == "__main__":
    main()