question_list = [
 "How many continents are there?",     # pehla question
 "What is the capital of India?",   # doosra question
 "NG mei kaun se course padhaya jaata hai?" # teesra question
]

options_list = [
 #pehle question ke liye options
 ["Four", "Nine", "Seven", "Eight"],
 #second question ke liye options
 ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
 #third question ke liye options
 ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
i=1
while i<=len(question_list):
    print(question_list[i-1])
    print(options_list[i-1])
    answer=int(input('enter your answer in option no.'))
    solution_list=[3,4,1]
    if solution_list[i-1]==answer:
        print('absolutely right')
        print('A big clap for you')
        # if i==len(question_list):
        #     break
        # else:
        #     print('now!,your next question is...')
    else:
        print('sorry!,wrong answer')
        # print('your next question')
    if i==len(question_list):
        break
    else:
        print('now!,your next question is...')
    i+=1
print('you played very well.')