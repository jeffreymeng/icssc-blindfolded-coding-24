# Problem 4. Calculations

**_Note: This problem has multiple stages, each of which awards some partial credit._**

You've finally made it to the final door! Through the small window slit, you can
see the treasure in front of you -- you just have to get in. The door has a interesting
keypad next to it. Upon further analysis, it seems like the door doesn't care
about the identity of the person trying to open it, only their abilities!

Unfortunately, the door seems to care about _mathematical_ ability. It has a display
with a big mathematical expression on it (such as `4 + 7 / 2 - (4 * 3)`), and a keypad for you to input an answer.
You look closer, and discover even more bad news: it turns out this door doesn't follow
the normal rules of mathematical evaluation.

Fortunately, there's a handy instruction manual describing the door's weird version of math:
1. Just like in normal math, a parentheses creates a new group that's evaluated first
2. Next, all _addition_ is evaluated before any other operators, left to right
3. After addition, _subtraction_ and _division_ is performed, left to right with equal 
precedence. **The division operator performs integer division -- that is, it always rounds its result down.**
4. Finally, multiplication is performed, left to right.

As an example, the expression `4 + 7 / 2 - (4 * 3)` can be simplified as follows:
```
4 + 7 / 2 - (4 * 3) # initial expression
4 + 7 / 2 - 12      # parenthesis first
11 / 2 - 12         # addition comes next
5 - 12              # then integer division
-7                  # finally, subtraction (because it's after division)
```

## The Tasks
Since the expressions are too big to do by hand, it looks like you'll have
to implement a calculator to solve it for you, step by step.

_Note: The inputs will only contain positive integers, but the answer may be negative._

### Step 1. Addition (20%)
To start off, implement your calculator for expressions with just numbers and addition.

##### Sample Input
```
1 + 4 + 7 + 2 + 492
```
Output: `506`

### Step 2. Subtraction and Division (30%)
Next, implement the calculator for subtraction and division.
##### Sample Input
```
1 - 2 / 7 + 2 + 492
```
Output: `-1`
Explanation:
```
1 - 2 / 7 + 2 + 492
1 - 2 / 501
-1 / 501
-1         # floor the result
```

### Step 3. Multiplication (20%)
Next, implement the calculator for multiplication.
##### Sample Input
```
5 - 2 / 7 * 2 + 1
```
Output: `3`
Explanation:
```
5 - 2 / 2 * 2 + 1
5 - 2 / 2 * 3
3 / 2 * 3
1 * 3
3
```

### Step 4. Parenthesis (30%)
Finally, implement your calculator for parenthesis, and you'll be done!
##### Sample Input
```
6 - (8 / 2) * 2 + 2
```
Output: `8`
Explanation:
```
6 - 4 * 2 + 2
6 - 4 * 4
2 * 4
8
```
