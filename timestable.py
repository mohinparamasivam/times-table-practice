import os
import random
print("                                                                       ")
print("                                                                       ")
print ("            #################################################" )       
print ("            #                                               #" )        
print ("            #         Interactive Times Table Exercise Tool #" )        
print ("            #                                               #" )        
print ("            #                  Version 1.0                  #" )        
print ("            #                                               #" )       
print ("            #           Author : Mohin Paramasivam          #" )       
print ("            #                                               #" )       
print ("            #################################################" )       

print("                                                                   ")


print("                                           ")

print("Option 1  : Times Table 1  ")
print("Option 2  : Times Table 2  ")
print("Option 3  : Times Table 3  ")
print("Option 4  : Times Table 4  ")
print("Option 5  : Times Table 5  ")
print("Option 6  : Times Table 6  ")
print("Option 7  : Times Table 7  ")
print("Option 8  : Times Table 8  ")
print("Option 9  : Times Table 9  ")
print("Option 10 : Times Table 10 ")
print("Option 11 : Times Table 11 ")
print("Option 12 : Times Table 12 ")
print("Option 13 : Times Table 1-12 ( Mix ) ")
print("							  ")
print(" Choose from number 1-12 : ")
print("							  ")
number_choice = int(input("Option : "))



counter = int(input("Please enter the counter value : ")) ##Set a counter value
os.system('clear')
counter_fix_percentage_calculate = counter

print("        ")
print ("            #################################################" )       
print ("            #                                               #" )        
print ("            #         Interactive Times Table Exercise Tool #" )        
print ("            #                                               #" )        
print ("            #                  Version 1.0                  #" )        
print ("            #                                               #" )       
print ("            #           Author : Mohin Paramasivam          #" )       
print ("            #                                               #" )       
print ("            #################################################" )       
print("                                                              " )
print("                          Questions                                    " )
print("                          ----------                                    " )
print("                                                              " )

##question code for other than option 13

if number_choice!=13:
	while(counter!=0):
		number = random.randint(1,12)
		question=input("      " + ((str(number))+"  "+"*"+str(number_choice))+"  " +":")
		number_multiplication = (number*number_choice)





##Answer declare for operation  

		answer=number_multiplication

## Output for wrong and correct answer
		
		while (str(answer)!=str(question)):
			print("    	    ")
			print("Wrong!!  ")
			print("         ")
			question=input("      " + ((str(number))+"  "+"*"+str(number_choice))+"  " +":")
			number_multiplication = (number*number_choice)
			answer=number_multiplication


		else :
			print("   ")
			print("Correct!!")
			print("         ")
			counter = counter-1






## question code for option 13

if number_choice==13:
	while(counter!=0):
		number = random.randint(1,12)
		number_choice = random.randint(1,12)
		question=input("      " + ((str(number))+"  "+"*"+str(number_choice))+"  " +":")
		number_multiplication = (number*number_choice)





##Answer declare for operation  

		answer=number_multiplication

## Output for wrong and correct answer
		while (str(answer)!=str(question)):
			print("    	    ")
			print("Wrong!!  ")
			print("         ")
			question=input("      " + ((str(number))+"  "+"*"+str(number_choice))+"  " +":")
			number_multiplication = (number*number_choice)
			answer=number_multiplication


		else :
			print("   ")
			print("Correct!!")
			print("         ")
			counter = counter-1

print("Congratulations you have completed exercising Times Table ")
print("									")
print(" ##Practice makes Perfect")
print("								")




