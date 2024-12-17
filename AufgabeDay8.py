'''Life in Weeks
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.'''

def life_in_weeks(age):
    total = 365*90/7
    current = 365*age/7
    div =int(total - current)
    return div 

'''Love Calculator
💪 This is a difficult challenge! 💪 
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"
T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 
Total = 5 
L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 
Love Score = 53'''

def calculate_love_score(name1, name2):
    # Combine the names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of letters in "TRUE"
    true_count = sum(combined_names.count(letter) for letter in "true")
    
    # Count occurrences of letters in "LOVE"
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    # Combine the counts to form a two-digit love score
    love_score = int(f"{true_count}{love_count}")
    
    # Print the love score
    print(love_score)

# Example usage
calculate_love_score("Kanye West", "Kim Kardashian")



