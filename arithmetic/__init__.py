import check50


@check50.check()
def exists():
    """arithmetic.py exists"""
    check50.exists("arithmetic.py")

@check50.check(exists)
def testSample():
    """input of 5 and 5 yields output of 'Sum: 10 Difference: 0 Product: 25 Quotient: 1.0'"""
    check50.run("python3 arithmetic.py")\
        .stdin("5", prompt=True)\
        .stdin("5", prompt=True)\
        .stdout("Sum: 10\nDifference: 0\nProduct: 25\nQuotient: 1.0").exit()

@check50.check(exists)
def testSample2():
    """input of 5 and 5 yields output of 'Sum: 10 Difference: 0 Product: 25 Quotient: 1.0'"""
    check50.run("python3 arithmetic.py")\
        .stdin("12", prompt=True)\
        .stdin("6", prompt=True)\
        .stdout("Sum: 18\nDifference: 6\nProduct: 72\nQuotient: 2.0").exit()