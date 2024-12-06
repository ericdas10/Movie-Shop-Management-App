import random
import string

def string_generator(size):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))

def number_string_generator(size):
    return ''.join(random.choice(string.digits) for _ in range(size))

def merge_sort(arr, keys=None, key_orders=None):
    if keys is None:
        keys = [None]

    if key_orders is None:
        key_orders = [True] * len(keys)

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, keys=keys, key_orders=key_orders)
        merge_sort(right_half, keys=keys, key_orders=key_orders)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            left_keys = [left_half[i] if key is None else key(left_half[i]) for key in keys]
            right_keys = [right_half[j] if key is None else key(right_half[j]) for key in keys]

            compare_result = 0
            for left_key, right_key, order in zip(left_keys, right_keys, key_orders):
                if left_key < right_key:
                    compare_result = -1 if order else 1
                    break
                elif left_key > right_key:
                    compare_result = 1 if order else -1
                    break

            if compare_result <= 0:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    """
    Merge sort, complexitate:
    1. Caz favorabil:T(n) apartine O(n*log2(n))
    2.Caz defavorabil: T(n) apartine O(n*log2(n))
    3. Caz mediu: T(n) apartine O(n*log2(n))
    """


def bingo_sort(arr, key=None, reverse=False):
    n = len(arr)
    sorted_elements = []

    while len(sorted_elements) < n:
        # Alege aleator un element din lista
        element = random.choice(arr)

        # Aplică funcția key dacă este specificată
        element_key = element if key is None else key(element)

        # Adaugă elementul în lista sortată dacă nu a fost deja adăugat
        if element_key not in (key(e) if key is not None else e for e in sorted_elements):
            sorted_elements.append(element)

    # Sortează lista sortată finală folosind key și reverse
    sorted_elements.sort(key=key, reverse=reverse)

    # Copiază elementele sortate înapoi în lista inițială
    for i in range(n):
        arr[i] = sorted_elements[i]

