from hello import hello

def test_default():
    assert hello() == "hello, world"


def test_value():
    assert hello("Simone") == "hello, Simone"

def test_list():
    for x in ["Harry", "Hermione", "Ron"]:
        assert hello(x) == f"hello, {x}"
