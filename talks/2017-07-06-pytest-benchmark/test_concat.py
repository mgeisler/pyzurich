def test_concat():
    foo = 'Hello'
    bar = 'World!'
    assert len(foo) + len(bar) == len('Hello, world')
