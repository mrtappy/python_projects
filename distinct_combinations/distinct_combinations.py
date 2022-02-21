import math

num_param = 4
options_per_param = 3

num_combinations = options_per_param**num_param

print("Possible combinations: ", num_combinations)

bit_per_param = math.ceil(math.log2(options_per_param))

print("bit per parameter: ", bit_per_param)

bit_stream = bit_per_param*num_param

print("bit stream length: ", bit_stream)

bit_stream_max = (2**8)-1

print("max bit stream vale: ", bit_stream_max)

combinations_list = []

for x in range(0, 256):
    combinations_list.append(f'{x:08b}')
    
print(combinations_list)

new_list = []
out_of_range_flag = False

for x in combinations_list:
    for y in range(0, 7, 2):
        if x[y:y+2] == '11':
            out_of_range_flag = True
            break
    if(out_of_range_flag == False):
        new_list.append(x)
    out_of_range_flag = False        

print()            
print(new_list)
print(len(new_list))
