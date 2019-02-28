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

def greedy_method(data,tolerance):
    num_photo = data[0]
    dict_photo = data[1].copy()
    result = []
    slide_before = ""
    score_total = 0
    i = 0
    while len(dict_photo) > 0 and i<num_photo+1:
        i = i + 1
        if i%100==0:
            print(i)
        min_score = 0
        if slide_before == "":
            slide_before = dict_photo[0]
            result.append(slide_before)
            del dict_photo[0]
        else:
            slide_before = slide_after.copy()
            result.append(slide_after)
        max_theorique = int(float(slide_before["num_tag"]) / 3.0)

        for elt in dict_photo:
            slide_tmp = dict_photo[elt].copy()
            tmp_score = score_two_list(slide_before["list_tag"], slide_tmp["list_tag"])
            if tmp_score >= min_score:
                slide_after = slide_tmp.copy()
                min_score = tmp_score
                id_supr = elt
            if min_score == max_theorique/tolerance:
                slide_after = slide_tmp.copy()
                min_score = tmp_score
                id_supr = elt
                break
        score_total = score_total + min_score
        del dict_photo[id_supr]

    result.append(slide_after)
    print(score_total)
    return result

def out_result(result):
    print(len(result))
    for elt in result :
        print(" ".join([str(x) for x in elt["id"]]))


def listVert(data):
    ret=[]
    for x in data[1]:
        if data[1][x]["h_or_v"]=="V":
           ret.append(data[1][x]["id"][0])
    return ret





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
        ret.append((li[0][0],li[-1][0]))
        li=li[1:-1]
    return ret



def out_result_file(result,file_out):
    with open(file_out,"w") as f :
        f.write(str(len(result))+"\n")
        for elt in result :
            f.write(" ".join([str(x) for x in elt["id"]])+"\n")


def concat_v(data,list_v) :
    data_finale = {}
    print(len([data[1][x] for x in data[1] if data[1][x]["h_or_v"] == "V"]))
    print(len(list_v))
    for i, (id1, id2) in enumerate(list_v):
        list_common = sorted(list(set(data[1][id1]["list_tag"]).union(set(data[1][id2]["list_tag"]))))
        data_finale[id1] = {}
        data_finale[id1]["id"] = [id1, id2]
        data_finale[id1]["h_or_v"] = "H"
        data_finale[id1]["num_tag"] = len(list_common)
        data_finale[id1]["list_tag"] = list_common

    list_h = [data[1][x] for x in data[1] if data[1][x]["h_or_v"] == "H"]
    print(len(list_h))
    for elt in list_h:
        id2 = elt["id"][0]
        data_finale[id2] = elt

    data_finale = (len(data_finale), data_finale)
    return data_finale