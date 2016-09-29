
import string

#input: a base for the user input n to take
#returns: the decimal form of the user's number in base n
def base_to_decimal(n):
     base_n_number = raw_input("Enter a number that has the base of input n: ")
     base_n_number = base_n_number[::-1]
     total_decimal_count = 0
     for index, i in enumerate(base_n_number):
          coeff = int(i)
          temp_decimal_count = (coeff) * pow(n, index)
          total_decimal_count += temp_decimal_count
     return total_decimal_count

print base_to_decimal(2)
