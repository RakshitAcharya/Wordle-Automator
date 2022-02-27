def creating_list():
    allowed_guesses = []
    with open("allowed guesses.txt", "r") as file:
        allowed_guesses.append(file.read())

    allowed_guesses =  allowed_guesses[0].split("\n")
    
    answers = []
    with open("possible answers.txt", "r") as file:
        answers.append(file.read())

    answers =  answers[0].split("\n")

    return answers , allowed_guesses 

def main():
    answers ,allowed_guesses = creating_list()
    chances = 1
    fixed = ["_","_","_","_","_"]
    fixed_index = []
    unfixed = []
    greys = []
    
    while chances < 7:
        len_flag = True
        while(len_flag):
            print("*****TRY "+str(chances)+"*****")
            word = input("ENTER YOUR INPUT : ")
        
        
            if len(word) == 5:
                word = word.lower()
                chances += 1 
                
                flag1 = True
                while flag1:
                    try:
                        green =  int(input("Enter number of greens : "))
                    except:
                        print("\nEnter a integer : ")
                    else:
                        flag1 = False
                for_grey_index = []
                original_grey = [0,1,2,3,4]
                if green == 5:
                    print("BRUH GG")
                    len_flag = False
                    chances= 10
                    break
                if green != 0:
                    
                    for i in range(green):
                        flag2 = True
                        while flag2:
                            try:
                                green_index = int(input("Enter the index of green : "))
                            except:
                                print("Enter an integer :")
                            else:
                                flag2 = False

                        fixed_index.append(green_index)
                        fixed[green_index] = word[green_index]
                        for_grey_index.append(green_index)
                
                flag3 = True
                while flag3:
                    try:
                        yellow = int(input("Enter number of yellows : "))
                    except:
                        print("Enter an integer")
                    else:
                        flag3 = False
                if yellow != 0:
                    for i in range(yellow):
                        flag4 = True
                        while flag4:
                            try:
                                yellow_index = int(input("Enter the index of yellow : "))
                            except:
                                print("Enter an integer ")
                            else:
                                flag4 = False
                        unfixed.append(word[yellow_index])
                        for_grey_index.append(yellow_index)
                

                greys_temp = [word[a] for a in original_grey if a not in for_grey_index]
                greys = greys+ greys_temp

                next_guesses = []
                for i in allowed_guesses:
                    flag = True
                    for indexs in fixed_index:
                        if (i[indexs] != fixed[indexs]):
                            flag = False
                            break
                    if flag:
                        next_guesses.append(i)

                next_guesses_f = []
                for i in next_guesses:
                    flag = True
                    for letter in unfixed:
                        for x in greys:
                            if (x in i) or (letter not in i):
                                    flag = False
                                    break
                    if flag == True:
                        next_guesses_f.append(i)

                
                
                better_guesses = []
                for i in next_guesses:
                    if i in answers:
                        better_guesses.append(i)
                
                better_guesses_f = []
                for i in better_guesses:
                    flag = True
                    for letter in unfixed:
                        for x in greys:
                            if (x in i) or (letter not in i):
                                flag = False
                                break
                    if flag == True:
                        better_guesses_f.append(i)

                better_guesses_f2 = []

                print(better_guesses_f)
                print(greys)
                for i in better_guesses_f:
                    flag5 = True
                    for x in greys:
                        if x in i:
                            flag5 = False
                            break
                    if flag5:
                        better_guesses_f2.append(i)

                if len(better_guesses_f) > 200:
                    print("TOO many options ")
                else:
                    print("\n\n VERY PROBABLE WORDS :")
                    print(better_guesses_f2)

                #print("\n\n ALL THE AVAILABLE WORDS : \n\n")
                #print(next_guesses_f)
                len_flag = False
                
            else:
                print("Not a 5 letter word type again")

        
main()
