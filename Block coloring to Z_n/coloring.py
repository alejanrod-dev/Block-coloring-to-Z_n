#Alejandro Rodirguez
#7/26/23
#file: coloring.py

#class used for my main program hold all functions used in main.py

import math


class Coloring(object):

    #init function only size of n which will dictate size of list
    def __init__(self, n,block_c):
        self.n = n
        self.block_c = block_c

    #function builds a list of our propsed coloring
    def build_propsed_coloring(self):

        #create a empty list
        colored_list = []

        #use a loop to build up the list with append
        for x in range(0,self.n):
            if x % 5 == 0:
                colored_list.append(1)
            elif (x % 5 == 1) or (x % 5 == 4):
                colored_list.append(2)
            elif (x % 5 == 2) or (x % 5 == 3):
                colored_list.append(3)

        #returns our filled list
        return colored_list

    #function that returns solutions to ax + by = cx for Z_n list
    def general_solutions(self, a, b, c, l):

        number_solutions = 0

        #2 loops to look for soultons to given equations 
        for x in range(0,len(l)):
            for y in range(0,len(l)):
                if(b*y >= a*x) and (((a*x + b*y) % len(l)) % c == 0 ):
                    #prints basic solutions below
                    #print(a*x,"+",b*y,"=", (a*x+b*y) % len(l))

                    #prints more detail solutions below
                    #print(a,"(",x,")","+",b,"(",y,")","=", c,"(",((a*x+b*y) % len(l)) // c,")")

                    number_solutions+=1

        #we want to return the number of solutions
        return number_solutions

    #2009 proposed best block coloring
    def build_researched_coloring(self):

        #n.self will be the size of out fist block, all other block will be porportional to this first block n according to there coloring
   
        #list that will hold our block coloring
        colored_list = []

        #print each coloring block size
        #print("regular:",1*self.n, (3/2)*self.n, (1/4)*self.n, 3*self.n, (1/8)*self.n, (487/440)*self.n, (47/440)*self.n)

        #varible {a,b,c,d,e,f} correspond to block size l={1, 3/2, 1/4, 3, 1/8, 487/440, 47/440}
        #we truncate to nearst whole number for our list to have integers values.
        a = math.trunc(1*self.n)
        b = math.trunc((3/2)*self.n)
        c = math.trunc((1/4)*self.n)
        d = math.trunc(3*self.n)
        e = math.trunc((1/8)*self.n)
        f = math.trunc((487/440)*self.n)
        g = math.trunc((47/440)*self.n)

        #prints our truncated values of {a,b,c,d,e,f}
        #print("truncated values:", a,b,c,d,e,f,g)

        #loop to build coloring according to our blocks
        for x in range(0, (a + b + c + d + e + f + g)+1):
            if x < a:
                colored_list.append(1)
            elif x >= a and x < a + b:
                colored_list.append(2)
            elif x >= a + b and x < a + b + c:
                colored_list.append(1)
            elif x >= a + b + c and x < a + b + c + d:
                colored_list.append(3)
            elif x >= a + b + c + d and x < a + b + c + d + e:
                colored_list.append(1)
            elif x >= a + b + c + d + e and x < a + b + c + d + e + f:
                colored_list.append(2)
            elif x >= a + b + c + d + e + f and x < a + b + c + d + e + f + g:
                colored_list.append(1)
        
        #Z_(length of list)
        print("Z_",len(colored_list))
        self.block_c = len(colored_list)

        #return the filled list
        return colored_list

    #find monochromatic solutions to ax + by = cz equations given a colored list in Z_(lenth of list(l) given)
    def mono_solutions(self, a , b, c , l):

        #varibles that will hold the number of solutions
        mono_solutions = 0

        #2 loops to look for soultions to given equations 
        for x in range(0,len(l)):
            for y in range(0,len(l)):

                #check thaat b*y >= a*x, so we dont get not negatives
                if(b*y >= a*x) and (((a*x + b*y) % len(l)) % c == 0 ):

                    #checks list at index x, y,and z = [((a*x+b*y) % len(l)) // c], if they are the same color then its mono solution
                    if l[x] == l[y] and l[y] == l[((a*x+b*y) % len(l)) // c]:

                        #prints mono solutions
                        #print("mono: ",a*x,"+",b*y,"=", c,"(",((a*x+b*y) % len(l)) // c,")")

                        #prints specific color solutions
                        #if(l[x] == 1,2,3):

                            #print("red = 1",a,"(",x,")","+",b,"(",y,")","=", c,"(",((a*x+b*y) % len(l)) // c,")")
                            #print("blue = 2",a,"(",x,")","+",b,"(",y,")","=", c,"(",((a*x+b*y) % len(l)) // c,")")
                            #print("green = 3",a,"(",x,")","+",b,"(",y,")","=", c,"(",((a*x+b*y) % len(l)) // c,")")

                        mono_solutions+=1

        #returns number of mono chromatic solutions
        return mono_solutions

    #build a custom coloring given a user string
    def build_custom_coloring(self, custom_string):

        #list that will contain the custom coloring
        custom_coloring = []

        #list that will hold the each string chacter after turning each char -> int
        c_str_l = []

        #loop turns each char from user string to a integer and bulds a list
        for x in range(len(custom_string)):
            c_str_l.append(int(custom_string[x]))


        #2 loops to build the custome coloring, which relies on char -> int list
        for x in range(0,self.n):
            for i in range(len(c_str_l)):
                if x % len(c_str_l) == i:
                    custom_coloring.append(c_str_l[i])
                    continue

        #returns the customs colored list
        return custom_coloring

    #prints colored list
    def print_coloring(self, l):
        print("Z_",self.n," = ", end="")
        print(l)

    #prints the block coloring
    def print_block_coloring(self, l):
        print("Z_",self.block_c ,"=", end="")
        print(l)


 





