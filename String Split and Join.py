
def split_and_join(line):
    words = line.split() 
    *word_list, = words  
    result = "-".join(word_list)
    return result  

if __name__ == '__main__':
    line = input()  
    result = split_and_join(line) 
    print(result)  
