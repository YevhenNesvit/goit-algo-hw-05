from timeit import timeit

from bm import boyer_moore_search
from rk import rabin_karp_search
from kmp import kmp_search

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
real_pattern = "представлення булевих функцій"
fake_pattern = "перемога"

time_real_bm = timeit(lambda: boyer_moore_search(read_file('search_algorithms_time_comparison/article2.txt'), real_pattern), number=11)
time_real_rk = timeit(lambda: rabin_karp_search(read_file('search_algorithms_time_comparison/article2.txt'), real_pattern), number=11)
time_real_kmp = timeit(lambda: kmp_search(read_file('search_algorithms_time_comparison/article2.txt'), real_pattern), number=11)

time_fake_bm = timeit(lambda: boyer_moore_search(read_file('search_algorithms_time_comparison/article2.txt'), fake_pattern), number=11)
time_fake_rk = timeit(lambda: rabin_karp_search(read_file('search_algorithms_time_comparison/article2.txt'), fake_pattern), number=11)
time_fake_kmp = timeit(lambda: kmp_search(read_file('search_algorithms_time_comparison/article2.txt'), fake_pattern), number=11)

print(f"{'| Algorithm': <20} | {'Time real pattern': <17} | {'Time fake pattern': <17} |")
print(f"|{'-'*20}|{'-'*19}|{'-'*19}|")
print(f"{'| Boyer-Moore': <20} | {time_real_bm:<17.5f} | {time_fake_bm:<18.5f}|")
print(f"{'| Rabin-Karp': <20} | {time_real_rk:<17.5f} | {time_fake_rk:<18.5f}|")
print(f"{'| Knuth–Morris–Pratt': <18} | {time_real_kmp:<17.5f} | {time_fake_kmp:<18.5f}|")