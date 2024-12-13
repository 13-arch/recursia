sp=[1,2,3,4,5]
def search_max(a):
    if len(a) == 0:
        return 0
    return a[0] if a[0] > search_max(a[1:]) else search_max(a[1:])
print(search_max(sp))