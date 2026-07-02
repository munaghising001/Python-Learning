# list
# keywords are mutable, duplicate, ordered, heterogenous
# mutable: an object's value can be changed after creation
# duplicate: used to store multiple values so duplicate means same value occuring multiple times.
# ordered: maintains ordered data structure mainstains the sequence of elements as they were inserted.
# Heterogenous: we can have multiple data types inside the list


# a = "hello"

# print(a[0])

# list traversing and methods

# a = [12, 13, 14, 15, 16, 34, 5]

# list way using index

# for i in range(len(a)):
#     print(a[i])


# # 2nd way directly on values

# # for i in a:
# #     print(i)


# print(dir(list))

# mean of element

l = [12,435,67,89,23,25]

sum = 0

for i in l:
    sum = sum + i

print(sum/len(l))
