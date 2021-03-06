import sys

def read_input(input_file):
    with open(input_file) as f:
        first_line = f.readline()
        fl_data = first_line.split(' ')

        max_slices = int(fl_data[0])
        n_types_pizza = int(fl_data[1])
        second_line = f.readline()
        sl_data = second_line.split(' ')
        n_slices_pizza = [int(i) for i in sl_data] 

        return max_slices, n_types_pizza, n_slices_pizza
def write_output(input_file, n_types_pizza, max_sublist):
    f = open(input_file[:-2]+'out',"w")
    f.write(str(n_types_pizza)+ '\n')
    sublist = ''
    for i in max_sublist:
        sublist += str(i) + ' '
    #print(sublist)
    f.write(sublist)
    f.close()



def order(max_slices, max_types_pizza, n_slices_pizza):
    # as many pizza slices as possible, but not more than the maximum number
    sorted_index = sorted(range(len(n_slices_pizza)), key=lambda k: -n_slices_pizza[k]) 
    max_sum = 0
    max_sublist = []
    max_n_types_pizza = 0
    for i in sorted_index:

        sum = n_slices_pizza[i]
        sublist = [i]
        types_pizza = 1
        elements = sorted_index
        elements.remove(i)

        for j in elements:
            if sum + n_slices_pizza[j] <= max_slices and types_pizza + 1 <= max_types_pizza:
                sum = sum + n_slices_pizza[j]
                types_pizza += 1
                sublist.append(j)

        if sum > max_sum:
            max_sum = sum
            max_n_types_pizza = types_pizza
            max_sublist = sublist

            if max_sum == max_slices:
                return max_sum, max_n_types_pizza, max_sublist
    return max_sum, max_n_types_pizza, max_sublist

    

if __name__ == '__main__':
    input_file = sys.argv[1]
    max_slices, n_types_pizza, n_slices_pizza = read_input(input_file)
    #print('MAX SLICES: ',max_slices,'MAX TYPES PIZZAS: ', n_types_pizza)
    max_sum, max_n_types_pizza, max_sublist = order(max_slices, n_types_pizza, n_slices_pizza)
    #print('MAX SUM SLICES: ', max_sum, 'TYPES OF PIZZA USED: ',max_n_types_pizza)
    max_sublist.sort()
    write_output(input_file, max_n_types_pizza, max_sublist)

