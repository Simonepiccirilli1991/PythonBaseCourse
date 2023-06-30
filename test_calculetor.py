from calculetor import square


def main():
    test_calc()

def test_calc():
    try:
        assert square(3) == 9
    except AssertionError:
        print("Error on line 9, assertion not true")

    try:
        assert square(7) == 49
    except AssertionError:
        print("Error on line 14, assertion not true square not equal 64")


if __name__ == "__main__":
    main()


##posso usare una libreria per fare in test, pytest quindi la installo con pip e refactoro il codice in maniera seguente
def pytest_calculator():
    assert square(3) == 2
    assert square(7) == 49

#ora non ho bisogno nemmeno di settare il main, mi basta lanciare lo scypt col comando pytest nome scrypt e via

