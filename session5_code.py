import numpy as np
import tabulate

def data():
    x_values = np.linspace(0, 2 * np.pi, 1000)
    sin_values = np.sin(x_values)
    data = list(zip(x_values, sin_values))
    return data

def main():
    data_for_table = data()
    headers = ["x", "sin(x)"]
    print(tabulate.tabulate(data_for_table, headers=headers, tablefmt="fancy_grid", floatfmt=".6f"))

if __name__ == "__main__":
    main()