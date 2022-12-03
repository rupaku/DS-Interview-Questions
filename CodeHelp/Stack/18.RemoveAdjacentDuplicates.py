''''''
from unittest import skip


def remove_adjacent_dup(str):
    skip_ptr=-1
    i=0
    while i < len(str):
        if skip_ptr == -1 or str[skip_ptr] != str[i]:
            skip_ptr=skip_ptr+1
            str[skip_ptr] = str[i]
            i=i+1
        else:
            while i < len(str) and str[skip_ptr] == str[i]:
                i=i+1
            skip_ptr = skip_ptr -1
        skip_ptr=skip_ptr+1
        str=str[0:skip_ptr]
        print(str)
remove_adjacent_dup(['6','2','4','1','2','1','2','2','1'])