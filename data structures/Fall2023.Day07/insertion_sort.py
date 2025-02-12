def insertion_sort(in_tuple):
  out_list = list(in_tuple)
  for i in range(1, len(out_list)):
    for j in range(i, 0, -1):
      before = out_list[j-1]
      current = out_list[j]
      if current < before:
        temp = out_list[j]
        out_list[j] = out_list[j-1]
        out_list[j-1] = temp
  return out_list