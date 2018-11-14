def many(*args, **kwargs):
    print(args)
    print(kwargs)
    
many(1, 2, 3, name="Mike", job="programmer")