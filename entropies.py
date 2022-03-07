import matplotlib.pyplot as plt
import re
from collections import OrderedDict
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

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

def checker(comb, answer , allowed_guesses, word):
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


def main():   
    
    new_dic= {}
    all_combs = get_combs()
    dic = {}
    keyss = []
    values = []
    max = 0
    #all_combs = ["green green grey grey yellow"] 
    answers, allowed_guesses = creating_list()
    #print(answers)
    for word in answers:
    #word = input("Enter a word : ")
        for comb in all_combs:
            A = checker(comb, answers , allowed_guesses, word)
            dic[A[1]] = A[0]
        for k,v in dic.items():
            keyss.append(k)
            values.append(v)

        df = pd.DataFrame({"keyss":keyss,
                    "values":values})
        df = df[df["values"]> 10]
        '''plt.figure(figsize=(10,6))
    # make barplot and sort bars
        sns.barplot(x='keyss',y="values", data=df, order=df.sort_values('values').keyss)
        # set labels
        plt.xlabel("Keys", size=5)
        plt.xticks(rotation = 90)
        plt.tick_params(labelsize = 5)
        plt.ylabel("values", size=15)
        plt.show()'''
        dic = dict(sorted(dic.items(), key=lambda item: item[1] , reverse=True))
        ans = 0
        for k,v in dic.items():
            prob = v/12972
            logs = 0
            if prob != 0:
                logs = math.log2(1/prob)
            ans += prob*logs
            new_dic[word] = ans
        print(len(new_dic))
    words = []
    entropies = []
    for k,v in new_dic.items():
        words.append(k)
        entropies.append(v)
    df = pd.DataFrame({"word":words,
                    "values":entropies})
    df.to_csv("lol.csv")
        
    
main()