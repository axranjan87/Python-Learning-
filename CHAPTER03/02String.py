""" @Slicing"""

name = "Ayush"
print(name[0:3])

print(name[-4:-1])
print(name[1:4])

print(name[:4]) #@ is same as print(name[0:4])
print(name[1:]) #@ is same as print(name[1:5])


""" @ Slicing with skip value """

word = "amazing"

print(word[1:6:2])  #mzn

""" @other advanced slicing techniques  """

word = "amazing"
print(word[:7])   #word[0:7] - 'amazing'
print(word[0:]) 