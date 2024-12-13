spisok = [1, 2, 3, 4, 5]
def sum(a):
    if len(a)==0:
        return 0
    return sum(a[1:])+a[0]
print(sum(spisok))