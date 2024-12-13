def reverse(a):
    if len(a)==0:
        return a
    return reverse(a[1:])+a[0]
print(reverse('qwerty'))