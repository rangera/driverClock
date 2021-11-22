from compliance_clock import create_app

def test_create():
    assert not create_app().testing
    assert create_app({'TESTING':True}).testing
