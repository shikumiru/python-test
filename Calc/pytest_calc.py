from calc import Calc

def test_add():
    assert Calc().add(1, 2) == 3
    
def test_minus():
    assert Calc().minus(3, 2) == 1
    
def test_multiply():
    assert Calc().multiply(1, 2) == 2
    
def test_divide():
    assert Calc().divide(8, 2) == 4