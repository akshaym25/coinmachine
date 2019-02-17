def less_coin(rem):
    print "Please enter the remaining amount",rem
    input_rem = list(input())
    sum_input_rem = sum(input_rem)
    len_input_rem = len(input_rem)
    validity = validate(input_rem,len_input_rem)
    dummy = []
    while validity != 1:
        less_coin(rem)
    if sum_input_rem != rem:
        rem = rem - sum_input_rem
        dummy = dummy + input_rem
        less_coin(rem)
    input_rem = input_rem + dummy
    return input_rem


def value_check(item_selected,input_coins):
    sum_input_coins = sum(input_coins)
    if sum_input_coins == item_selected:
        flag = 1
        return flag
    elif sum_input_coins < item_selected:
        flag = 2
        return flag
    elif sum_input_coins > item_selected:
        flag = 3
        return flag
    else:
        flag = 0
        return flag

def validate(input_coins,len_input_coins):
    valid_coins = [1, 5, 10, 25]
    for i in range(0, len_input_coins):
        if input_coins[i] in valid_coins:
            validity = 1
        else:
            validity = 0
            break
    return validity

def main():
    item_cost = [24, 35, 31]
    item_names = ['A', 'B', 'C']
    #total_coins = 41
    quarter = 25
    nickel = 5
    dime = 10
    cents = 1
    item_selected = raw_input("Please select the item A,B or C\n")
    if item_selected == item_names[0]:
        item_selected = item_cost[0]
        print "The cost of the selected toy is", item_selected
    elif item_selected == item_names[1]:
        item_selected = item_cost[1]
        print "The cost of the selected toy is", item_selected
    elif item_selected == item_names[2]:
        item_selected = item_cost[2]
        print "The cost of the selected toy is", item_selected
    else:
        print'invalid'
        main()

    input_coins = list(input("Please enter the selected amount\n"))
    len_input_coins = len(input_coins)
    validity = validate(input_coins,len_input_coins)
    if validity == 1:
        value = value_check(item_selected,input_coins)
        if value == 1:
            print "Thank you for using the machine"
            for i in range(0, len_input_coins):
                if nickel in input_coins:
                    nickel = nickel + input_coins[i]
                if quarter in input_coins:
                    quarter = quarter + input_coins[i]
                if dime in input_coins:
                    dime = dime + input_coins[i]
                if cents in input_coins:
                    cents = cents + input_coins[i]
        elif value == 2:
            rem = item_selected - sum(input_coins)
            input_rem = less_coin(rem)
            total_input = input_coins + input_rem
            len_total_input = len(total_input)
            print "Thank you for using the machine"
            for i in range(0, len_total_input):
                if nickel in total_input:
                    nickel = nickel + total_input[i]
                if quarter in total_input:
                    quarter = quarter + total_input[i]
                if dime in total_input:
                    dime = dime + total_input[i]
                if cents in total_input:
                    cents = cents + total_input[i]
        elif value == 3:
            input_difference = sum(input_coins) - item_selected
            print "Thank you for using the machine returning extra amount",input_difference
            for i in range(0, len_input_coins):
                if nickel in input_coins:
                    nickel = nickel + input_coins[i]
                if quarter in input_coins:
                    quarter = quarter + input_coins[i]
                if dime in input_coins:
                    dime = dime + input_coins[i]
                if cents in input_coins:
                    cents = cents + input_coins[i]
            coins_returned = [0,0,0,0]
            coins_returned[0] = input_difference/25
            coins_returned[1] = (input_difference%25)/10
            coins_returned[2] = ((input_difference%25)%10)/5
            coins_returned[3] = (((input_difference%25)%10)%5)/1
            quarter = quarter - coins_returned[0]*25
            dime = dime - coins_returned[1]*10
            nickel = nickel - coins_returned[2]*5
            cents = cents - coins_returned[3]*1
    else:
        main()




main()

