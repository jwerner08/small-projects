def Get_Data():
    key_list_single = []
    value_list_single = []
    key_list_multiple = []
    value_list_multiple = []

    with open('GreekTransliterationTable.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            strip_rows = line.strip()
            get_all_values = strip_rows.split()
            get_keys = get_all_values[0].strip().split(',')
            value = get_all_values[1]
            for i in range(len(get_keys)):
                if len(get_keys[i]) != 1:
                    key_list_multiple.append(get_keys[i])
                    value_list_multiple.append(value)
                else:
                    key_list_single.append(get_keys[i])
                    value_list_single.append(value)
        f.close()

        dict_to_translate_single = {key_list_single[i]: value_list_single[i] for i in range(len(key_list_single))}
        multi_char_list = [[key_list_multiple[i], value_list_multiple[i]] for i in range(len(key_list_multiple))]
        dummy_string = 'abc'
        single_char_key_dict = dummy_string.maketrans(dict_to_translate_single)
        return single_char_key_dict, multi_char_list


def Transliterate():
    single_char_key_dict, multi_char_list = Get_Data()
    with open('GreekSentences.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            for i in multi_char_list:
                line = line.replace(i[0], i[1])
            line = line.translate(single_char_key_dict)
            print(line)
    f.close()


if __name__ == '__main__':
    Transliterate()
