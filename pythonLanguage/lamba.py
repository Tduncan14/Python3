

# sub = lambda n,m : n - m


# print(sub(19,4))



lst = [12,45,343,343,23,2,423,45,64]



def remove_dup(L):
     unique = set(L)
     u = list(unique)
     u.sort()
     return u


print(lst)
print(remove_dup(lst))