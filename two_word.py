#item 5.2.2.
from logic.address import Address
def convert_to_binary(decimal_number):
    binary_number = bin(decimal_number)[2:]
    return binary_number

address_size = 64

address_list = [3,180,43,2,191,88,190,14,181,44,186,253]

def two_word_get_cache_indexes(n):
    aux = convert_to_binary(n)
    return (3 - len(aux)) * '0' + aux

two_word_cache_list = [[two_word_get_cache_indexes(i), Address(0,0,0,0,0)] for i in range(8)]
two_word_hit_list = []
def two_word_get_binary_address(n):
    aux = convert_to_binary(n)
    return (address_size - len(aux)) * '0' + aux

def two_word_get_index(binary_number):
    return binary_number[address_size - 4:address_size - 1]

def two_word_get_tag(binary_number):
    return binary_number[:address_size - 4]

def two_word_get_offset(binary_number):
    return binary_number[address_size - 1]

def two_word_make_addressess(address_list, hits=0, misses=0):
    for address in address_list:
        binary = two_word_get_binary_address(address)
        index = two_word_get_index(binary)
        tag = two_word_get_tag(binary)
        offset = two_word_get_offset(binary)


        for i in range(len(two_word_cache_list)):
            if two_word_cache_list[i][0] == index:
                if two_word_cache_list[i][1].tag == tag and two_word_cache_list[i][1].index == index:
                    hits+=1
                    two_word_hit_list.append([address, 'Hit'])
                else:
                    two_word_cache_list[i][1].decimal = address
                    two_word_cache_list[i][1].binary = binary
                    two_word_cache_list[i][1].tag = tag
                    two_word_cache_list[i][1].index = index
                    two_word_cache_list[i][1].offset = offset
                    two_word_hit_list.append([address, 'Miss'])
                    misses += 1
                    break
    return hits, misses

hits, misses = two_word_make_addressess(address_list)

for i in range(len(two_word_cache_list)):
    print(two_word_cache_list[i][0] ,two_word_cache_list[i][1].__tuple__())

print('\n\n')

for i in range(len(two_word_hit_list)):
    print('[',two_word_hit_list[i][0], two_word_hit_list[i][1],']')

print("\n\nHits: ", hits)
print("Misses: ", misses)