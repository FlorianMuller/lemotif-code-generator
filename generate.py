import json
import string

RESULT_DIR = "result"

all = list(string.ascii_letters)
data = [
    # 1  [100%]
    ["d"],
    # 2  [100%]
    ["a"],
    # 3  [100%]
    ["a"],
    # 4  [100%]
    ["w", "W"],
    # 5  [  5%] 🧠
    ["S", "s"],
    # 6  [100%]
    ["R"],
    # 7  [100%]
    ["R"],
    # 8  [ 20%] 🧠
    ["u"],
    # 9  [100%]
    ["w", "W"],
    # 10 [ 50%] 🧠
    ["0"],
    # "EI", "IE", "E", "e", "O"],
    # 11 [100%]
    ["u"],
    # 12 [ 70%]
    ["AU", "UA", "au", "ua"],
    #  "A", "U", "a", "u"],
    # 13 [100%]
    ["p"],
    # 14 [100%]
    ["R"],
    # 15 [ 75%]
    ["A", "C", "O"],
    # 16 [ 99%]
    ["R"],
    # 17 [100%]
    ["S"],
    # 18 [100%]
    ["n"],
    # 19 [100%]
    ["u"],
    # 20 🧠 🧠 🧠
    all,
    # 21 [90%]
    ["V"],
    # 22 [ 50%] 🧠
    ["O", "o"],
    # "0"],
    # 23 [100%]
    ["n", "N"],
    # 24 [  1%] 🧠
    ["J", "j"],
    # 25 [ 99%]
    ["J", "j"],
    # 26
    # rien
    # 27.1 [ 99%]
    ["M", "m"],
    # "13"],
    # 27.2 [100%]
    ["0"],
    # 28 [100%]
    ["0"],
    # 29 [100%]
    ["8"],
    # "H", "h"],
    # 30 [100%]
    ["4"]
    # "D", "d"]
]

def format_for_youtube(base_lst):
    new_lst = ['https://www.youtube.com/watch?v=' + res[:11] for res in base_lst]
    # removing duplicate
    new_lst = list(set(new_lst))

    return new_lst

def format_for_unsonparjour(base_lst):
    return ['https://www.unsonparjour.com/' + res for res in base_lst]

def format_for_unsonparjour_no_case(base_lst):
    new_lst = ['https://www.unsonparjour.com/' + res.upper() for res in base_lst]
    # removing duplicate
    new_lst = list(set(new_lst))
    return new_lst



def save_files(name, result_lst):
    with open(f"{RESULT_DIR}/{name}.json", "w") as f:
        json.dump({"data": data, "results": result_lst}, f)
    
    with open(f"{RESULT_DIR}/{name}.txt", "w") as f:
        f.write("Résultats:\n" + '\n'.join(result_lst) + "\n\n\nParamètres:\n" + json.dumps(data, indent=4))

def next_index(index_lst):
    for i, index in list(enumerate(index_lst))[::-1]:
        if index + 1 >= len(data[i]):
            index_lst[i] = 0
            i -= 1
        else:
            index_lst[i] += 1
            break
    
    return index_lst

def main(print_res, save):
    index_lst = [0] * len(data)
    res_lst = []

    # Generating code list
    while len(res_lst) == 0 or sum(index_lst) != 0:
        next_index(index_lst)
        res_lst.append(''.join([possibility[index_lst[i]] for i, possibility in enumerate(data)]))

    if print_res:
        print('\n'.join(res_lst))
    
    if save:
        save_files("result", res_lst)
        # save_files("youtube_result", format_for_youtube(res_lst))
        save_files("unsonparjour_result", format_for_unsonparjour(res_lst))
        save_files("unsonparjour_nocase_result", format_for_unsonparjour_no_case(res_lst))

    print(f'\n\n {len(res_lst)} result found')

if __name__ == '__main__':
    main(False, True)
