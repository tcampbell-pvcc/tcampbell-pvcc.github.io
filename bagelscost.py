#Name: Taylor Campbell
#Name: Taylor Campbell
#Prog Purpose: This program creates a sales receipt for Brownsville Bagels
#   Price for one bagel: $2.25
#   Price for cream cheese: $1.25
#   Sales tax rates: 6%
import datetime

############## define global variables ############
# define tax rate and prices
SALES_TAX_RATE= .06
PR_BAGEL= 2.25
PR_CREAMCH= 1.25 

# define global variables
num_tickets = 0
num_creamch = 0
cost_bagels = 0
cost_creamch = 0 
subtotal = 0 
sales_tax = 0
total = 0 

############## define program functions ################
def main(): 
    get_user_data()
    perform_calculations()
    display_results()
    
def get_user_data():
    global num_bagels, num_creamch
    num_bagels = int(input("Number of bagels: "))
    num_creamch- int(input("Number of cream cheese: "))
    
def perform_calculations():
    global cost_bagels, cost_creamch, subtotal, sales_tax, total
    cost_bagels = num_bagels * PR_BAGEL
    cost_creamch = num_creamch * PR_CREAMCH
    subtotal = cost_bagels + cost_creamch
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('______________________________')
    print('BROWNSVILLE BAGEL COMPANY')
    print('Fresh-baked bagels every day!')
    print('______________________________')
    print('Bagels       $ ' + format(cost_bagels,'8,.2f'))
    print('Cream cheese $ ' + str(cost_creamch))
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    print('subtotal     $ ' + str(subtotal))
    print('sales_tax    $ ' + str(sales_tax))
    print('total        $ ' + str(total))
    print('- - - - - - - - - - - - - - -')
    print(str(datetime.datetime.now()))
    
########## call on main program to execute ############
main()