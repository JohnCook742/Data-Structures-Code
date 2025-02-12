def selection_sort(in_tuple):
  out_list = list(in_tuple)
  for i in range(len(out_list)):
    lowestIndex = -1
    lowestValue = 1000000
    for j in range(i, len(out_list)):
      if out_list[j] < lowestValue:
        lowestIndex = j
        lowestValue = out_list[j]
    temp = out_list[i]
    out_list[i] = out_list[lowestIndex]
    out_list[lowestIndex] = temp
  return out_list