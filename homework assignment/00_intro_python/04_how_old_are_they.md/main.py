#Problem Statement:

# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

# Anton is 3

# Beth is 4

# Chen is 5

# Drew is 6

# Ethan is 7

#Solution:

def main():
    anton: int = 21  # Anton's age is given as 21 years old
    beth: int = anton + 6  # Beth is 6 years older than Anton
    chen: int = beth + 20  # Chen is 20 years older than Beth
    drew: int = chen + anton  # Drew is Chen's age plus Anton's age
    ethan: int = chen  # Ethan is the same age as Chen

    # Print out all of the ages!
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))


# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()

