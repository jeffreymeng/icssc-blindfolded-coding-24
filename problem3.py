def navigate_maze0() -> list:

    maze0 = ['RIGHT', 'DOWN', 'RIGHT', 'DOWN'] #sample solution to example maze
    return maze0

def navigate_maze1() -> list:
    pass #your code here

def navigate_maze2() -> list:
    pass #your code here

if __name__ == "__main__":

    # sample cases -- you can modify, remove, or leave these statements in
    # This only checks for the first maze, but can give you an idea on how things are tested

    try:
        assert navigate_maze0() == ['RIGHT', 'DOWN', 'RIGHT', 'DOWN']
    except Exception as e:
        raise e
    else:
        print("Passed!")