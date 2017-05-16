#*********************** List *******************************#
x=[1,2,3,4]
y=5
x.append(y)
x.append(6)
print(x)

y=[7,8]
x.extend(y)
print(x)

y=x+["ab","taha"]
print(y)

y=x+y
print(y)

x,y=[9,5]
print("x=",x,"\ny=",y)

x,y,z,a=[[14,4,9],[25,5.4],{"name":"taha","age":20},(32,"abc")]
print("x=",x,"\ny=",y,"\nz=",z,"\na=",a)

print(x[-1])

_,y=[1,2]   # _ throw away the value now y == 2, didn't care about the first element
print("x=",x,"\ny=",y)

#****************************** List Comprehension *********************************#
list=[x for x in range(5)]
print("Comprehensive list by range",list)

list_2=[x for x in list]
print("Comprehensive list",list_2)

even_list=[x for x in range(5) if x%2 ==0]
print("Even list",even_list)

odd_list=[x for x in list if x%2 !=0]
print("Odd list",odd_list)

square_list=[x*x for x in range(5)]
print("Square list",square_list)

even_square_list=[x*x for x in list if x%2 ==0]
print("Even Square List",even_square_list)

odd_square_list=[x for x in square_list if x%2 !=0 ]
print("Odd Square List",odd_square_list)

#******************** If you don’t need the value from the list, it’s conventional to use an underscore as the variable ****************************#
zeroes=[0 for _ in even_list]  ### has the same length as even_numbers

print(zeroes)

zeroes=[2 for _ in even_list]   ## has the same length as odd_numbers

print(zeroes)

#*************************** You can similarly turn lists into dictionaries or sets: **************************************#
square_dict={x : x*x for x in list}
print("Square Dictionary",square_dict)

square_set= {x*x for x in [1,-1]}
print(square_set)

#************************ A list comprehension can include multiple fors: ****************#
pairs=[(x,y)
       for x in range(10)
       for y in range(10)]
print("Pairs",pairs)


dict={"data1":[1,4,4,5],"data2":[3,4,5,5]}
for x in dict.values():
    print(x)


#************************** Tuples ************************#
#Tuples are immutable which means that it can not be medified it same as list but use ()

my_list=[3,5,4]
my_list[1]=6   #we can modify the list but can not modify tuples
print(my_list)

my_tuple=(12,8,5,"taha") # we can also use tuple without braces 12,8
print(my_tuple[1])
#my_tuple[1]=77        # it as an error because tuple can,t be modified
#print(my_tuple)

try:                   #Exceptional Handling
    my_tuple[1]=77
except TypeError:
    print ("can not modify a tuple")

def sum_and_products(x,y):    
    return x+y,x*y
sp=sum_and_products(2,4)
print(sp)
a,b=sum_and_products(5,10)   #Tuples are a convenient way to return multiple values from functions:
print("a",a,"b",b)                  #a=15 and b=50

a,b=b,a                     ## Pythonic way to swap variables; now a=50 and b=15
print("a",a,"b",b)


#******************************* Dictionaries ******************************************#

my_dict={"name":"taha","age":20,"Place of Birth":"Karachi","Height":5.11}
print("name" in my_dict) #defaultly it will only check the key 

print(5.11 in my_dict.values()) #it will only check the values against key

print("Height" in my_dict.keys()) #it will only check the keys 

print(my_dict.values())

##Dictionaries have a get method that returns a default value (instead of raising an exception) when you look up a key that’s not in the dictionary:exception) when you look up a key that’s not in the dictionary
a=my_dict.get("age")
print(a)
print(my_dict.get("accupation",0))    # it will not send the Error

##You assign key-value pairs using the same square brackets
my_dict["Education"]={"Matriculation":2012,"Inter":2015,"Bachelors":"Present"}  # passing dict into my_dic
print(my_dict)
my_dict["weight"]=85
my_dict["favourite foods"]=["Chinnese","Continental","Desi","Thai"]   #passing list into my_dict
my_dict["weight"]=80      #we can also change the values 
print(my_dict)

tweet={
        "user" : "joelgrus",
        "text" : "Data Science is Awesome",
        "retweet_count" : 100,
        "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
        }
print(tweet)
print(tweet.values())
print(tweet.keys())



#DefaultDict

with open("data.txt") as my_file:     #1st approach
    file=my_file.read()
    word_counts={}
    for words in file :
        print(words)
        if words in word_counts:
            word_counts[words]=word_counts[words]+1     # adding the 1 if words in word count against that word in word_coun dict
        else:
            word_counts[words]=1
    print("Approach 1",word_counts)
list=[x for x in word_counts.values()]
list.sort(reverse=True)
print(list)

with open("data.txt") as my_file:        #2nd approach
    document=my_file.read()
    word_count={}
    for words in document:
        previous_count=word_count.get(words,0)
        word_count[words]=previous_count+1
    print("Approach 2",word_count)

from collections import defaultdict

with open("data.txt") as my_file:
    document=my_file.read()
    word_counts=defaultdict(int)
    for word in document:
        word_counts[word]+=1
    print("Approach 3 by importing defaultdict",word_count)
