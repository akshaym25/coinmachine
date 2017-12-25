item_cost = [24,35,31];
item_names = ['A','B','C'];
input_coins = 0
total_coins = 41
quarter = 25
nickel = 5
dime = 10
cents = 1
print"Please select the item A,B or C";
x = raw_input();
print "Selected item",x;
if x == item_names[0]:
    x = item_cost[0];
    print "The cost of the selected toy is",x;
elif x == item_names[1]:
    x = item_cost[1];
    print "The cost of the selected toy is", x;
elif x == item_names[2]:
    x=item_cost[2];
    print "The cost of the selected toy is", x;
else:
    print'invalid' ;

print "Please insert the coins in the form of 1,5,10,25"
y = input();
z = len(y);
a = sum(y);
i = 0
valid_coins = [1,5,10,25]

def valid_check():
    print "Please enter the remaining amount"
    rem = input();
    sum_rem = [0,0]
    sum_rem[0] = sum(rem);
    sum_rem[1] = len(rem);
    #sum_rem = 0;
    valid_coins = [1,5,10,25];
    for i in range(0,sum_rem[1]):
        if rem[i] in valid_coins:
            sum_rem[0] = sum_rem[0] + rem[i];
            return sum_rem
        else:
            sum_rem = 0;
            print "Invalid coins";
            return sum_rem

for i in range (0,z):
    if y[i] in valid_coins:
        input_coins += y[i];
    else:
        print "Invalid coins";
        input_coins = 0;

if input_coins == x:
    print "Transaction successful";
    for i in range (0,z):
        if nickel in y:
            nickel = nickel + y[i];
        if quarter in y:
            quarter = quarter + y[i];
        if dime in y:
            dime = dime + y[i];
        if cents in y:
            cents = cents + y[i];
    #total_coins = total_coins + input_coins;
elif input_coins < x and input_coins != 0:
    diff = x - input_coins;
    print "Your amount is short by %d returning $%d "%(diff,input_coins);
    #input_coins = 0
    print "diff",diff;
    # print "Please enter the remaining amount",diff;
    # rem = input();
    # sum_rem = sum(rem);
    # len_rem = len(rem);
    rem = valid_check()
    diff = diff - rem[0];
    while diff > 0:
        print "please enter remaining amount",diff;
        rem = valid_check()
        diff = diff - rem[0]
        if diff == 0:
            input_coins = input_coins + rem[0];
elif input_coins > x:
    diff = input_coins - x;
    print "returning extra coins",diff;
    input_coins = input_coins - diff;
    print "input coins ",input_coins;
total_coins = total_coins + input_coins;
print "Total coins in the machine",total_coins
print "dimes $",dime
print "quarter $",quarter
print "cents $",cents
print "nickel $",nickel


















