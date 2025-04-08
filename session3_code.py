def f(x):
	result = x**3 + 8
	return result

def main():
	x = 9
	print(f(x))
	if f(x) > 27:
		print("YAY!")

main()