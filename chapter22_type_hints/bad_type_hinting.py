# bad_type_hinting.py

def my_function(a: str, b: str) -> None:
    return a.keys() + b.keys()
