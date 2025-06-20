subject1 = input('subject name1: ') 
subject2 = input('subject name2: ') 
subject3 = input('subject name3: ')  
subject4 = input('subject name4: ')
subject5 = input('subject name5: ')


madlibs = "I am a student of computer science learning major {subject1}, and after that will learn {subject2}, then {subject3} and at last {subject3} and {subject4}".format
print(madlibs)

madlibs1 = madlibs(subject1='datascience', subject2='datascience', subject3='datascience', subject4='datascience', subject5='datascience')

if madlibs == madlibs1:
    print("The madlib is correct!")
else:
    print("The madlib is incorrect, please try again.")

print("the end of the program")
# madlibs = madlibs(subject1=subject1, subject2=subject2, subject3=subject3, subject4=subject4, subject5=subject5)
# print(madlibs)











