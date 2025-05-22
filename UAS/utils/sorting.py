def merge_sort(data):
    """
    Implementasi Merge Sort untuk sorting leaderboard
    Kompleksitas waktu: O(n log n)
    """
    if len(data) <= 1:
        return data
    
    # Bagi data menjadi dua bagian
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    
    # Gabungkan dengan urutan descending
    return merge(left, right)

def merge(left, right):
    """Menggabungkan dua list yang sudah terurut"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i]['poin'] >= right[j]['poin']:  # Descending order
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Tambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])
    return result