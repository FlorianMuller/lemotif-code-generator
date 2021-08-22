import json

data = [
    # 1
    ["d"],
    # 2
    ["a"],
    # 3
    ["a"],
    # 4
    ["w", "W"],
    # 5
    ["S", "s"],
    # 6
    ["R"],
    # 7
    ["R"],
    # 8
    ["u"],
    # 9
    ["w", "W"],
    # 10
    ["0", "EI", "IE", "E", "e", "O"],
    # 11
    ["u"],
    # 12
    ["AU", "UA", "au", "ua", "A", "U", "a", "u"],
    # 13
    ["p"],
    # 14
    ["R"],
    # 15
    ["A", "C"],
    # 16
    ["R"],
    # 17
    ["S"],
    # 18
    ["n"]
]

def format_for_youtube(base_lst):
    new_lst = ['https://www.youtube.com/watch?v=' + res[:11] for res in base_lst]
    # removing duplicate
    new_lst = list(set(new_lst))

    return new_lst

def format_for_unsonparjour(base_lst):
    return ['https://www.unsonparjour.com/' + res for res in base_lst]

def save_files(name, result_lst):
    with open(f"{name}.json", "w") as f:
        json.dump({"data": data, "results": result_lst}, f)
    
    with open(f"{name}.txt", "w") as f:
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
        save_files("youtube_result", format_for_youtube(res_lst))
        save_files("unsonparjour_result", format_for_unsonparjour(res_lst))

    print(f'\n\n {len(res_lst)} result found')

if __name__ == '__main__':
    main(True, True)
