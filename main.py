def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Условие меняется в зависимости от выбранного направления сортировки
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Запрашиваем у пользователя количество чисел
    n = int(input("Введите количество чисел для сортировки: "))
    numbers = []

    # Ввод чисел с клавиатуры
    for i in range(n):
        num = int(input(f"Введите число {i + 1}: "))
        numbers.append(num)

    # Запрашиваем направление сортировки
    direction = input("Введите направление сортировки (введите 'возрастание' или 'убывание'): ").strip().lower()
    ascending = True if direction == "возрастание" else False

    # Сортируем массив пузырьковым методом в выбранном направлении
    bubble_sort(numbers, ascending)

    # Выводим отсортированный список
    print("Отсортированные числа:", numbers)

if __name__ == "__main__":
    main()
