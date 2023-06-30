from calculetor import square
##posso usare una libreria per fare in test, pytest quindi la installo con pip e refactoro il codice in maniera seguente
#devo mettere test davanti come primo nome se no nn lo legge
def test_calculator():
    assert square(3) == 9
    assert square(7) == 49

#ora non ho bisogno nemmeno di settare il main, mi basta lanciare lo scypt col comando pytest nome scrypt e via
#posso settare piu test contemporaneamente
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0