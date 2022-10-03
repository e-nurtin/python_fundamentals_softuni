first_original_int = int(input())
second_original_int = int(input())

print("Before:")
print(f"a = {first_original_int}")
print(f"b = {second_original_int}")
temporary_var = first_original_int
first_original_int = second_original_int
second_original_int = temporary_var
print("After:")
print(f"a = {first_original_int}")
print(f"b = {second_original_int}")