def parsing(file_name) :
    path_in = "../../data/in/"

    with open(path_in + file_name) as f:
        for i, line in enumerate(f):
            element = line.replace("\n", "").strip()
            dict_line = dict()
            print(element)
            if i == 0:
                num_line = int(element)
                tab_global = []
            else:
                tab_line = element.split(" ")
                h_or_v = tab_line[0]
                num_tag = tab_line[1]
                list_tag = tab_line[2:]
                # dict_line={}
                dict_line["id"] = i - 1
                dict_line["h_or_v"] = h_or_v
                dict_line["num_tag"] = num_tag
                dict_line["list_tag"] = sorted(list_tag)
                tab_global.append(dict_line)

    data = (num_line, tab_global)
    return data

def found_max_tag(data) :
    return max([x['num_tag'] for x in data[1]])