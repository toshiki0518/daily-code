from linkedlist import LinkedList
def create_list():
    a_list = LinkedList()
    a_list.append("tuesday")
    a_list.append("wednesday")
    return a_list

def search_list():
    a_list = create_list()
    print(a_list)
    search = a_list.search("wednesday")
    print(search)
    search = a_list.search("sunday")
    print(search)
# def create_linked_list() -> Node:
#     node = Node('test', )

def create_rand_list():
    import random
    a_list = LinkedList()

    for i in range(0, 20):
        j = random.randint(1, 30)
        a_list.append(j)
        print(j, end=" ")

    print(a_list.search(10))
    print(10 in a_list)
    return a_list

def create_str_rand_list():
    import random
    import string

    alphabet = list(string.ascii_lowercase)  # アルファベットの小文字のリストを作成

    # random_list = [random.choice(alphabet) for _ in range(10)]  # ランダムな文字を10個選んでリストに追加
    random_list = LinkedList()  # 空のリストを作成

    for _ in range(4):
        random_char = random.choice(alphabet)  # アルファベットからランダムに文字を選択
        random_list.append(random_char)  # リストに選択された文字を追加

    print(random_list)
    return random_list

def remove_list():
    a_list = create_list()
    target = "tuesday"
    if target in a_list:
        a_list.remove(target)
        print('remove')
        print(a_list)

def reverse_list():
    a_list = create_str_rand_list()
    a_list.reverse()
    print(a_list)

def create_cycle():
    a_list = LinkedList()
    a_list.append("a")
    a_list.append("b")
    a_list.append("c")
    return a_list

def search_cycle():
    a_list = create_cycle()
    result = a_list.detect_cycle()
    print(result)

search_cycle()
# reverse_list()
# remove_list()
# search_list()
# create_rand_list()

