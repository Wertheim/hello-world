#keep working on PS 1
#If you dont know how to do something
#check your Lesson Code notes
#They have good examples of all the code

#ps1c (bi-section)

#declare variables for user input
annual_salary = int(input("Enter your annual salary: "))
portion_saved = 0
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = total_cost * .25

#update current savings every month
current_savings = 0

#annual return
r = 0.04

#counters

num_guesses = 0
low = 0
high = 10000
portion_saved = (high + low)/2.0

while abs(current_savings - portion_down_payment) >= 100:
    #recalculate monthly salary every time we try a new portion saved.
    monthly_salary = annual_salary / 12
    months = 0
    current_savings = 0
    
    #use a while loop to simulate  36 months
    while(months < 32):    
    #update savings using calculations from problem
        current_savings += current_savings * r/12
        current_savings += monthly_salary * (portion_saved/10000.0)
        #print(current_savings, portion_saved/1000.0)
        #print(portion_down_payment, monthly_salary)
    #calculate semi-annual raise and increase number of months 
        months += 1
        if(months%6==0):
            monthly_salary += annual_salary * semi_annual_raise / 12
#calculate new guess(portion_saved) based on if we are above or below
    if(current_savings < portion_down_payment):
        low = portion_saved
    else:
        high = portion_saved

    portion_saved = (high+low)/2.0
    num_guesses+=1
#print output outside of while loop
print "Best savings rate: " + str(portion_saved/10000.0)
print "Number of guesses: " + str(num_guesses)
