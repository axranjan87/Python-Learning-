#@ Set is a collection of non-repetitive elements

s = set()     #@no repetition allowed
s.add(1)
s.add(2)      #@ or set = {1,2}

"""
1. Sets are unordered => elements order does not matter
2. sets are unindexed => cannot access elements by index
3. there is no way to change items in sets
4. sets cannot contain duplicates values


@operation on sets
s = {1,8,2,3}

1. len(s) = return 4, the length of sts
2. s.remove(8) = updates the set s and remove 8 from s
3. s.pop() = remove an arbitrary element from the set and return the element removed
4. s.clear() = empties the set s
5. s.union({8,11}): returns a new set with all oiitems from both sets{1,8,2,3,11}
6. s.intersection({8,11}): return a set which contains only item in both sets{8}

"""


s = {1,5,32,58,5,5,5,"Ayush"}

print(s,type(s))

s.add(522)
print(s,type(s))
s.remove(1)

s1 = {1,45,6,78}
s2 = {7,8,1,78}

print(s1.union(s2))
print(s1.intersection(s2)) #@for common values