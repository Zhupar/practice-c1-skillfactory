from cat import Cat

cat1 = Cat('Baron', 'male', 2)
cat2 = Cat('Sam', 'male')


print(cat1.get_name())
print(cat1.get_gender())
print(cat1.get_age())
cat2.set_age(2)
print(cat2.get_name())
print(cat2.get_gender())
print(cat2.get_age())
