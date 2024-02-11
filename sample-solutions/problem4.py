from collections import deque

# def part1(expression: str) -> int:
#     return sum(int(x) for x in expression.split("+"))

# def eval_paren(tokens: list[str | int]):
#     if tokens[0] == "(":

def parse_mult(tokens: deque[int | str]):
    left = parse_subdiv(tokens)
    while tokens and tokens[0] == "*":
        tokens.popleft()
        left = left * parse_subdiv(tokens)
    return left

def parse_subdiv(tokens: deque[int | str]):
    left = parse_add(tokens)
    while tokens and tokens[0] in "-/":
        op = tokens.popleft()
        if op == "-":
            left = left - parse_add(tokens)
        else:
            left = left // parse_add(tokens)
    return left

def parse_add(tokens: deque[int | str]):
    left = parse_base(tokens)
    while tokens and tokens[0] == "+":
        tokens.popleft()
        left = left + parse_base(tokens)
    return left

def parse_base(tokens: deque[int | str]):
    # print(tokens)
    if tokens[0] == "(":
        tokens.popleft()
        res = parse_mult(tokens)
        assert tokens.popleft() == ")", "mismatched parenthesis"
        return res
    assert type(tokens[0]) == int
    return tokens.popleft()

def gettokens(expression: str):
    tokens = []
    last = ""
    for c in expression:
        if c in " \t":
            continue
        if c in "+-*/()":
            if last:
                tokens.append(int(last))
            tokens.append(c)
            last = ""
        else:
            last += c
    if last:
        tokens.append(int(last))
    return tokens

def calculate(expression: str) -> int:
    # your code here
    tokens = deque(gettokens(expression))

    return parse_mult(tokens)

if __name__ == "__main__":
    # sample cases

    print("Testing sample case 1 (part 1)...", end="")
    input1 = "1 + 4 + 7 + 2 + 492"
    output1 = 506
    try:
        assert calculate(input1) == output1
    except AssertionError:
        print("\nCase 1 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(calculate(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")

    print("Testing sample case 2 (part 2)...", end="")
    input1 = "1 - 2 / 7 + 2 + 492"
    output1 = -1
    try:
        assert calculate(input1) == output1
    except AssertionError:
        print("\nCase 2 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(calculate(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")

    print("Testing sample case 3 (part 3)...", end="")
    input1 = "5 - 2 / 2 * 2 + 1"
    output1 = 3
    try:
        assert calculate(input1) == output1
    except AssertionError:
        print("\nCase 3 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(calculate(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")

    print("Testing sample case 4 (part 4)...", end="")
    input1 = "6 - (8 / 2) * 2 + 2"
    output1 = 8
    try:
        assert calculate(input1) == output1
    except AssertionError:
        print("\nCase 4 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(calculate(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")