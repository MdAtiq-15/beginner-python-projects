A random number is selected and the user has to guess the number

DIFFICULTY - 3/4

## Version Notes

### Version 1.0
    Random number is selected using __randint()__ method. User has to keep on guessing
    until it is correct. On each guess user is informed if the number entered is 
    'Too High!' or 'Too Low!' and the number of attempts is counted.

### Version 1.1
    I allowed the user to specify the minimum and maximum values for the number
    range before the game starts. This gives the player more control over the
    difficulty level. 

### Version 1.2
    __try except__ is added to handle invalid input. Code in the last version was not 
    clean and had some repeated lines. It had an issue with not stopping when 
    **user_attempts == max_attempts** and so it was set to 1 at start just for it to work
    properly. 
    **It is now cleaner and more readable**