import time
from multiprocessing import Pool, cpu_count

# Синхронна
def factorize_number(num): # Функція одного числа
    divisors = []
    for i in range(1, num + 1): # Перевірка чисел от 1 до num
        if num % i == 0: # Якщо без остачі
            divisors.append(i) # Додаємо до списку
    return divisors


def factorize(*numbers): # Для декілька чисел
    result = []
    for num in numbers:
        result.append(factorize_number(num))
    return result


def factorize_parallel(numbers): # Паралельна
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize_number, numbers)
    return results


if __name__ == '__main__':
    print(f"Дільники числа: {factorize_number(10)}") # Перевіряємо одного числа

    numbers = [128, 255, 99999, 10651060]

    # Синхронна
    start = time.time() # Початок
    a, b, c, d  = factorize(*numbers)
    end = time.time() # Кінець
    print(f"Час виконання (синхронно): {end - start:.2f} секунд")

    # Перевірка
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530,
                 10651060]

    # Паралельна
    print(f"Кількість ядер: {cpu_count()}")

    start = time.time()
    a, b, c, d = factorize_parallel(numbers)
    end = time.time()
    print(f"Час виконання (паралельно): {end - start:.2f} секунд")
