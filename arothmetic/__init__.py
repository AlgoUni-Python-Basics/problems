import check50


@check50.check()
def exists():
    """arithmetic.py exists"""
    check50.exists("arithmetic.py")

@check50.check(exists)
def testgiorgi():
    """input of Giorgi yields output of 'Hello, Giorgi, nice to meet you!'"""
    check50.run("python3 arithmetic.py").stdin("Giorgi", prompt=True).stdout("Hello, Giorgi, nice to meet you!").exit()

@check50.check(exists)
def testalgouni():
    """input of algouni yields output of 'Hello, algouni, nice to meet you!'"""
    check50.run("python3 arithmetic.py").stdin("Algouni", prompt=True).stdout("Hello, Algouni, nice to meet you!").exit()