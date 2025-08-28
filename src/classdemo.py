def myUpperCase(mystring):
    """this converts a string to all upper case.

    parameters
    ------
    mystring:str
        a string to be made all upper case
        
    returns
    -------
    str
        an upper case version of my string word
    """
    return mystring.upper()
if __name__ == "__main__":
    print("hello world")
    mstr = "this is a testing area for a function"
    ustr = myUpperCase(mstr)
    print(ustr)