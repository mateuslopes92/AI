def merge_two_sorted_lists(a, b):
  sorted_list = []
  len_a = len(a)
  len_b = len(b)
  i = j = 0

  while i < len_a and j < len_b:
    if a[i] <= b[j]:
      sorted_list.append(a[i])
      i += 1
    else:
      sorted_list.append(b[j])
      j += 1

  while i < len_a:
    sorted_list.append(a[i])
    i += 1

  while j < len_b:
    sorted_list.append(b[j])
    j += 1

  return sorted_list

def merge_sort(elements):
  if len(elements) <= 1:
    return elements

  mid = len(elements) // 2
  left = elements[:mid]
  right = elements[mid:]

  left = merge_sort(left)
  right = merge_sort(right)

  return merge_two_sorted_lists(left, right)


if __name__ == '__main__':
  a = [5, 8, 12, 56]
  b = [7, 9, 45, 51]
  unsorted_list = [10, 3, 15, 7, 8, 23, 98, 29]

  print("merge_two_sorted_lists: ", merge_two_sorted_lists(a, b))
  print("merge_sort: ", merge_sort(unsorted_list))