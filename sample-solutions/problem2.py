def second_longest_contiguous(pattern: str) -> int:
    first_longest_count = 0
    second_longest_count = 0

    count = 1
    prev_char = None
    for char in pattern+' ':
        if char == prev_char:
            count += 1
        else:
            if count >= first_longest_count:
                second_longest_count = first_longest_count
                first_longest_count = count
            elif count > second_longest_count:
                second_longest_count = count
            count = 1
        prev_char = char

    return second_longest_count


if __name__ == "__main__":
    # sample cases -- you can modify, remove, or leave these statements in

    print("Testing sample case 1...", end="")
    input1 = "abbbcccccc"
    output1 = 3
    try:
        assert second_longest_contiguous(input1) == output1
    except AssertionError:
        print("\nCase 1 was not correct")
        print("Expected: ", repr(output1))
        print("Your answer: ", repr(second_longest_contiguous(input1)))
        print()
    except Exception as e:
        raise e
    else:
        print("Passed!")

    print("Testing sample case 2...", end="")
    input2 = "ddeeddddeeee"
    output2 = 4
    try:
        assert second_longest_contiguous(input2) == output2
    except AssertionError:
        print("\nCase 2 was not correct")
        print("Expected: ", repr(output2))
        print("Your answer: ", repr(second_longest_contiguous(input2)))
    except Exception as e:
        raise e
    else:
        print("Passed!")
