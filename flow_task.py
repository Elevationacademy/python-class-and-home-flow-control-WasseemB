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


def mult_table(n, size=10):
    for i in range(size + 1):
        print(f"{i} x {n} = {i * n} ")


def mult_table_to(n, size):
    for i in range(size + 1):
        for j in range(n + 1):
            print(f"{i} x {j} = {i * j}")


def password_validation(string: str):
    special_char = ["$", "#", "!", "%", "@"]
    lower_count = sum([word.islower() for word in string]) >= 4
    upper_count = sum([word.isupper() for word in string]) >= 2
    digit_count = sum([word.isdigit() for word in string]) >= 1
    string_len = 8 <= len(string) <= 20
    special_char_count = sum([any(x in string for x in special_char)]) >= 1
    return [True if lower_count and upper_count and digit_count and string_len and special_char_count else False]


list_test = ["Car", "Boy", "Block"]
iter_list = my_enumerate(list_test)
print(list(iter_list))

num_test = [1, 2, 3, 4, 5]
print(my_reduce(sum, num_test))

acc_list = [1, 2, 3, 4, 5]
print(my_accumulate(num_test))

fizzbuzz(15)
print(password_validation("wasseem"))
print(password_validation("WAsseem@2010"))

mult_table(5)
print()
mult_table_to(5, 5)


