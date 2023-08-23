#Alejandro Rodriguez
#7/26/23
#file: main.py

#block coloring and proposed coloring for Z_n

#import my coloring class
from coloring import Coloring

#main while loop
while True:
    print("Coloring for Z_n")

    #coloring choioces
    print("Choose coloring.")
    print("(1) for 2009 block coloring:")
    print("(2) for our proposed coloring:")
    print("(3) for custom coloring:")

    #input for our user choice above
    choice = int(input("Coloring:"))

    #if 1
    if choice == 1:
        print("we are in 2009 block")

        #input for n = size of first block
        n = int(input("choose size of first block: "))

        #create class object that will have user value n
        new_coloring_f = Coloring(n,0)

        #f will gold colored list
        f = new_coloring_f.build_researched_coloring()

        #prompt user for equation
        print("pick coefficeints for equaton: ax + by = cz.")
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))

        #get number of total and mono solutions to given equations
        number_total_f = new_coloring_f.general_solutions(a,b,c,f)
        number_mono_f = new_coloring_f.mono_solutions(a,b,c,f)

        #print those numbers
        print("number of total solutions: ", number_total_f)
        print("number of mono solutions:", number_mono_f)

        print("mono/total solutions: ", number_mono_f/number_total_f)

        #new_coloring_f.print_block_coloring(f)



    #if 2
    elif choice == 2:
        print("we are in proposed block")

        #input for n
        n = int(input("choose n:"))

        #create our object
        new_coloring_g = Coloring(n,0)

        #g will hold the colored list
        g = new_coloring_g.build_propsed_coloring()

        #prompt user for equation
        print("pick coefficeints for equaton: ax + by = cz.")
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))

        #get number of total and mono solutions to given equations
        number_total_g = new_coloring_g.general_solutions(a,b,c,g)
        number_mono_g = new_coloring_g.mono_solutions(a,b,c,g)

        #print those numbers
        print("number of total solutions: ", number_total_g)
        print("number of mono solutions:", number_mono_g)

        print("mono/total solutions: ", number_mono_g/number_total_g)

        new_coloring_g.print_coloring(g)

    elif choice == 3:
        print("we are in custom coloring block.")

        #input for n
        n = int(input("choose n:"))

        #create the object class
        new_coloring_c = Coloring(n,0)

        #promts user for string of numbers
        print("input your custom 3 coloring: Ex 112231 -> this coloring that will repeat for a given Z_n")

        custom_string = input("custom coloring: ")

        #c will hold the custom colored list
        c_two = new_coloring_c.build_custom_coloring(custom_string)

        #prints list
        new_coloring_c.print_coloring(c_two)

        #get coeficients form user
        print("pick coefficeints for equaton: ax + by = cz.")
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))

        #get total number of solutions and mono solutions
        number_total_c = new_coloring_c.general_solutions(a,b,c,c_two)
        number_mono_c = new_coloring_c.mono_solutions(a,b,c,c_two)

        #print number of solutions
        print("number of total solutions: ", number_total_c)
        print("number of mono solutions: ", number_mono_c)

        #print percenatge
        print("mono/total solutions: ", number_mono_c/number_total_c)




    #everything else break loop EXIT
    else:
        print("Bye!")
        break
    pass