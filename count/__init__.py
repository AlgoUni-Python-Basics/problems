import check50

@check50.check()
def exists():
    """count.py exists"""
    check50.exists("count.py")

@check50.check(exists)
def test_homer():
    """input of 'Homer' yields output 'Homer has 5 characters.'"""
    check50.run("python3 count.py").stdin("Homer").stdout("Homer has 5 characters.", regex=False).exit(0)

@check50.check(exists)
def test_empty_string():
    """input of '' yields output ' has 0 characters.'"""
    check50.run("python3 count.py").stdin("").stdout(" has 0 characters.", regex=False).exit(0)

@check50.check(exists)
def test_long_string():
    """input of 'Supercalifragilisticexpialidocious' yields output 'Supercalifragilisticexpialidocious has 34 characters.'"""
    check50.run("python3 count.py").stdin("Supercalifragilisticexpialidocious").stdout("Supercalifragilisticexpialidocious has 34 characters.", regex=False).exit(0)


@check50.check(exists)
def test_algouni():
    """input of 'algouni 2023' yields output 'Homer has 12 characters.'"""
    check50.run("python3 count.py").stdin("Algouni 2024").stdout("Algouni 2024 has 12 characters.", regex=False).exit(0)

@check50.check(exists)
def test_algouni_empty_spaces():
    """input of '  algouni  ' yields output '  algouni   has 11 characters.'"""
    check50.run("python3 count.py").stdin("  algouni  ").stdout("  algouni   has 11 characters.", regex=False).exit(0)