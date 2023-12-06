#created by shubh
from array import array

# Creating an array of integers
int_array = array('i', [10, 20, 30, 40, 50])  # 'i' specifies the type code for integers

# Displaying array items using indexes
print("Array items:")
for i in range(len(int_array)):
    print(f"Index {i}: {int_array[i]}")
