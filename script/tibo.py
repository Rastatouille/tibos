
def inter(l1,l2):
    return sorted(list(set(l1) & set(l2)))

def tailleInter(l1,l2):
    return len(inter(l1,l2))