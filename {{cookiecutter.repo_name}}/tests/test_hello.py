from {{cookiecutter.project_name}}.hello import say_hello

def test_hello() -> None:
    assert say_hello() == 1
