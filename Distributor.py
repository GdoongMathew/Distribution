from typing import Any, Dict, List
from collections import Counter


def all_to_avg(l1: List, d1: Dict[Any, List]) -> Dict:
    """
    given a list and a dictionary, try to remap
    d1's values with items in the list with the
    minimum changes to the dictionary.
    :param l1: a list
    :param d1: a dictionary
    :return: a dictionary
    """
    assert isinstance(l1, (list, tuple)), 'l1 should be a list or tuple.'
    assert isinstance(d1, dict), 'd1 should ba a dictionary.'

    d_ori = d1.copy()
    d_count = sum([len(x) for x in d1.values()])
    it_num = d_count // len(l1)
    remainder = d_count % len(l1)

    que_list = []
    for k, v in d_ori.items():
        if k not in l1:
            que_list.extend(v)
            d1.pop(k)
        elif len(v) > it_num:
            d1[k] = v[:it_num]
            que_list.extend(v[it_num:])
        else:
            d1[k].extend(que_list[:it_num - len(v)])
            que_list = que_list[it_num - len(v):]

    return d1


if __name__ == '__main__':
    l1 = [1, 4, 5, 2, 8]
    import numpy as np
    d_ori = dict((lambda x: (f'com{x}', np.random.randint(10)))(i) for i in range(30))
    d1 = dict()
    for k, v in d_ori.items():
        if v not in d1:
            d1[v] = [k]
        else:
            d1[v].append(k)
    d2 = all_to_avg(l1, d1)
    print(d2)


