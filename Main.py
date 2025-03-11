my_list = [1,2,3,4,5,6,7,8,9]
my_list[0] = 11
my_list.append(10)
print(my_list)
print(len(my_list))
print(my_list.index(5))

my_tuple = (1,2,3,4,5,6,7,8,9,3,3)
print(my_tuple.count(3))

my_set = {1,2,None,3,4,False,5,6,7,8,9,3,3}
my_set.add(55)
print(my_set)

my_dict = {"key1": "value1", "key2": "value1" }
my_dict["key1"] = "myvalue"
my_dict["key3"] = "myvalue3"
print(my_dict.items())
