class TestClass:
    '''
    :When grouping tests inside classes is that each test has a unique instance of the class.
    :Having each test share the same class instance would be very detrimental to test isolation and would promote poor test practices.
    '''
    def test_one(self):
        x = "this"
        assert "h" in x
    def test_two(self):
        x = "hello"
        # hasattr() returns true if an object has the given named attribute and false if it does not
        assert hasattr(x, "check")
    
class TestClassDemoInstance:
    def test_three(self):
        assert 0
    def test_four(self):
        assert 0
    def test_five(self):
        assert 0