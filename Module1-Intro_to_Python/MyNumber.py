"""
This program prints the int 2 then preforms addition and subtraction from a provided variable.
If used as a module it will print the int provided.

Only integers should be used with this file.


"""
class MyNumber:
    """
    This class stores a number and performs basic mathematics on the number.
    
    Attributes
    ----------
    x : int
        The number that this class works with.

    Methods
    -------
    print():
        Prints the number    
    add(y):
        Adds the number in y to the number of this object.
    subtract(y):
        Subtacts the number in y to the number of this object.
    """
    
    def __init__(self, x):
        """
        Function checks to make sure value provided is an integer
        
        Parameters
        ----------
            int: 
        Returns
        -------
            raises an exception if input is not and int
            If it is an int it saves it to self.x
        """
        if not type(x) == int:
            raise Exception("Please provide an integer when using the MyNumber object")
        self.x = x

    def print(self):
        """
        Function utilizes a formated print function
        
        Usage
        -----
        print(variable)
        
        Returns
        -------
        A print of the variable contents
        """
        print("The number is: {}".format(self.x))
        
    def add(self, y):
        """
        This function adds a provided integer to the variable associated with the function
        and then writes the sum as the same variable creating an additive variable.
        
        Usage
        -----
        variable.add(int)
        
        Returns
        -------
        A sum of the two variables.
        """
        self.x = self.x + y
        

    def subtract(self, y):
         """
        This function subtracts a provided integer to the variable associated with the function
        and then writes the sum as the same variable creating an additive variable.
        
        Usage
        -----
        variable.subtract(int)
        
        Returns
        -------
        A subtraction of the two variables.
        """
        self.x = self.x - y


def main():
    xval = 3
    yval = 2
    number = MyNumber(2)
    number.print()
    number.add(yval)
    number.print()
    number.subtract(yval)
    number.print()

if __name__ == "__main__":
    main()