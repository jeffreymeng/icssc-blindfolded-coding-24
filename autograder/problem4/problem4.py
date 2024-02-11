

def calculate(expression: str) -> int:
    # your code here
    pass


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
    input1 = "5 - 2 / 7 * 2 + 1"
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