import random
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
        ret.append((li[0][0],li[-1][0]))
        li=li[1:-2]
    return ret


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

def greedy_method(data):
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

        for elt in random.sample(dict_photo.keys(), min(len(dict_photo),10)):
            slide_tmp = dict_photo[elt].copy()
            tmp_score = score_two_list(slide_before["list_tag"], slide_tmp["list_tag"])
            if tmp_score >= min_score:
                slide_after = slide_tmp.copy()
                min_score = tmp_score
                id_supr = elt
            if min_score == max_theorique:
                break
        score_total = score_total + min_score
        del dict_photo[id_supr]

    result.append(slide_after)
    print(score_total)
    return result

print(doublets(data))
