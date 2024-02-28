from task4 import pass_gen
import string

def test_pass_gen_string():
    user = 8
    password = pass_gen(user)
    assert isinstance(password, str)

def test_pass_gen_length():
    user = 12
    password = pass_gen(user)
    assert len(password) == user

def test_pass_gen_check_requirements():
    user = 12
    password = pass_gen(user)
    all_chars = string.ascii_letters + string.digits + string.punctuation
    assert all(item in all_chars for item in password)

