'''
your_num=eval(input("Enter any number between 1-10 range:  "))
if your_num in [1,2,3,4,5,6,7,8,9,10]:
    if your_num==1:
        print("one")
    elif your_num==2:
        print("two")
    elif your_num==3:
        print("three")
    elif your_num==4:
        print("four")
    elif your_num==5:
        print("five")
    elif your_num==6:
        print("six")
    elif your_num==7:
        print("seven")
    elif your_num==8:
        print("eight")
    elif your_num==9:
        print("nine")
    else:
        print("ten")
else:
    print("out of range number please select 1-10 range")
'''

'''
#Improved version of code
your_num=eval(input("Enter any number between 1-10 range:  "))
num_word={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
if your_num in [1,2,3,4,5,6,7,8,9,10]:
    print(num_word.get(your_num))
else:
    print("out of range number please select 1-10 range")

'''
