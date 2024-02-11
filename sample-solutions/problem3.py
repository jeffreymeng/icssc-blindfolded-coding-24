import random
def max_rest_time(guards: list[tuple[int, int]]):
    return min(time - position/4 for time, position in guards)

if __name__ == "__main__":
    # sample cases -- you can modify, remove, or leave these statements in

    print("Testing sample case 1...", end="")
    input1 = [(130, 80), (250, 120)]
    output1 = 110
    try:
        assert max_rest_time(input1) == output1
    except AssertionError:
        print("\nCase 1 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(max_rest_time(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")