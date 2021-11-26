Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1. ans:-  step 1:  first search python.org on your computer
step 2: then a screen open ,then click on download button
step 3: after some time the python det installed in your system 
step 4: then search idle shell on your system 
step 5: then perform your program here .

2 .
a)   5**9
ans : 1953125
b)  3//2
ans: 1
c)  7//3
ans: 2
d)  7/2
ans: 3.5
e)  6==6
ans: True
f)  a=20;a+=30;a%=3;print(a)
ans: 2
g) True *False
ans:  let, a=5,
 b=10
 a>b
False
 a<b
True
a*b
50
H) True & False
ans: let:  a=5,
 b=10
 a>b
False
 a<b
True
a & b
0
i) print(True and False)
j)print((6>3) and (7<4) or (18==3)) and (9>3)
k) print(True is False)
l) print(False in ‘False’)
M)print((True == False) or (False > True)) and (False <= True)

#Q3)
s1 = "Nice to have it"
s2 = "here"
print(s1,s2)

# Q4)
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#Q5)
a.insert(0,s1)
a.insert(s2)
print(a)

#Q6)

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
 for i in numbers:
     if(i==237)
     break
    elif(i%2==0):
        print(i)
        
# the first number in the list is greater than 237 and hence no number gets printed

#Q7)

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

 print(color_list_1 - color_list_2)
 
        
#Q8)

 string = input("enter the sentence to be checked -")
 string = string.strip()
 string =string.upper()
 dictionary={}
 flag =1
 for i in range(65,91):
     dictionary[chr(i)]=0
 for i in string:

     if (ord(i)>=65 and ord(i)<=90):
         dictionary[i]+=1

for i in dictionary:
    if(dictionary[i]==0):
        flag=0
        break
 if(flag==0):
     print("given string is not a pangram")

  else:
      print("given string is pangram")

#Q9)


n= (input("enter a number -"))
num1=n
num2=n*2
num3= n*3
print(int(num1)+int(num2)+int(num3))


#Q10)

string1= eval(input("enter string in the given fashion"))   #"23 54  12#98 3 17"
string1=string1.strip()
string1+=" "
num=" "
x=[]
y=[]
flag=0
for i in string1:
    if (!=" "):
        if (i!="#"):
            num+=i

            else:
                flag = 1
                x.append(int(num))
                num=" "


           else:
               if (flag==0):
                   x.append(int(num))
                   num=" "

                   else:
                       y.append(int(num))
                       num=""
 print(x)
 print(y)


 #Q11)

 string2= (input("enter the word"))
 string2=string2.strip()
 string2+=","
 word=" "
 l=[]
 for i in string2:
     if(i!=","):
         word+=i

      else:
          l.append(word)
          word=" "
 l.sort()
 print(l)

 #Q12)

d = {'Student’: ['Rahul', ‘Kishore’, ‘Vidhya’, ‘Raakhi’],'marks':[57,87,67,79]}
    maximum=0
     idx=-1
     for i in d['marks']:
     idx+=1
     if(maximum<i):
     maximum=i
     pos=idx
print(d['student'][pos])


#Q13)

string3=input("enter the sentence"))
letter=0
digits=0
for i in string3:
    if (i.isalpha()):
        letters+=1
    if (i.isdigit()):
        digits+=1
 print("LETTERS" ,letters)
 print("DIGITS",digits)


 #Q14)

d = {'Name': ['Akash’, ‘Soniya’, ‘Vishakha’ , ‘Akshay’, ‘Rahul’, ‘Vikas’],
'Subject': ['Python’, ‘Java’, ‘Python’, ‘C’, ‘Python’, ‘Java’],
'Ratings’: [8.4, 7.8, 8, 9, 8.2, 5.6]}
inp=input("enter subject name")
            idx=-1
            pos=[]
            for i in d['subject']:
            idx+=1
            if(inp==i):
            pos.append(idx)
newdata={'name':[],'subject':[],'ratings':[]}
 for i in pos:
            newdata['Name'].append(d['Name'][i])
            newdata['Subject'].append(d['Subject'][i]
            newdata['Rating'].append(d['Rating'][i])

            print(newdata)

#Q15)
                                        
#-----------------------------------------------------------------------------

#Q16)
                                      
x=0
y=0
while(True):
    string4=(input("enter the instructions"))
    if(string4==""):
        break
    else:
        string4=string4.split(' ')
        if string4[0]=="UP":
            y+=int(string4[1])
        elif string4[0]=="DOWN":
            y-=int(string4[1])
        elif string4[0]=="RIGHT":
            x+=int(string4[1])
        elif string4[0]=="LEFT":
            x-=int(string4[1])
dist=(((x**2)+(y**2))**(1/2))
print('DISTANCE:'int(dist))
            
    
            
     

 
 
                


      
        








