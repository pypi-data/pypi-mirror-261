import copy
import traceback
import random


class Field:

    def __init__(self, name: str, value: object=None):
        self.name = name
        self.children = list()
        self.value = value

    def to_dict(self):
        if self.value is None:
            return {self.name: None}
        elif self.value.__class__.__name__ == 'Field':
            return {self.name: self.value.to_dict()}
        return {self.name: self.value}


def create_field(dotted_name: str, value: object)->Field:
    field_names = dotted_name.split('.')
    if len(field_names) > 1:
        next_dotted_name = '.'.join(field_names[1:])
        field = Field(name=field_names[0], value=create_field(dotted_name=next_dotted_name, value=value))
    else:
        field = Field(name=field_names[0], value=copy.deepcopy(value))
    return field


def merge_dicts(A: dict, B: dict)->dict:
    # FROM https://stackoverflow.com/questions/29241228/how-can-i-merge-two-nested-dictionaries-together (Vivek Sable)
    for i, j in B.items(): 
        if i in A:
            A[i].update(j)
        else:
            A[i] = j
    return A


def generate_random_string(
    length: int=16,
    chars: str='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
)->str:
    if chars is None:
        raise Exception('chars parameter cannot be None')
    if isinstance(chars, str) is False:
        raise Exception('chars must be a string object')
    if len(chars) == 0:
        raise Exception('chars parameter must contain at least some characters')
    result = ''
    chars_list = list(chars)
    random.shuffle(chars_list)
    while len(result) < length:
        result = '{}{}'.format(
            result,
            random.choice(chars_list)
        )
    return result

