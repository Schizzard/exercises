# Step 6

Y = int(input())
print('Високосный' if (not Y%4 and Y%100) or not Y%400 else 'Обычный')