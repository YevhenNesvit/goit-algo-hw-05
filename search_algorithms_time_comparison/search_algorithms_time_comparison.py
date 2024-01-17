from timeit import timeit

from bm import boyer_moore_search
from rk import rabin_karp_search
from kmp import kmp_search

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
real_pattern1 = "розглянемо проблему виплати"
fake_pattern1 = "перемога буде за нами"

real_pattern2 = "представлення булевих функцій"
fake_pattern2 = "перемога буде за нами"

time_real_bm1 = timeit(lambda: boyer_moore_search(read_file('search_algorithms_time_comparison/article1.txt'), real_pattern1), number=11)
time_real_rk1 = timeit(lambda: rabin_karp_search(read_file('search_algorithms_time_comparison/article1.txt'), real_pattern1), number=11)
time_real_kmp1 = timeit(lambda: kmp_search(read_file('search_algorithms_time_comparison/article1.txt'), real_pattern1), number=11)

time_fake_bm1 = timeit(lambda: boyer_moore_search(read_file('search_algorithms_time_comparison/article1.txt'), fake_pattern1), number=11)
time_fake_rk1 = timeit(lambda: rabin_karp_search(read_file('search_algorithms_time_comparison/article1.txt'), fake_pattern1), number=11)
time_fake_kmp1 = timeit(lambda: kmp_search(read_file('search_algorithms_time_comparison/article1.txt'), fake_pattern1), number=11)

time_real_bm2 = timeit(lambda: boyer_moore_search(read_file('search_algorithms_time_comparison/article2.txt'), real_pattern2), number=11)
time_real_rk2 = timeit(lambda: rabin_karp_search(read_file('search_algorithms_time_comparison/article2.txt'), real_pattern2), number=11)
time_real_kmp2 = timeit(lambda: kmp_search(read_file('search_algorithms_time_comparison/article2.txt'), real_pattern2), number=11)

time_fake_bm2 = timeit(lambda: boyer_moore_search(read_file('search_algorithms_time_comparison/article2.txt'), fake_pattern2), number=11)
time_fake_rk2 = timeit(lambda: rabin_karp_search(read_file('search_algorithms_time_comparison/article2.txt'), fake_pattern2), number=11)
time_fake_kmp2 = timeit(lambda: kmp_search(read_file('search_algorithms_time_comparison/article2.txt'), fake_pattern2), number=11)

print(f"{'| Algorithm': <20} | {'Time real pattern 1': <17} | {'Time fake pattern 1': <17} | {'Time real pattern 2': <17} | {'Time fake pattern 2': <17} |")
print(f"|{'-'*20}|{'-'*21}|{'-'*21}|{'-'*21}|{'-'*21}|")
print(f"{'| Boyer-Moore': <20} | {time_real_bm1:<19.5f} | {time_fake_bm1:<20.5f}| {time_real_bm2:<19.5f} | {time_fake_bm2:<20.5f}|")
print(f"{'| Rabin-Karp': <20} | {time_real_rk1:<19.5f} | {time_fake_rk1:<20.5f}| {time_real_rk2:<19.5f} | {time_fake_rk2:<20.5f}|")
print(f"{'| Knuth–Morris–Pratt': <20} | {time_real_kmp1:<19.5f} | {time_fake_kmp1:<20.5f}| {time_real_kmp2:<19.5f} | {time_fake_kmp2:<20.5f}|")
print(f"|{'-'*20}|{'-'*21}|{'-'*21}|{'-'*21}|{'-'*21}|")