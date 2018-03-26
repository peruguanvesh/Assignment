class StringCase():

    def getString(self):
        '''getString function takes input from console'''
        input_string = input("Enter input string:")
        return input_string

    def printString(self):
        '''printString return string in upper case'''
        return self.getString().upper()
