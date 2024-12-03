class Node:

    def __init__(self, name):
        self.name = name
        self.childs = []
        self.metadata = []

    def add_child(self, child_node):
        self.childs.append(child_node)

    def add_meta_data(self, meta_data):
        self.metadata.append(meta_data)

    def get_meta_sum(self):
        result = 0
        for child in self.childs:
            result += child.get_meta_sum()
        for meta in self.metadata:
            result += meta
        return result

    def get_value(self):
        result = 0
        if len(self.childs) == 0:
            for meta in self.metadata:
                result += meta
            return result
        else:
            for meta in self.metadata:
                if meta == 0:
                    continue
                elif meta <= len(self.childs):
                    result += self.childs[meta - 1].get_value()
        return result


def parse_tree(id, int_list, index):
    counter = id
    new_node = Node(counter)
    childs = int_list[index]
    meta = int_list[index + 1]
    index += 2
    for i in range(childs):
        counter += 1
        result = parse_tree(counter, int_list, index)
        new_node.add_child(result[0])
        index = result[1]

    for i in range(meta):

        new_node.add_meta_data(int_list[index])
        index += 1
    return (new_node, index)

def solve_part_one(int_list):
    root = parse_tree(0, int_list, 0)[0]
    return root.get_meta_sum()

def solve_part_two(int_list):
    root = parse_tree(0, int_list, 0)[0]
    return root.get_value()

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

input_list = []

for line in Lines:
    input_line= line.strip()
    input_list = [int(x) for x in input_line.split(" ")]
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(input_list)))

print("TASK 2 - sol: {}".format(solve_part_two(input_list)))
