# function to get unique values 
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
  #  for x in unique_list: 
     #   print(x)
    return unique_list


# Assigns how many times an entry appears
# in the list argument input_list to a 
# dictionary. The dictionary's keys are 
# the unique elements of input_list
def counts(input_list):

    # The dictionary the counts returns
    output_dict = {}
    # Unique elements of input_list
    unique_list = unique(input_list)

    # Traverse each element of unique_list:
    for i in unique_list:
        # the count is initially 0 for each key of output_dict
        output_dict[i] = 0
        # Traverse each element of the original input_list
        for j in input_list:
            if(i==j):
                # increase the count for each key of output_dict
                # if the element of the unique list
                # equals the element of the original list
                output_dict[i] += 1
        
    # Return the dictionary
    return output_dict


print(counts(['A','A','B','C','A']))
#print(counts(['A','A','B','C','A', 'K', 'S', 'A', 1, 50, 'AttaBoy']))










