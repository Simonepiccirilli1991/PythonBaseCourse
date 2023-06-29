from calculetor import square


def main():
    test_calc()

def test_calc():
    try:
        assert square(3) == 9
    except AssertionError:
        print("Error on line 9, assertion not true")

    try:
        assert square(7) == 64
    except AssertionError:
        print("Error on line 14, assertion not true square not equal 64")


if __name__ == "__main__":
    main()
