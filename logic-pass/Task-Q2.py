def prime_numbers_detector():    
        print("please enter a starting and ending for the range so we find the prime numbers in it.")
        start = int(input("enter the beginning of the range: "))
        end = int(input("enter the ending of the range: "))
        if start < end:
           print(f"prime numbers between {start} to {end}: ")
           for i in range(start,end+1):     
            if i>1:        
                for j in range (2,i):
                    if (i%j) == 0:
                        break;
                else: 
                    print(i,end=" ")
        elif (start == end):
            print(f"the range from ({start} to {end}) doesn't exist.")
        else:
            y = start
            start = end
            end = y
            print(f"prime numbers between {start} to {end}: ")
            for i in range(start,end+1):
             if i>1:
                for j in range(2,i):
                    if (i%j) == 0:
                        break; 
                else:
                    print(i,end=" ")           
def main():
    prime_numbers_detector()

if __name__ == "__main__":
    main()    