"""
Return the sorted version of the list using a quicksort
You must use the first value in a given list as the pivot.
For example, if list was [2,3,1], then the pivot would be the value 2
"""


def sort(list):
    lowList = []
    highList = []
    newList = []
    if len(list) > 1:
        # initialization of pivot to first item in the list
        piv = list[0]
        for i in range(len(list)):
            if (piv > list[i]):
                lowList.append(list[i])
            elif (piv < list[i]):
                highList.append(list[i])
            else:
                newList.append(list[i])

        # recursive sorting of new lists
        lowList = sort(lowList)
        highList = sort(highList)
    else:
        return list

    # concatenating lists based on stackoverflow post
    newList = lowList + newList + highList

    return newList
