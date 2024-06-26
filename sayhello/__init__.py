import check50


@check50.check()
def exists():
    """sayhello.py exists"""
    check50.exists("sayhello.py")

@check50.check(exists)
def testolasha():
    """input of Lahsa yields output of 'Hello, Lasha, nice to meet you!'"""
    check50.run("python3 sayhello.py").stdin("Lasha", prompt=True).stdout("Hello, Lasha, nice to meet you!").exit()

@check50.check(exists)
def testgiorgi():
    """input of Giorgi yields output of 'Hello, Giorgi, nice to meet you!'"""
    check50.run("python3 sayhello.py").stdin("Giorgi", prompt=True).stdout("Hello, Giorgi, nice to meet you!").exit()

@check50.check(exists)
def testalgouni():
    """input of algouni yields output of 'Hello, algouni, nice to meet you!'"""
    check50.run("python3 sayhello.py").stdin("Algouni", prompt=True).stdout("Hello, Algouni, nice to meet you!").exit()