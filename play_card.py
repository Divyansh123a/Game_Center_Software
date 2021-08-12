class PlayCard:
    def __init__(self, card_number,holder_name,amount):
        self.__total_points=0.0
        #Fill the code here for initializing the instance variables
        self.__card_number = card_number;
        self.__holder_name = holder_name;
        self.__amount = amount;
        

    def get_card_number(self):
        return self.__card_number
    
    def set_card_number(self,card_number):
        self.__card_number = card_number
    
    def get_holder_name(self):
        return self.__holder_name
    
    def set_holder_name(self,holder_name):
        self.__holder_name = holder_name
    
    def get_amount(self):
        return self.__amount
    
    def set_amount(self,amount):
        self.__amount = amount
    
    def get_total_points(self):
        return self.__total_points
    
    def set_total_points(self,total_points):
        self.__total_points = total_points
    
    def calculate_total_points(self):
        #Fill the code for calculating the total points
        x = (20*self.get_amount())/100
        self.set_total_points(x)
    
    
    
    def calculate_balance(self,hours_to_play):
        #Fill the code here calculating the balance total points
        balance_point = (50*hours_to_play)
        # self.__total_points = self.__total_points - balance_point;
        if(self.__total_points < balance_point):
            return False
        else:
            self.__total_points = self.__total_points - balance_point
            return True
