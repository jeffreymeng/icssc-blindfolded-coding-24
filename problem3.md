# Problem 3. Running from the guards 

You make it past the door, and you now arrive at a long hallway. Suddenly, an alarm sounds! The guards are coming!
Luckily, your friend has gathered intel on when the guards will get to each location, and has relayed this information to you. 
Through alternative passageways, the guards will soon arrive to junctions along your hallway and block you off. However, 
it seems the guards are quite slow, and it will take each some time to get to their destination! You can easily get to 
safety before all of the guards arrive, but you’re still tired from your previous escapades, so you want to take a 
break for a while.

Imagine the hallway as a number line. You’re currently at x=0m, and your group can run at a speed of 4 meters per second.
Given a list of tuples (time, position), where the first element represents the time in seconds it will take for the guard 
to get to its location and start blocking you, and the second parameter represents the x-coordinate along the hallway the 
guard will arrive at, in meters, what's the largest number of seconds you can rest for while still making it past all the 
guards? Assume that if you arrive at a location at the same time as a guard, you narrowly escape the guard. 

It's guaranteed that you will always be able to escape with some non-negative rest time.

## The Task

Write a function `max_rest_time(guards: list[tuple[int, int]])` to return the maximum rest time as an Integer.

**Sample Input:**

```
[(130, 80), (250, 120)]
```

This input means that after 130 seconds from now, the first guard will be blocking the hallway at x = 80m. After 250 seconds
from now, the second guard will be blocking the hallway at x = 200m.

**Sample Output:** `110`

Assume it is currently `t = 0` seconds.

In order to safely make it past all the guards, you must at `t = 110` (so you get 110 seconds of rest). 
You’ll reach x = 80m after 20 seconds of running (`t = 130`), just barely escaping the first guard. Then 
you’ll reach x = 120m after 10 more seconds (`t = 140`), very comfortably missing the second guard and making
it to safety!
