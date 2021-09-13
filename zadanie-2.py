def csv_reader(print_header=False, separator=',', quote_character='"'):
    csv_data_list = []
    with open('csv_file_for_reading.csv', 'r') as csv_file:
        for line in csv_file:
            if quote_character in line:
                start_idx = line.find(quote_character)
                end_idx = line.find(quote_character, start_idx + 1)
                if start_idx > 0 and end_idx == len(line) - 1:
                    # start inny niż 0, end równy len
                    csv_data_list.append([line[:start_idx], line[start_idx:]])
                elif start_idx > 0 and end_idx != len(line) - 1:
                    # start inny niż 0 i end inny niż len
                    csv_data_list.append([line[:start_idx], line[start_idx: end_idx + 1], line[end_idx + 1:]])
                elif start_idx == 0 and end_idx != len(line) - 1:
                    # start równy 0, a end inny niz len
                    csv_data_list.append([line[:end_idx + 1], line[end_idx + 1:]])
                elif start_idx == 0 and end_idx == len(line) - 1:
                    # start równy 0, a end równy len
                    csv_data_list.append([line])
            else:
                csv_data_list.append(line.split(separator))
    if print_header:
        header = csv_data_list[0]
        return csv_data_list[1:], header
    else:
        return csv_data_list


if __name__ == '__main__':
    print(csv_reader())
