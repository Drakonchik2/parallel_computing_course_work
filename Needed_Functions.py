def clean_string(str):
    symbols = ['.', ',', '(', ')', '!', '?', '*', ':', ';', '"', '{', '}', '~', '%', '&', '$', "::", '#', '##', "'",
            '/', '+', '=', '>', '@']
    str = str.replace('<br />', '')
    str = str.replace('-', '')
    str = str.replace('//', '')
    str = str.replace('/////', '')
    str = str.replace('<bt><br>', '')
    for i in str:
        for j in symbols:
            if i == j:
                str = str.replace(i, ' ')
    str = str.replace('  ', ' ')
    str = str.replace('----', ' ')
    str = str.replace('--', ' ')
    return str

def open_directory(list_of_files, path):
    text_list = []
    for file in list_of_files:
        f = open(path + '/' + str(file))
        text = f.read()
        text = clean_string(text)
        text_list.append(text)
        f.close()
    return text_list


def work_string(string, index):
    list_words = string.split(' ')
    words_dict = {}
    for i in list_words:
        words_dict[i] = index
    return words_dict


def create_list_of_dict(lst, main_lst):
    list_of_dict = []
    for i in lst:
        list_of_dict.append(work_string(i, main_lst.index(i)))
    return list_of_dict


def merge_dicts(list_of_dict):
    j = 0
    inverted_index = {}
    while j < len(list_of_dict)-1:
        inverted_index = {k: [list_of_dict[j].get(k), list_of_dict[j+1].get(k)] for k in list_of_dict[j].keys() |
                          list_of_dict[j+1].keys()}
        list_of_dict[j+1] = inverted_index
        j += 1
    return inverted_index


def listmerge(lst):
    res = []
    for el in lst:
        res += listmerge(el) if isinstance(el, list) else [el]
    return res


def new_lst(lst):
    result_list = []
    for i in lst:
        if i != None:
            result_list.append(i)
    return result_list


def sort_lst(lst):
    lst.sort()
    return lst


def makeup(dict_my):
    for i in dict_my:
        dict_my[i] = listmerge(dict_my.get(i))
        dict_my[i] = new_lst(dict_my.get(i))
        dict_my[i] = sort_lst(dict_my.get(i))
    return dict_my


def Create_Inverted_Index(lst):
    list_of_dicts = create_list_of_dict(lst[0], lst[1])
    list_of_dicts = merge_dicts(list_of_dicts)
    result_dicts = makeup(list_of_dicts)
    return result_dicts


def good_print(dict_my):
    dict_my = dict(sorted(dict_my.items()))
    return dict_my



