#!/usr/bin/env python3
"""
Читаем из stdin

Пишем в stdout

Считать размеры
  h : int
  w : int
  h, w >= 1
Считать матрицу 1
  a : [[int]]
Считать матрицу 2
  b : [[int]]
Сложить матрицы
  res : [[int]]
Вывести результат сложения
"""

def read_matrix(h, w):  # [[int]]
    m = [[0] * w] * h
    for row in range(h):
        m[row] = list(map(int, input().split()))
    return m

def add_matrix(a, b):
    #a[0][0] = 3
    #a = [[3]]
    assert len(a) == len(b)
    c = []
    for row_a, row_b in zip(a, b):
        assert len(row_a) == len(row_b)
        c.append([x + y for x, y in zip(row_a, row_b)])
    return c

def print_matrix(a):
    for row in a:
        print(" ".join(map(str, row)))

def main():
    h, w = map(int, input().split())
    a = read_matrix(h, w)
    b = read_matrix(h, w)
    #a = [[1,2],[3,4]]
    #b = [[1,2],[3,4]]
    print_matrix(add_matrix(a, b))


if __name__ == "__main__":
    main()
