def bubble_sort(in_tuple):
  out_list = list(in_tuple)
  for i in range(len(out_list)):
    for j in range(len(out_list)-1-i):
      if out_list[j+1] < out_list[j]:
        temp = out_list[j]
        out_list[j] = out_list[j+1]
        out_list[j+1] = temp
  return out_list