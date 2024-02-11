## Problem 2. Unformatted Text File

Now you're ready to get started! You make your way to a dark corner in the back of the first floor of Donald Bren Hall. 
Oh? What's that? As an student in ICS, you've been in DBH plenty of times, but you never noticed a door in this 
particular spot before...

The door's unusually heavy, but you open it and... it's another door. There's something else in front of this second door
though, as if it's guarding what lies behind...

Professor Pattis left behind a cute little robot to watch over this door. You approach it and... it starts talking. 
It starts to say "Hello, it appears you've foun--" but then you hear static and the robot cuts off and appears to malfuntion.
It seems the robot's supposed to have some sort of message for you, but now, you can only make out what seems to be a seemingly 
random string of characters, followed by a brief pause, before it starts up again, with what you can only make out to be another
seemingly random string of characters, with the robot repeating this cycle.

You go past the robot and try to open the door. It's locked, and you notice a number pad next to the door frame. Looks like
you'll need a password.

As you listen to the robot, you notice that some of the characters you make out get repeated a seemingly random number 
of times, before it changes to what sems to be another character. You're not 100% sure why, but you think the number 
of times each character gets repeated is somehow important.

So, for each string in between the pauses, you decide to find the number of characters in the second-longest contiguous 
repetition of the same character, which you'll then enter into the keypad. Why this approach and why second-longest? 
You're not sure why either, but it somehow just feels like what Prof. Pattis would have wanted.


### The Task

Write a function `second_longest_contiguous(pattern: str) -> int` that takes in a string of characters, with each character
in the string being the character you make out from what the robot's saying in it's malfunctioning state. The input string 
will always have at least two distinct characters in it and will consist only of lowercase letters.

Return an integer representing the number of times the second-longest contiguous repetition of the same character gets 
repeated (see sample input/output below). If there is a tie for first-longest, then the second-longest is also the 
same as the first-longest (see sample input/output 2 below).

**Sample input:**
```
second_longest_contiguous("abbbcccccc")
```
**Sample output:** `3`

**Explanation:** The first-longest contiguous repetition of the same character is of the character 'c' which gets repeated 6 times. The second-longest contiguous repitition is of the character 'b' which gets repeated 3 times. Therefore, we return 3.

**Sample input 2:**
```
second_longest_contiguous("ddeeddddeeee")
```

**Sample output 2:** `4`

**Explanation:** There is a tie for the first-longest contiguous repetition of the same character; in other words, the
first and second-longest contiguous repetitions of the same character both repeat the respective character 4 times.
Thus, the second-longest contiguous repetition of the same character is among these two, so we return the number of
times each of these characters are contiguously repeated, which is 4.


With this function, you'll be able to enter onto the keypad the numbers the function returns when you give it the strings
of characters you hear from the robot.
