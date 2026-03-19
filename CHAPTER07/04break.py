for i in range(100):
    if(i == 34):
        break #@ Exit the loop right now
    print(i)



#@ continue 
"""
continue is used to stop the current iteration of 
the loop and continue with the next oneit instruction
the program to skip this iteration

"""
for i in range(100):
    if(i == 34):
        continue     #@skip this iteration
    print(i)


#@ pass statement
"""
pass is a null statement in python
it instruct to do nothing

"""

l = [1,7,8]
for item in l:
    pass  #@ without pass, the program will throw an error