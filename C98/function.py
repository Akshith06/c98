def countWordsFromFile():
    filename=input("Enter the file name ")
    n=0
    file= open(filename,'r')
    for line in file: 
       w=line.split()
       n=n+len(w)
    print("number of words")
    print(n)

countWordsFromFile()