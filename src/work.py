import math as mt
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
    sq = mt.sqrt(64)
    print(sq)
    mathlist = [0] * 11
    mathlist[0] = 2+2
    mathlist[1] = ((2+5)*4)
    mathlist[2] = 5**4
    mathlist[3] = 10/2
    mathlist[4] = 4/3
    mathlist[5] = 20//6
    mathlist[6] = 20%6
    mathlist[7] = 10/20
    mathlist[8] = 10//20
    mathlist[9] = 4%8
    mathlist[10] = 5**40
    print(mathlist)
    justalist = ["words","are","not","1n","h3r3"]
    print(justalist)
    listbutmore = [justalist]*2
    print(listbutmore)
    mathlist.insert(0,321)
    print(mathlist)
    