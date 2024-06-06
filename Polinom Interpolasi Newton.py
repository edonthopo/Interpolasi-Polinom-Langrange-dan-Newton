# Data yang diberikan
tegangan = [5, 10, 15, 20, 25, 30, 35, 40]
waktu_patah = [40, 30, 25, 40, 18, 20, 22, 15]

# Fungsi untuk menghitung koefisien Newton
def divided_differences(x_values, y_values):
    n = len(x_values)
    coef = y_values[:]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x_values[i] - x_values[i - j])
    return coef

# Fungsi untuk menghitung polinom Newton
def newton_interpolation(x, x_values, y_values):
    coef = divided_differences(x_values, y_values)
    n = len(x_values)
    result = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term
    return result

# Fungsi untuk mencetak hasil interpolasi
def print_interpolation_results(x_values, y_values):
    print("x\tInterpolasi Newton")
    print("-------------------------")
    for x in range(5, 41):
        y_interpolated = newton_interpolation(x, x_values, y_values)
        print(f"{x}\t{y_interpolated:.2f}")

# Mencetak hasil interpolasi untuk rentang x dari 5 hingga 40
print_interpolation_results(tegangan, waktu_patah)
