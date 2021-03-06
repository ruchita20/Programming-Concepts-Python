# Given a list, use the last element in the list as the pivot to partition the
# list into those less than or equal to the pivot, the pivot itself and those
# greater. Return the final index of the pivot. Assume that start and end are
# given the range of the list. Assume both are inclusive and the list is not
# empty.
def partition(li, start, end):
  if start == end:
    return start
  pivot = li[end]  # last element
  rightPartStartIndex = start
  for i in range(start, end):
    if (li[i] <= pivot):
      li[i], li[rightPartStartIndex] = li[rightPartStartIndex], li[i]
      rightPartStartIndex += 1
  li[end], li[rightPartStartIndex] = li[rightPartStartIndex], li[end]
  return rightPartStartIndex

def quickSort(li, start, end):
  pivot = partition(li, start, end)
  # If there is more than one element on the right
  # then quick sort the partition.
  if (pivot - start > 1):
    quickSort(li, start, pivot - 1)
  # If there is more than one element on the left
  # then quick sort the partition.
  if (end - pivot > 1):
    quickSort(li, pivot + 1, end)
