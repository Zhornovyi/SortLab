def CountingSort(alist, largest, key):#key - функція визначення розряду сортування

    c = [0] * (largest + 1)#заповнюємо нулями масив підрахунків
    for i in range(len(alist)):
        c[key(alist, i)] = c[key(alist, i)] + 1

    # додавання індексів, пошук місця
    c[0] = c[0] - 1  # зменшуємо перший еоемент для початку відліку з нуля
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)
    for i in range(len(alist) - 1, -1, -1): # заповсення масиу результату з кінця
        result[c[key(alist, i)]] = alist[i]
        c[key(alist, i)] = c[key(alist, i)] - 1
    return result

def RadixSort(unsorted, base=10):# base - система числення
    if unsorted == []:
        return
    def key_factory(digit, base):#виділення розряду
        def key(alist, index):
            return ((alist[index] // (base ** digit)) % base)
        return key

    largest = max(unsorted)
    exp = 0 #номер найсильнішого розряду
    while base ** exp <= largest:
        sorted_a = CountingSort(unsorted, base - 1, key_factory(exp, base))
        exp = exp + 1
    return sorted_a

