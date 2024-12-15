import numpy as np

def input_matrices():
    size = int(input("Введите размер матриц: "))
    matrix1 = []
    matrix2 = []
    
    print("Введите элементы первой матрицы:")
    for i in range(size):
        row = list(map(int, input().split()))
        if len(row) != size:
            print("Ошибка: количество элементов в строке должно быть равно размеру матрицы.")
            return None, None
        matrix1.append(row)
    
    print("Введите элементы второй матрицы:")
    for i in range(size):
        row = list(map(int, input().split()))
        if len(row) != size:
            print("Ошибка: количество элементов в строке должно быть равно размеру матрицы.")
            return None, None
        matrix2.append(row)
    
    return np.array(matrix1), np.array(matrix2)

def add_matrices(matrix1, matrix2):
    return matrix1 + matrix2

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def main_menu():
    matrix1 = matrix2 = None
    result_matrix = None
    determinant_matrix1 = None
    determinant_matrix2 = None

    while True:
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")

        if choice == '4':
            break
        elif choice == '1':
            matrix1, matrix2 = input_matrices()
        elif choice == '2':
            if matrix1 is not None and matrix2 is not None:
                result_matrix = add_matrices(matrix1, matrix2)
                determinant_matrix1 = calculate_determinant(matrix1)
                determinant_matrix2 = calculate_determinant(matrix2)
            else:
                print("Сначала введите матрицы.")
        elif choice == '3':
            if result_matrix is not None:
                print("Сумма матриц:\n", result_matrix)
                print("Определитель первой матрицы:", determinant_matrix1)
                print("Определитель второй матрицы:", determinant_matrix2)
            else:
                print("Сначала выполните алгоритм.")

def input_matrices():
    size = int(input("Введите размер матриц: "))
    matrix1 = []
    matrix2 = []

    print("Введите элементы первой матрицы:")
    for i in range(size):
        row = list(map(int, input().split()))
        if len(row) != size:
            print("Ошибка: количество элементов в строке должно быть равно размеру матрицы.")
            return None, None
        matrix1.append(row)

    print("Введите элементы второй матрицы:")
    for i in range(size):
        row = list(map(int, input().split()))
        if len(row) != size:
            print("Ошибка: количество элементов в строке должно быть равно размеру матрицы.")
            return None, None
        matrix2.append(row)

    return np.array(matrix1), np.array(matrix2)

def add_matrices(matrix1, matrix2):
    return matrix1 + matrix2

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def main_menu():
    matrix1 = matrix2 = None
    result_matrix = None
    determinant_matrix1 = None
    determinant_matrix2 = None

    while True:
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")

        if choice == '4':
            break
        elif choice == '1':
            matrix1, matrix2 = input_matrices()
            if matrix1 is None or matrix2 is None:
                print("Ошибка ввода матриц. Попробуйте снова.")
        elif choice == '2':
            if matrix1 is not None and matrix2 is not None:
                result_matrix = add_matrices(matrix1, matrix2)
                determinant_matrix1 = calculate_determinant(matrix1)
                determinant_matrix2 = calculate_determinant(matrix2)
            else:
                print("Сначала введите матрицы.")
        elif choice == '3':
            if result_matrix is not None:
                print("Сумма матриц:\n", result_matrix)
                print("Определитель первой матрицы:", determinant_matrix1)
                print("Определитель второй матрицы:", determinant_matrix2)
            else:
                print("Сначала выполните алгоритм.")

if __name__ == "__main__":
    main_menu()

