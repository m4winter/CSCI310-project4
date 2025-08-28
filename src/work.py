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
    
    The program deals with math and other list type stuff.
    parameters
    ------
    nothing
        there is nothing that you enter that would be in the program.
    returns
    -------
    lists and other like it
        like it says it is just normal list and stuff like that, that are in the program.
    """
    return mystring.upper()
if __name__ == "__main__":
    print("hello world")
    mstr = "this is a testing area for a function"
    ustr = myUpperCase(mstr)
    print(ustr)
    print("1. 64 squared - below")
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
    print("2. Math List is below")
    print(mathlist)
    print("2.1. Mathlist with the first number is changed. - below")
    mathlist.insert(0,321)
    print("3. Words with numbers below")
    justalist = ["words","are","not","1n","h3r3"]
    print(justalist)
    print("How much words in list - below")
    print(len(justalist))
    print("3.1. List above times 2 - below")
    listbutmore = [justalist]*2
    print(listbutmore)
    print("3.2. one words from list")
    oneword = justalist[2]
    print(oneword)
    print("3.3. one words but in all caps")
    print(oneword.upper())
    print("4. Range lists with different variants")
    print(mathlist)
    list1 = list(range(10))
    print(list1)
    list2 = list(range(5,10))
    print(list2)
    list3 = list(range(20,0,-1))
    print(list3)