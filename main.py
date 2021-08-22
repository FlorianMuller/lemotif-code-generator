import json

data = [
	["d"],
	["a"],
	["a"],
	["w", "W"],
	["S", "s"],
	["R"],
	["R"],
	["u"],
	["w", "W"],
	["0", "EI", "IE", "E", "e", "O"],
	["u"],
	# ["AU", "UA", "au", "ua", "A", "U", "a", "u"],
    # ["p"],
    # ["R"],
    # ["A", "C"],
    # ["R"],
    # ["S"],
    # ["n"]
]

def next_index(index_lst):
    for i, index in list(enumerate(index_lst))[::-1]:
        if index + 1 >= len(data[i]):
            index_lst[i] = 0
            i -= 1
        else:
            index_lst[i] += 1
            break
    
    return index_lst

def main(youtube_format, print_res, save):
    index_lst = [0] * len(data)
    res_lst = []

    # Generating code list
    while len(res_lst) == 0 or sum(index_lst) != 0:
        next_index(index_lst)
        res_lst.append(''.join([possibility[index_lst[i]] for i, possibility in enumerate(data)]))

    # Formating results

    if youtube_format:
        res_lst = ['https://www.youtube.com/watch?v=' + res[:11] for res in res_lst]
        # removing duplicate
        res_lst = list(set(res_lst))
    
    if print_res:
        print('\n'.join(res_lst))
    
    if save:
        with open("result.json", "w") as f:
            json.dump({"data": data, "results": res_lst}, f)

    print(f'\n\n {len(res_lst)} result found')

if __name__ == '__main__':
    main(True, True, True)
