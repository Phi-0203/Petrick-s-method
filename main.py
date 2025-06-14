# logic_design final project - Petrick's method 
# Author: [1130737 趙翊帆]
# Date: 2025/6/12

from sympy import * # import all functions from sympy module 
from itertools import product #allow to use product function to get all combinations of SOPs by Cartesian product

n = 1 # the nth of function
F = [] # use list to store the minterm of function

# system input 
while True: # use a while loop to allow input different f
    function = str(input ("Please input minterm number  of f" + str(n)+" :\n")) # request minterm function
    if function == "": # if function is empty, break the loop
        break
    else:
        n += 1 # function is normal, lterative the nth of function
        F.append(function) # add f to F list
c = 1 # counter of prime implicants
s = 0 # counter of shared term
S = [] # use a list to store the shared term of P, initially empty
while True: # use a while loop to allow input different shared term
   shared_term = input("Please input the shared term P" + str(c) +": ").split(",") # request share term
   if shared_term != [""]:
      S.append(shared_term) # if shared term is not empty, add it to shared_term list
      c+=1 # lterative the nth of shared term
      s+=1 # lterative the number of shared term
   else: # if S is empty, break the loop, don't lterative c
      break
PI = {} # use a dictionary to store the prime implicants
PI_counter = [] # use a list to store the prime implicants for counting
for m in range(1,n): # for each function in F
   P_list = [] # let P_list is a list of P, initially empty      
   while True: # use a while loop to allow input different P
         P = input("Please input the PI of fnnction"+str(m)+"'s P"+str(c)+": ").split(",") # request P and convert it to a list
         if P != [""]: # if P is not empty
            P_list.append(P) # add it to P_list
            PI_counter.append(P) # add P to PI_counter for counting
            c+=1 # lterative the nth of P 
         else:
            break
   PI["PI of f"+str(m)] = P_list # add P_list to PI dictionary with key "PI of f"+str(m)
#print(PI_counter) # output the list of P for counting for checking the  minterm

# algorithm of Petrick's method
groups = {}  # use a dictionary to store the groups of P that cover each minterm
for f in F:  # for each function in F
    group = []  # create a list to store the group of P that covers each minterm
    for minterm in f.split(","):  # convert the f to a list 
        covered = [] # create a list to store the P that covers the minterm
        for i, shared in enumerate(S): # check each shared term
               if minterm in shared: # if the miterm covered by shared term
                  covered.append("P" + str(i + 1)) # add the shared term to covered list
                  #break # break the loop to avoid adding the same shared term
        for P in PI["PI of f"+str(F.index(f)+1)]: # check each P in PI of f
            if minterm in P : # if P covers the minterm 
               covered.append("P" + str(PI_counter.index(P) + 1 + s))  # add P to covered 
            # (PI.index(P)+1, because P is numbered from 1, and s is added to account for shared terms)
        group.append(covered) # add the covered list to group
        groups["f" + str(F.index(f) + 1)] = group  # store the group of P that covers each minterm in groups dictionary
# output the groups of P that cover each minterm
#for key in groups: 
   #print(f"{key}: {groups[key]}") 

# calculate each P_function
all_solutions = {} # dictionary to store all solutions for each function
for key, group in groups.items():
   term = [Or(*[simplify(p) for p in t]) for t in group]  # create a list to store the term of P_function in POS form by OR each P in coverd list of group
   P_function = And(*term)  # AND all the terms together to get P_function in POS form
   result = to_dnf(P_function, simplify=True)  # convert P_function to SOP form by using to_dnf function (disjunctive law), and simplify it by using simplify=True
   #print(f"Result of {key}  : \n", result)  # output the result of P_function 
   result_list = str(result).split("|")  # convert the result to string for use
   all_solutions[key] = result_list  # store each the result list in all_solutions dictionary
   
# find the minimum solution for multiple outputs   
all_combinations = list(product(*all_solutions.values()))  # get all combinations of SOPs by Cartesian product
min_total_cost = float('inf') # initialize min_total_cost to infinity for comparison
best_combos = [] # store the best combinations of solutions by list
for combo in all_combinations: # for each combination of solutions
    used_p = set() # use a set to store the used P to avoid duplication
    for expr in combo: # for each expression in the combination
        parts = [p.strip() for p in expr.split("&")] # get each solution by splitting the expression by "&", stripping whitespace
        used_p.update(parts) # add the parts to used_p set
    total_cost = len(used_p) # calculate the total cost by counting the number of unique P used in the combination
    if total_cost < min_total_cost: # if the total cost is less than the current minimum
        min_total_cost = total_cost # update the minimum total cost
        best_combos = [combo] # reset the best_combos to the current combination
    elif total_cost == min_total_cost: # if the total cost is equal to the current minimum
        best_combos.append(combo) # add the current combination to the best_combos
for i, combo in enumerate(best_combos, 1): # enumerate the best combinations starting from 1
    print(f" solution {i} :") # output the index of the best combination
    for fn_name, expression in zip(all_solutions.keys(), combo): # zip the function names and expressions together
        print(f"  {fn_name}'s P-function = {expression}") # output the best combinations of solutions
        print(f"  {fn_name}'s minimum SOP = {expression.replace("&","+")}") # output the best combinations of solutions in a more readable format

input("👾:This is final solution, Enter to close windows...")