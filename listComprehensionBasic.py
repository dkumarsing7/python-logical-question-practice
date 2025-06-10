square = [ x**2 for x in range(1,5)]
even = [x for x in range(20) if x%2==0]

names = ["deep", "manasvini", "divanshu"]
capitalName = [ name.upper() for name in names]

text = "H3ll0 W0rld 2025"
digit = [int(char) for char in text if char.isdigit()]
print(digit)