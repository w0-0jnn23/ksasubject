import check

def gongtong(a, b):
    a_set = set(check.check(a)[0])
    b_set = set(check.check(b)[0])
    
    gong = a_set & b_set
    return gong