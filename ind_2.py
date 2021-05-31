#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
# В списке, состоящем из вещественных элементов, вычислить:
# 1) максимальный по модулю элемент списка;
# 2) сумму элементов списка, расположенных между первым и вторым положительными
# элементами.
# Преобразовать список таким образом, чтобы элементы, равные нулю, располагались после всех
# остальных.

if __name__ == '__main__':
    import math
    from random import random

    if __name__ == '__main__':
        # номер минимального по модулю элемента списка
        m = 0
        u = list(map(float, input('Введите вещественные числа -->').split()))
        a = abs(max(u))
        for i in u:
            if abs(i) > a:
                m = i
        print(m)
        # сумму модулей элементов списка, расположенных после первого отрицательного элемента
        s = 0
        neg = 1
        for i, n in enumerate(u):
            if n > 0:
                neg = i
                break

        for n in u[neg + 1:]:
            s += abs(n)

        print(s)

        # Сжать список, удалив из него все элементы, величина которых находится в интервале [а, b].

        import random
        from random import randint

        N = 10
        mass = [random.randint(0, 2) for i in range(N)]
        print(mass)

        start = next(i for i, x in enumerate(mass) if x == 0)
        p = mass[:start]
        c = mass[start:]

        print([0]*mass.count(0) + [x for x in mass if x!=0])