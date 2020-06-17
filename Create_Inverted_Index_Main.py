import os
import time
from Needed_Functions import Create_Inverted_Index, makeup, merge_dicts, open_directory, good_print
from multiprocessing import Pool

big_list = []

if __name__ == '__main__':
    main_address = 'C:/Users/HP/Desktop/Course_work/Datasets/'
    path1 = main_address + 'neg1'
    path2 = main_address + 'neg2'
    path3 = main_address + 'pos1'
    path4 = main_address + 'pos2'
    path5 = main_address + 'unsupp'

    list_of_files1 = os.listdir(path=path1)
    list_of_files2 = os.listdir(path=path2)
    list_of_files3 = os.listdir(path=path3)
    list_of_files4 = os.listdir(path=path4)
    list_of_files5 = os.listdir(path=path5)

    big_list = list_of_files1 + list_of_files2 + list_of_files3 + list_of_files4 + list_of_files5

    text_list1 = open_directory(list_of_files1, path1)
    text_list2 = open_directory(list_of_files2, path2)
    text_list3 = open_directory(list_of_files3, path3)
    text_list4 = open_directory(list_of_files4, path4)
    text_list5 = open_directory(list_of_files5, path5)

    main_text_list = text_list1 + text_list2 + text_list3 + text_list4 + text_list5

    text_list6 = text_list5[500:]
    text_list5 = text_list5[:500]

    number_of_threads = 5

    start_time = time.time()

    if number_of_threads == 1:
        args_my = [[text_list1 + text_list2, main_text_list], [text_list3 + text_list5, main_text_list],
                   [text_list4 + text_list6, main_text_list]]
        inverted_index1 = Create_Inverted_Index(args_my[0])
        inverted_index2 = Create_Inverted_Index(args_my[1])
        inverted_index3 = Create_Inverted_Index(args_my[2])
        result = [inverted_index1, inverted_index2, inverted_index3]
        result = merge_dicts(result)
        result = makeup(result)
        good_print(result)
        print(time.time() - start_time)

    elif number_of_threads == 3:
        args_my = [[text_list1 + text_list2 + text_list3, main_text_list], [text_list4 + text_list5, main_text_list],
                   [text_list6, main_text_list]]
        pool = Pool(processes=3)
        result = pool.map(Create_Inverted_Index, args_my)
        result = merge_dicts(result)
        result = makeup(result)
        good_print(result)
        print(time.time() - start_time)

    elif number_of_threads == 4:
        args_my = [[text_list1 + text_list2, main_text_list], [text_list3 + text_list4, main_text_list],
                   [text_list5, main_text_list], [text_list6, main_text_list]]
        pool = Pool(processes=4)
        result = pool.map(Create_Inverted_Index, args_my)
        result = merge_dicts(result)
        result = makeup(result)
        good_print(result)
        print(time.time() - start_time)

    elif number_of_threads == 5:
        args_my = [[text_list1 + text_list2, main_text_list], [text_list3, main_text_list], [text_list4, main_text_list],
                   [text_list5, main_text_list], [text_list6, main_text_list]]
        pool = Pool(processes=5)
        result = pool.map(Create_Inverted_Index, args_my)
        result = merge_dicts(result)
        result = makeup(result)
        result = good_print(result)
        print(time.time() - start_time)

    with open('out.txt', 'w') as out:
        for key, val in result.items():
            out.write('{}:{}\n'.format(key, val))
