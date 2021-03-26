print("Hello Mycaptain")
def most_frequent(word):
    count_i=word.count('i')
    count_s=word.count('s')
    count_m=word.count('m') 
    count_p=word.count('p')

    count={'i':count_i, 's':count_s ,'p':count_p , 'm':count_m}
    print(count)



v=input("Enter the word: ")
most_frequent(v) 
