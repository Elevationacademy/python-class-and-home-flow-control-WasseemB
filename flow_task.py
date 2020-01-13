def my_enumerate(obj):
    for i in range(len(obj)):
        yield i, obj[i]


def my_reduce(function, sequence, initial=0):
    return sequence[initial] + function(sequence[initial + 1:])


def my_accumulate(sequence):
    n_sequence = list()
    for i in range(1, len(sequence) + 1):
        n_sequence.append(my_reduce(sum, sequence[:i]))
    return n_sequence


def fizzbuzz(n):
    for i in range(n):
        output = ""
        if i % 3 == 0:
            output += ("fizz")
        if i % 5 == 0:
            output += ("buzz")
        print(output or i)


list_test = ["Car", "Boy", "Block"]
iter_list = my_enumerate(list_test)
print(list(iter_list))

num_test = [1, 2, 3, 4, 5]
print(my_reduce(sum, num_test))

acc_list = [1, 2, 3, 4, 5]
print(my_accumulate(num_test))

fizzbuzz(15)
