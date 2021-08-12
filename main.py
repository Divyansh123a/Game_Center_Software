import play_card 

def get_card_details():
    #Fill the code for getting user inputs and creating the card object
    card_number = int(input("Enter Card Number"))
    holder_name = input("Enter Holder Name:")
    amount = float(input("Enter Amount"))
    card_obj = play_card.PlayCard(card_number,holder_name,amount)
    return card_obj



def main():
    card_obj=get_card_details()  
    hrs=int(input("Enter Hours Want to Play:"))

    #Fill the code for invoking the calculate_total_point() and calculate_balance(). 
    #Fill the code for displaying the balance total points.
    card_obj.calculate_total_points()
    if(card_obj.calculate_balance(hrs)):
        print("Balance is {:.2f}".format(card_obj.get_total_points()))
    else:
        print("You need more amount to play")
    



if __name__=='__main__':
    main()
    
