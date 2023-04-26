handbook = {
    'mile': 1609,
    'yard': 0.9144,
    'foot': 30.48 / 100,
    'inch': 2.54 / 100,
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}

data = input().split()

numb = float(data[0])
from_units = data[1]
to_units = data[3]

result = numb * handbook[from_units] / handbook[to_units]
print(f"{result:.2e}")
