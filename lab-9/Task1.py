def sum_even_odd(numbers):
   
    even_sum = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return even_sum, odd_sum



if __name__ == "__main__":
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]
    even_sum, odd_sum = sum_even_odd(numbers)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")