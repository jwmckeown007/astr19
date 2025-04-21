def f(x):
	result = x**3 + 8
	return result

def main():
	x = 9
	output = f(x)
	print(output)
	if output > 27:
		print("YAY!")

if __name__ == "__main__":
	main()
