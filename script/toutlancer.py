def parsing(file_name) :
    path_in = "../data/in/"

    with open(path_in + file_name) as f:
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

#data=parsing("a_example.txt")

#data=parsing("b_lovely_landscapes.txt")
data=parsing("c_memorable_moments.txt")
#data=parsing("d_pet_pictures.txt")
#data=parsing("e_shiny_selfies.txt")

def listVert(data):
    ret=[]
    for x in data[1]:
        if data[1][x]["h_or_v"]=="V":
           ret.append(data[1][x]["id"][0])
    return ret


"""renvoie liste doublets (id,numtag)"""
def taillesV(data):
    list=listVert(data)
    tailles=[]
    for x in list:
        tailles.append((x,(int(data[1][x]["num_tag"]))))
    return tailles

def sortedV(data):
    li=taillesV(data)
    return sorted(li, key=lambda student: student[1])

def doublets(data):
    ret=[]
    li=sortedV(data)
    while len(li)>1:
        ret.append((li[0],li[-1]))
        li=li[1:-2]
    return ret

print(doublets(data))
