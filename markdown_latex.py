from copy import deepcopy

TEMPLATE_LEFT = ['$`\\displaystyle ']
TEMPLATE_RIGHT = [' `$']

def array_creator(m, n, left_delimiter=None, right_delimiter=None, align_center=True):
    result_list = deepcopy(TEMPLATE_LEFT)
    result_list.append('\\left')
    result_list.append(left_delimiter) if left_delimiter else result_list.append('\\lbrace')
    result_list.append('\\begin{array}')
    result_list.append('{')
    aligner_list = ['c' for _ in range(n)] if align_center else ['l' for _ in range(n)]
    result_list.extend(aligner_list)
    result_list.append('} ')

    for i in range(m):
        for j in range(n):
            result_list.append(str(i))
            result_list.append(chr(j+65))            
            result_list.append('&')
        result_list.pop()
        result_list.append('\\\\')
    result_list.pop()

    result_list.append(' \\end{array}')
    result_list.append('\\right')
    result_list.append(right_delimiter) if right_delimiter else result_list.append('\\rbrace')
    result_list.extend(TEMPLATE_RIGHT)
    return ''.join(result_list)


def summation_creator(bottom_text=None, top_text=None, right_text=None):
    result_list = deepcopy(TEMPLATE_LEFT)
    result_list.append('\\sum_{')

    if bottom_text:
        result_list.append('\\textrm{')
        result_list.append(bottom_text)
        result_list.append('}')
    else:
        result_list.append('i=1')
    result_list.append('}^{')

    if top_text:
        result_list.append('\\textrm{')
        result_list.append(top_text)
        result_list.append('}')
    else:
        result_list.append('n')
    result_list.append('}{')

    if right_text:
        result_list.append('\\textrm{')
        result_list.append(right_text)
        result_list.append('}')
    else:
        result_list.append('a_i')
    result_list.append('}')

    result_list.extend(TEMPLATE_RIGHT)
    return ''.join(result_list)


if __name__ == '__main__':
    print('[Array Examples]')
    print(array_creator(3, 4))
    print(array_creator(m=2,n=2,left_delimiter='.',right_delimiter='.',align_center=True))
    
    print('\n[Summation Examples]')
    print(summation_creator())
    print(summation_creator(bottom_text='abc', top_text='n', right_text='xxx'))
    


    print(array_creator(m=2,n=2,left_delimiter=None,right_delimiter='.',align_center=True))
    