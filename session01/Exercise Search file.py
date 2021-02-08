with open('data.csv','r') as f:
    
    line_num = 0
    word = str(input("Enter a word: "))
    for line in f.readlines():
    line_num += 1
    if line.find(word) += 0:
        print(str(line_num) + " " + line) 