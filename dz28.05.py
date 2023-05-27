##2
def average_closure():
    numbers = []
    def add_number(number):
        numbers.append(number)
    def get_avg():
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    return add_number , get_avg
add_num , get_average = average_closure()
add_num(10)
add_num(5)
add_num(100)
print(get_average())