import check50

@check50.check()
def exists():
    """anagram.py exists"""
    check50.exists("hello.py")

@check50.check(exists)
def test_anagrams():
    """Correctly identifies anagrams"""
    check50.run("python3 hello.py")\
        .stdout("Hello World")\
        .exit(0)