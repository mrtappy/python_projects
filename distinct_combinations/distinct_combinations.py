# Python script to determine all possible parameter combinations for arbitrary configurations
# Use case: The script will produce a combination matrix which can then be used to autonomously test all possible (and relevant) configurations in order to find the optimal configuration for an arbitrary device (e.g. a sensor)

import math
import yaml

class Config_Parameters():
    attribute_list = []
    def __setattr__(self, name, value):
        self.__dict__[name] = value
        self.attribute_list.append(value)
        print("Hello!")
    # def __init__(self):
    #     self.attribute_list = [getattr(self, attr) for attr in dir(self) if not (attr.startswith("__") or attr.startswith("get"))]
    
    # threshold = [0, 127, 255]
    # blind_time = [0, 7, 15]
    # pulse_counter = [0, 1, 3]
    # window_time = [0, 1, 3]
        
config_parameters = Config_Parameters()
# print("Parameter list: ", config_parameters.attribute_list)

with open('parameters.yaml') as f:
    my_dict = yaml.safe_load(f)

print("my dict: ", my_dict)

for key in my_dict:
    print("key: ", key)
    print("list: ", my_dict[key])
    setattr(config_parameters, key, my_dict[key])

print(vars(config_parameters))
print(config_parameters.attribute_list)

# bit_per_param_list = []
# combination_count = 1
# for x in config_parameters.attribute_list:
#     combination_count *= len(x)
#     bit_per_param_list.append(math.ceil(math.log2(len(x))))

# print("Possible combinations: ", combination_count)
# print("bits per parameter: ", bit_per_param_list)

# bit_stream_length = sum(bit_per_param_list)
# print("bit stream length: ", bit_stream_length)

# bit_stream_max = (2**bit_stream_length)-1
# print("max bit stream value: ", bit_stream_max)

# bit_combinations_list = []
# for x in range(0, bit_stream_max+1):
#     bit_combinations_list.append(f'{x:08b}')
    
# relevant_combinations_list = []
# out_of_range_flag = False
# parameter_list_index = 0       
# for x in bit_combinations_list:
#     for y in range(0, bit_stream_length-1, 2):
#         if int(x[y:y+2],2) >= len(config_parameters.attribute_list[parameter_list_index]):
#             out_of_range_flag = True
#             break
#         parameter_list_index += 1
#     parameter_list_index = 0
#     if(out_of_range_flag == False):
#         relevant_combinations_list.append(x)
#     out_of_range_flag = False        

# print()            
# for x in relevant_combinations_list:
#     print(x)
# print(len(relevant_combinations_list))

# configuration_matrix = []
# iterations = 0
# for x in range(0, len(relevant_combinations_list)):
#     configuration_matrix.append([])
#     iterations += 1
#     for y in range(0, bit_stream_length-1, 2):
#         # print("attribute index: ", int(y/2))
#         # print("binary value: ", int(relevant_combinations_list[x][y:y+2], 2))
#         configuration_matrix[x].append(config_parameters.attribute_list[int(y/2)][int(relevant_combinations_list[x][y:y+2], 2)])

# for x in configuration_matrix:
#     print(x)
# print("iterations: ", iterations)
