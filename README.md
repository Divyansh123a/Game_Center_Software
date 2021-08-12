# Game_Center_Software
Fun Unlimited Game Center
Expected completion time: 30 minutes

Nolan and his friends plan to start a new video game center. They plan to give an access card to their customers to play the game. Create a Python application and help them to manage their business.

Create a class 'PlayCard'  (template given) with the following private member variables:
card_number  - data should be an integer value
 holder_name  -  data should a string value
 amount  -  data should be a float value
 total_points - data should be a float value
Include appropriate getter and setter methods in the PlayCard class.

Write the following methods in the PlayerCard class:
1. calculate_total_point() :  This method should set the value for the total_points. Calculate the total_points as 20% of the amount.  When someone plays a game in the GameCenter, points should be deducted from the card.
2. calculate_balance(hours_to_play) : This method should take hours_to_play as an argument and deduct the points for playing from the total points .  The points to be deducted are calculated as: total_points-(50*hours_to_play).  If the points for playing is greater than the total points, then the function should return 'False' else set the balance points to the total points and return 'True'.  If the calculate_balance() method returns 'True', then  display the total points , else display the message “You need more amount to play”. 

The file 'main.py' should contain a method : 'get_player_details()' which gets necessary details from the user as specified in the sample input statements and set these details into a player card object using  a parameterized constructor with 3 arguments and return the object .   Then using this object invoke necessary methods and  prints the details as shown in the sample output statements.

Refer the sample input and output statements for more clarifications.



Note:
Strictly follow the naming conventions for the class, member variable and functions.
Templates for the files: main.py and player.py are given.  Fill only the necessary parts alone.

Sample Input 1:
Enter Card Number: 101
Enter Holder Name: Adam
Enter Amount: 500
Enter Hours Want to Play: 1


Sample Output 1:
Balance is 50.00


Sample Input 2:
Enter Card Number: 105
Enter Holder Name: Alex
Enter Amount: 2500
Enter Hours Want to Play: 11

Sample Output 2:
You need more amount to play

Core Programming
General
Unix Fundamentals and Scripting
File System
Filters
Vi Editor
Bourne Shell
Python programming - Course Introduction
Introduction to Python
Control Structures
Lists,Tuples and Dictionaries
Functions and Modules
Working with Files
Class and Objects
Challenge Yourself!
Python References
Help Desk
Dashboard
Performance Dashboard
Help Desk
FAQs
Discussion Community
Practice editor
      
