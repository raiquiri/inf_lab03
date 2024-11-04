def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Запрашиваем у пользователя количество чисел
    n = int(input("Введите количество чисел для сортировки: "))
    numbers = []

    # Ввод чисел с клавиатуры
    for i in range(n):
        num = int(input(f"Введите число {i + 1}: "))
        numbers.append(num)

    # Сортируем массив пузырьковым методом
    bubble_sort(numbers)

    # Выводим отсортированный список
    print("Отсортированные числа:", numbers)

if __name__ == "__main__":
    main()