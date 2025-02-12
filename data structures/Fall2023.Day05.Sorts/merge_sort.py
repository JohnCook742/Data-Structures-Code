import math

def merge_recurse(in_tuple, start_index, stop_index):
  out_list = list(in_tuple)
  diff = stop_index - start_index
  if diff <= 0:
    return out_list
  
  halfway_index = math.floor((stop_index + start_index)/2)
  first_half = merge_recurse(out_list, start_index, halfway_index)
  second_half = merge_recurse(out_list, halfway_index+1, stop_index)
  
  first_index = start_index
  second_index = halfway_index+1

  for i in range(start_index, stop_index+1):
    if first_index > halfway_index:
      out_list[i] = second_half[second_index]
      second_index += 1
      continue
    if(second_index > stop_index):
      out_list[i] = first_half[first_index]
      first_index += 1
      continue

    if first_half[first_index] < second_half[second_index]:
      out_list[i] = first_half[first_index]
      first_index+=1
    else:
      out_list[i] = second_half[second_index]
      second_index+=1
  return out_list

def merge_sort(in_tuple):
  
  result = merge_recurse(in_tuple, 0, len(in_tuple)-1)

  return result