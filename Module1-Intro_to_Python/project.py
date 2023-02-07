file = open("./data/covtype.data.gz")

AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}

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

def stats(cx):
    '''
    This function allows you to calculate min, max and mmean values of a list of integers
    
    Parameters
    ----------
    cx : int
        List of integers
  
    Returns
    -------
    minx : int
        Minimun value
    maxx : int 
        Maximun value
    meanx : int
        Mean value
    '''
    minx = round(min(cx),2) # Use Python pre-made function for minimun value in a list
    maxx = round(max(cx),2) # Use Python pre-made function for maximun value in a list
    meanx = round(sum(cx)/len(cx),2) # Calculate mean as the sum of all the values in the list divided by the lenght of the list
    # Note I use the round function to control for signifucant digits printed
    return minx,maxx,meanx

from sys import argv
script, file_name = argv
file = open(file_name)
