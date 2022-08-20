def CharRemover(s,char):
    if char not in (s):
        return "the string does not contain the giving character."
    NewString = s.replace(char,"")
    return NewString.lower()

    
def main():
    s,char = input("enter the string: "),input("enter the unwanted char: ")
    s = s.upper()
    char = char.upper()
    print(CharRemover(s,char))

if __name__ == "__main__":
    main()    