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
                dict_line[i - 1]["id"] = [i - 1]
                dict_line[i - 1]["h_or_v"] = h_or_v
                dict_line[i - 1]["num_tag"] = num_tag
                dict_line[i - 1]["list_tag"] = sorted(list_tag)

    data = (num_line, dict_line)
    return data

def found_max_tag(data) :
    return max([x['num_tag'] for x in data[1]])

def inter_not_in(l1,l2):
    return list(set(l1)-set(l2))

def size_not_in(l1,l2):
    return len(inter_not_in(l1,l2))

def inter(l1,l2):
    return sorted(list(set(l1) & set(l2)))

def tailleInter(l1,l2):
    return len(inter(l1,l2))

def score_two_list(l1,l2) :
    num_intersec=tailleInter(l1,l2)
    num_uni_1=size_not_in(l1,l2)
    num_uni_2=size_not_in(l2,l1)
    return min(num_intersec,num_uni_1,num_uni_2)