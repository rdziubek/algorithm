"""
NOTE:
    Lists instead of strings are used (where not specified otherwise).

"""

import anagram
import bisection_root_finding
import bisection_search
import bubble_sort
import bucket_sort
import caesar_cipher
import change_making
import dec_to_base_iterative
import dec_to_base_recursive
import exponentiation_by_squaring
import fibonacci_iterative
import fibonacci_recursive
import gcd_iterative
import gcd_recursive
import insertion_sort
import lcm_iterative
import lcm_recursive
import lexicographic_order
import merge_sort
import palindrome
import pattern_search
import perfect_number
import prime_factorisation
import prime_number
import quick_sort
import selection_sort
import sieve_of_eratosthenes
import transposition_cipher


""" SORTING """

bubble_sort.sort(
    array=[3, 2, 11, -1, 0]
)

array = [0.48, 0.27, 0.12, 0.21, 0.43, 0.25]
bucket_sort.sort(
    array,
    max_value=max(array)
)

insertion_sort.sort(
    array=[3, 2, 11, -1, 0]
)

merge_sort.sort(
    array=[3, 2, 11, -1, 0]
)

array = [3, 2, 11, -1, 0]
quick_sort.sort(
    array,
    left=0,
    right=len(array) - 1
)

selection_sort.sort(
    array=[3, 2, 11, -1, 0]
)

lexicographic_order.order(
    words=['aab', 'aaa', 'aa', 'aaa']
)


""" SEARCHING """

pattern_search.search(
    text=list('karykatura'),
    pattern=list('ka')
)

bisection_root_finding.bisect(
    a=-4,
    b=4,
    error=0.001
)

bisection_search.search(
    array=[-1, 0, 2, 3, 11],
    target=3
)


""" STRING OPS """

anagram.anagram(
    word1=list('arbuz'),
    word2=list('burza')
)

palindrome.palindrome(
    word=list('kajak')
)

caesar_cipher.cipher(
    key=2,
    text=list('xyz')
)

transposition_cipher.cipher(
    text=list('SLOWO')
)


""" NUMERAL SYSTEMS """

dec_to_base_iterative.change_base(
    number=10,
    base=2
)

array = []
dec_to_base_recursive.change_base(
    number=10,
    base=2,
    callback=array
)


""" NUMERIC OPTIMISATION """

gcd_iterative.gcd(
    a=5,
    b=10
)

gcd_recursive.gcd(
    a=5,
    b=10
)

lcm_iterative.lcm(
    a=5,
    b=10
)

lcm_recursive.lcm(
    a=5,
    b=10
)

prime_factorisation.factorise(
    number=100
)

change_making.change(
    amount=6
)

exponentiation_by_squaring.exponentiate(
    base=2,
    power=10
)


""" SEQUENCES """

fibonacci_iterative.fibonacci(
    count=5
)

fibonacci_recursive.fibonacci(
    count=5
)

sieve_of_eratosthenes.sieve(
    limit=13
)


""" NUMBER THEORY """

prime_number.is_prime(
    number=13
)

perfect_number.is_perfect(
    number=6
)
