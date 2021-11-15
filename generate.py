import os
import json
import pandas as pd

from data import data

RESULT_DIR = "result"
if not os.path.exists(RESULT_DIR):
    os.makedirs(RESULT_DIR)


def format_no_case(base_lst):
    new_lst = [res.upper() for res in base_lst]
    # removing duplicate
    return list(set(new_lst))

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

def save_files(name, result_lst, to_txt=True, to_json=True, to_csv=False):
    if to_txt:
        with open(f"{RESULT_DIR}/{name}.json", "w") as f:
            json.dump({"data": data, "results": result_lst}, f)

    if to_json:
        with open(f"{RESULT_DIR}/{name}.txt", "w") as f:
            f.write("Résultats:\n" + '\n'.join(result_lst) + "\n\n\nParamètres:\n" + json.dumps(data, indent=4))

    if to_csv:
        df = pd.DataFrame({"url": result_lst})
        df.to_csv(f"{RESULT_DIR}/{name}.csv")


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
        # Simple code list
        save_files("result", res_lst)
        save_files("result_nocase", format_no_case(res_lst))
        
        # Youtube format
        # save_files("youtube_result", format_for_youtube(res_lst))
        
        # `unsonparjour.com/[CODE]` format
        save_files("unsonparjour_result", format_for_unsonparjour(res_lst))
        save_files("unsonparjour_nocase_result", format_for_unsonparjour_no_case(res_lst), to_csv=True)

    print(f'\n\n- {len(res_lst)} result found')
    print(f'- {len(format_no_case(res_lst))} result found with no case')


if __name__ == '__main__':
    main(False, True)
