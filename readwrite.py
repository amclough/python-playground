# read name.txt into a variable my_name
# write the new file named hello.txt with the contents "Hello my name is ___"

with open('name.txt') as f:
    my_name = f.read()


with open('hello.txt', 'w') as f:
    f.write('hello, my name is ' + my_name)
    f.write('\n')
   
