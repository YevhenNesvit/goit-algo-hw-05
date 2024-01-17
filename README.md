# Порівняння алгоритмів пошуку
У цьому репозиторії проводиться порівняльний аналіз трьох алгоритмів пошуку: Boyer-Moore, Rabin-Karp та Knuth–Morris–Pratt. Дослідження включає оцінку продуктивності алгоритмів на двох текстах: з шаблоном, який присутній в текстах та з таким, якого немає.

## Результати
Наведена таблиця демонструє час виконання (у секундах) для кожного алгоритму з різними текстами і різними шаблонами:

| Algorithm          | Time real pattern 1 | Time fake pattern 1 | Time real pattern 2 | Time fake pattern 2 |
|--------------------|---------------------|---------------------|---------------------|---------------------|
| Boyer-Moore        | 0.00994             | 0.01155             | 0.00580             | 0.01436             |
| Rabin-Karp         | 0.05852             | 0.07402             | 0.04864             | 0.10119             |
| Knuth–Morris–Pratt | 0.02436             | 0.02871             | 0.02200             | 0.04452             |

## Висновки
- **Boyer-Moore** виявився найефективнішим серед тестованих алгоритмів, демонструючи швидкість пошуку, яка перевершує інші алгоритми.
- **Rabin-Karp** є менш ефективним порівняно з Boyer-Moore, але може бути прийнятним в певних випадках.
- **Knuth–Morris–Pratt** є гарним варіантом, але трошки менш ефективним порівняно з Boyer-Moore, зокрема при пошуку фальшивих патернів.

Ці результати варто враховувати при виборі алгоритму для конкретного використання в залежності від вимог до швидкості та характеру вхідних даних.

## Використання

Клонуйте репозиторій:

```bash
git clone https://github.com/YevhenNesvit/goit-algo-hw-05
```

Запустіть:
```bash
python3 search_algorithms_time_comparison
```
