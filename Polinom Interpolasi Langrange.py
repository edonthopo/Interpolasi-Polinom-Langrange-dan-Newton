# Data yang diberikan
tegangan = [5, 10, 15, 20, 25, 30, 35, 40]
waktu_patah = [40, 30, 25, 40, 18, 20, 22, 15]

# Fungsi untuk menghitung polinom Lagrange
def lagrange_interpolation(x, x_values, y_values):
    result = 0.0
    for i in range(len(y_values)):
        term = y_values[i]
        for j in range(len(y_values)):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

# Fungsi untuk mencetak hasil interpolasi
def print_interpolation_results(x_values, y_values):
    print("x\tInterpolasi Langrange")
    print("-------------------------")
    for x in range(5, 41):
        y_interpolated = lagrange_interpolation(x, x_values, y_values)
        print(f"{x}\t{y_interpolated:.2f}")

# Mencetak hasil interpolasi untuk rentang x dari 5 hingga 40
print_interpolation_results(tegangan, waktu_patah)
