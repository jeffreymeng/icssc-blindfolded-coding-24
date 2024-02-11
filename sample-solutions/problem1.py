
def warm_up() -> None:
    print("hELLO wORLD11")
    print(":sunglasses:")
    print(min(420 ** 5, 42 ** 42, 5 ** 420))
    print((8 * 70 + 1965)/5)
    print('type the wrods "I\'m a big kid now!" then move on :)')



if __name__ == "__main__":
    # sample cases -- you can modify, remove, or leave these statements in

    print("Testing first print statement...\n")
    # we use __import__ to prevent issues if the import statement at the top is deleted
    with __import__("contextlib").redirect_stdout(__import__("io").StringIO()) as f:
        warm_up()
    s = f.getvalue()
    print(s)

    assert s.split("\n")[0] == "hELLO wORLD11"
    print("Passed!")

