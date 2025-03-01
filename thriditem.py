from logic.address import Address

def get_binary_address(n):
    aux = convert_to_binary(n)
    return (address_size - len(aux)) * '0' + aux

def convert_to_binary(decimal_number):
    binary_number = bin(decimal_number)[2:]
    return binary_number

address_size = 64

address_list = [3,180,43,2,191,88,190,14,181,44,186,253]


def indexes(n, index_size): #3, 2, 1
    aux = convert_to_binary(n)
    return (index_size - len(aux)) * '0' + aux

C1_cache_list = [[indexes(i,3), Address(0,0,0,0,0)] for i in range(8)]
C1_hit_list = []

C2_cache_list = [[indexes(i,2), Address(0,0,0,0,0)] for i in range(4)]
C2_hit_list = []

C3_cache_list = [[indexes(i,1), Address(0,0,0,0,0)] for i in range(2)]
C3_hit_list = []

def get_index(binary_number, index_size, offset_size):
    return binary_number[address_size - index_size - offset_size:address_size - offset_size]

def get_tag(binary_number, index_size, offset_size):
    return binary_number[:address_size - index_size - offset_size]

def get_offset(binary_number, offset_size):
    return binary_number[address_size - offset_size - 1]

def make_addressess(address_list, C1 = [], C2 = [], C3 = []):
    for address in address_list:
        binary = get_binary_address(address)

        C1_index = get_index(binary, 3,0)
        C2_index = get_index(binary, 2, 1)
        C3_index = get_index(binary, 1, 2)

        C1_tag = get_tag(binary, 3,0)
        C2_tag = get_tag(binary, 2, 1)
        C3_tag = get_tag(binary, 1, 2)

        C1_offset = get_offset(binary,0)
        C2_offset = get_offset(binary,1)
        C3_offset = get_offset(binary,2)

        C1_hit_list = address_routing(8, C1_cache_list, address, binary, C1_index, C1_tag, C1_offset, C1)
        C2_hit_list = address_routing(4, C2_cache_list, address, binary, C2_index, C2_tag, C2_offset, C2)
        C3_hit_list = address_routing(2, C3_cache_list, address, binary, C3_index, C3_tag, C3_offset, C3)

    return C1_hit_list, C2_hit_list, C3_hit_list


def address_routing(cache_size, cache_list, address, binary, index, tag, offset, hit_list = []):
        for i in range(cache_size):
            if cache_list[i][0] == index:
                if cache_list[i][1].tag == tag and cache_list[i][1].index == index:
                    hit_list.append([address, 'Hit'])
                else:
                    cache_list[i][1].decimal = address
                    cache_list[i][1].binary = binary
                    cache_list[i][1].tag = tag
                    cache_list[i][1].index = index
                    cache_list[i][1].offset = offset
                    hit_list.append([address, 'Miss'])
                    break
        return hit_list

def get_hits_and_misses(hit_list = []):
    hits = 0
    misses = 0
    for i in range(len(hit_list)):
        if hit_list[i][1] == 'Hit':
            hits += 1
        else:
            misses += 1
    print('Hits: ', hits)
    print('Misses: ', misses)
    return hits, misses

def get_missrate(hits, misses):
    print('Miss Rate: ', misses * 100 / (hits + misses),'%')
    return misses * 100 / (hits + misses)


C1_hit_list, C2_hit_list, C3_hit_list = make_addressess(address_list, C1_hit_list, C2_hit_list, C3_hit_list)

#for i in range(len(C1_cache_list)):
    #print(C1_cache_list[i][0] ,C1_cache_list[i][1].__tuple__())

#print('\n\n')

for i in range(len(C1_hit_list)):
    print('[',C1_hit_list[i][0], C1_hit_list[i][1],']')

C1_hits, C1_misses = get_hits_and_misses(C1_hit_list)
C1_missrate = get_missrate(C1_hits, C1_misses)


#for i in range(len(C2_cache_list)):
    #print(C2_cache_list[i][0] ,C2_cache_list[i][1].__tuple__())

print('\n\n')

for i in range(len(C2_hit_list)):
    print('[',C2_hit_list[i][0], C2_hit_list[i][1],']')

C2_hits, C2_misses = get_hits_and_misses(C2_hit_list)
C2_missrate = get_missrate(C2_hits, C2_misses)

#for i in range(len(C3_cache_list)):
    #print(C3_cache_list[i][0] ,C3_cache_list[i][1].__tuple__())

print('\n\n')

for i in range(len(C3_hit_list)):
    print('[',C3_hit_list[i][0], C3_hit_list[i][1],']')

C3_hits, C3_misses = get_hits_and_misses(C3_hit_list)
C3_missrate = get_missrate(C3_hits, C3_misses)

rates = [C1_missrate, C2_missrate, C3_missrate]
min_rate = min(C1_missrate, C2_missrate, C3_missrate)

if min_rate == C1_missrate:
    print('La cache 1 es la mejor opción para la secuencia de datos dado que tiene el porcentaje de miss rate más bajo')
elif min_rate == C2_missrate:
    print('La cache 2 es la mejor opción para la secuencia de datos dado que tiene el porcentaje de miss rate más bajo')
else:
    print('La cache 3 es la mejor opción para la secuencia de datos dado que tiene el porcentaje de miss rate más bajo')