
def cmp_nr(elem):
    return elem[0]

def cmp_cifra(elem):
    return elem[1]

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

my_list = [(38, 'b'), (27, 'a'), (38, 'g'), (3, 'd'), (9, 'e'), (38, 'c'), (10, 'f')]
merge_sort(my_list, keys=[cmp_nr, cmp_cifra], key_orders=[True, False])
print("Lista sortată:", my_list)
