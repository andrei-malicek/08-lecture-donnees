FILENAME = "listes.csv"


def read_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                data.append([int(x) for x in line.split(';')])
    return data


def get_list_k(data, k):
    return data[k]


def get_first(l):
    return l[0] if l else None


def get_last(l):
    return l[-1] if l else None


def get_max(l):
    return max(l) if l else None


def get_min(l):
    return min(l) if l else None


def get_sum(l):
    return sum(l)


def main():
    data = read_data(FILENAME)
    for i, lst in enumerate(data):
        print(i, lst)
    k = 37
    print(k, get_list_k(data, k))


if __name__ == "__main__":
    main()
