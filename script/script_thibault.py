def parsing(file_name) :
    path_in = "../../data/in/"

    with open(path_in + "a_example.txt") as f:
        for i, line in enumerate(f):
            element = line.replace("\n", "").strip()

            if i == 0:
                num_line = int(element)
                dict_line = {}
            else:
                tab_line = element.split(" ")
                h_or_v = tab_line[0]
                num_tag = tab_line[1]
                list_tag = tab_line[2:]
                dict_line[i - 1] = {}
                dict_line[i - 1]["h_or_v"] = h_or_v
                dict_line[i - 1]["num_tag"] = num_tag
                dict_line[i - 1]["list_tag"] = sorted(list_tag)

    data = (num_line, dict_line)
    return data

def found_max_tag(data) :
    return max([x['num_tag'] for x in data[1]])