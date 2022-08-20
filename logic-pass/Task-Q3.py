def char_counter(string,char):
    counter = 0;
    for i in string:
        if char == i:
            counter+=1;
    return counter        
def main():
    string = input("enter the string: ")
    char = input("enter the char: ")
    c = char.lower()
    s = string.lower()
    print(f"the char '{char}' was reapeated ({char_counter(s,c)}) times in the string '{string}'.")
    
if __name__ == "__main__":
    main()


