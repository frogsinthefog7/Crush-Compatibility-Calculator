
numbers = []

def calc(names_list):

    letter_count = 1

    length = names_list.len()

    if length == 0:
        return numbers

    for i in range(0, length+1):
        if names_list[0] == names_list[i]:
            letter_count += 1
            names_list.pop[i]

    numbers.append[letter_count]
    names_list.pop[0]
    
    




def main():

    YourName = str(input("What is your name: "))
    TheirName = str(input("What is your crush's name: "))



    YourName = YourName.lower()
    TheirName = TheirName.lower()

    print(YourName , TheirName)

    names_list = YourName, TheirName
    calc(names_list[0])    
    
    

main()
