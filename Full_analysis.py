from pickle import TRUE
from matplotlib.pyplot import get
import pandas as pd
import operator
import re,math

def checker2(comb, allowed_guesses, word):
    green_letters = ["","","","",""]
    green_index = []
    yellow_letters = {}
    grey_letters = []
    next_guess = []
    next_guess2 = []
    next_guess3 = []
    next_guess4 = []
    m = ""
    clues = comb.split()
    for i in range(len(clues)):
        m+=clues[i][0]
        if clues[i] == "green":
            green_letters[i] = word[i]
            green_index.append(i)
        if clues[i] == "black":
            grey_letters.append(word[i])
        if clues[i] == "yellow":
            if word[i] not in yellow_letters:
                yellow_letters[word[i]] = [i]
            else:
                yellow_letters[word[i]].append(i)

    
    #check greens
    for i in allowed_guesses:
        flag = True
        for indexes in green_index:
            if green_letters[indexes] != i[indexes]:
                flag = False
                break
        if flag:
            next_guess.append(i)

    #check greys:
    for i in next_guess:
        flag = True
        for letter in grey_letters:
            if letter in i :
                flag = False
                break
        if flag:
            next_guess2.append(i)

    #check for yellows:
    for i in next_guess2:
        flag = True
        for letters,positions in yellow_letters.items():
            if (letters not in i):
                flag = False
        if flag:
            next_guess3.append(i)

    for i in next_guess3:
        flag = True
        for letters,positions in yellow_letters.items():
            if letters in i:
                indices = [x.start() for x in re.finditer(letters, i)]
            for indic in indices:
                if indic in positions:
                    flag = False
                    break
        if flag:
            next_guess4.append(i)
    #print(next_guess4)
    return len(next_guess4),m

def get_combs():
    all_combs = []
    alpha = ["black" ,"green" , "yellow"]
    for one in alpha:
        for two in alpha:
            for three in alpha:
                for four in alpha:
                    for five in alpha:
                        x = one+" "+two+" "+three+" "+four+" "+five
                        if x not in all_combs:
                            all_combs.append(x)
    return all_combs

all_combs = get_combs()

def final_main(answer1):
    answers = []
    count = 1
    green_index = []
    fixed = ["","","","",""]
    yellows = {}
    greys = []
    next_guess1 = []
    next_guess2 = []
    next_guess3 = []
    next_guess4 = []
    
    with open("possible answers.txt", "r") as file:
        answers.append(file.read())
        allowed_answers =  answers[0].split("\n")

    allowed_answers2 = [i for i in allowed_answers]
    df = pd.read_csv("lol.csv")
    max_value= df['values'].max()
    df2 = df. loc[df['values'] == max_value]
    guess = df2.values.tolist()[0][1]
    #guess = "tares"
    #answer = "catch"
    answer = answer1
    #x = 1
    #print(guess)
    while guess != answer :
        new_dic = {}
        next_guess1 = []
        next_guess2 = []
        next_guess3 = []
        next_guess4 = []
        dic = {}
        keyss = []
        values = []
        word = guess
        #next_guess = checker(guess, allowed_answers, answer)
        for i in range(len(word)):
            if word[i] == answer[i]:
                green_index.append(i)
                fixed[i] = word[i]
        
        for i in range(len(word)):
            indices = [x.start() for x in re.finditer(word[i], answer)]
            if (word[i] in answer) and (i not in indices):
                if word[i] in yellows:
                    yellows[word[i]].append(i)
                else:
                    yellows[word[i]] = [i]

        for i in range(len(word)):   
            if word[i] not in answer:
                greys.append(word[i])
        #print(greys)
        #check for grens
        for i in allowed_answers:
            flag = True
            for indec in green_index:
                if i[indec] != fixed[indec]:
                    flag = False
                    break
            if flag:
                next_guess1.append(i)

        #check greys:
        for i in next_guess1:
            flag = True
            for letter in greys:
                if letter in i :
                    flag = False
                    break
            if flag:
                next_guess2.append(i)
        
        #check for yellows:
        for i in next_guess2:
            flag = True
            for letters,positions in yellows.items():
                if (letters not in i):
                    flag = False
            if flag:
                next_guess3.append(i)

        for i in next_guess3:
            flag = True
            for letters,positions in yellows.items():
                if letters in i:
                    indices = [x.start() for x in re.finditer(letters, i)]
                for indic in indices:
                    if indic in positions:
                        flag = False
                        break
            if flag:
                next_guess4.append(i)

        length = len(next_guess4)
        for word in next_guess4:
            for comb in all_combs:
                A = checker2(comb , allowed_answers ,word)
                dic[A[1]] = A[0]
            for k,v in dic.items():
                keyss.append(k)
                values.append(v)
            dic = dict(sorted(dic.items(), key=lambda item: item[1] , reverse=True))
            ans = 0
            for k,v in dic.items():
                prob = v/len(allowed_answers2)
                logs = 0
                if prob != 0:
                    logs = math.log2(1/prob)
                ans += prob*logs
                new_dic[word] = ans
        #print(new_dic)
        allowed_answers = [i for i in next_guess4]
        
        guess = max(new_dic.items(), key=operator.itemgetter(1))[0]
        print(guess)
        count+=1
    #return count

def main():
    lol = 0
    answers = [] 
    numbers = []
    values = []
    dic = {}
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    more = 0
    with open("possible answers.txt", "r") as file:
        answers.append(file.read())
        allowed_answers =  answers[0].split("\n")
    for answer in allowed_answers:
        x = final_main(answer)
        if x == 1:
            one+=1
        elif x == 2:
            two+=1
        elif x == 3:
            three+=1
        elif x == 4:
            four+=1
        elif x == 5:
            five+=1
        elif x == 6:
            six +=1
        elif x>6:
            more+=1
        lol +=1
        print(lol ,one , two , three, four, five, six , more)
    dic["one"] = one
    dic["two"] = two
    dic["three"] = three
    dic["four"] = four
    dic["five"] = five
    dic["six"] = six
    dic["more"] = more
    for k,v in dic.items():
        numbers.append(k)
        values.append(v)
    df = pd.DataFrame({"word" : numbers,
                    "values" : values})
    df.to_csv("valuesss.csv") 



#main()
final_main("shave")