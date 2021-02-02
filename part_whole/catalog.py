from part_whole.Component import Component

class Catalog(Component):
    def __init__(self, name):
        super().__init__(name)
        # self.name = name              # 目录的名字
        self.children = []            # 子节点列表

    # 向该目录下添加一个目录或叶节点
    def add(self, leaf):
        self.children.append(leaf)

    # 以字符串为名字的节点是否在子节点列表中，若在返回下标，不在返回-1
    def name_in(self, name):
        for i in range(len(self.children)):
            child = self.children[i]
            if name == child.name:
                return i
        return -1

    # 删除该目录下的以leaf_name为名字的子节点，若无抛出异常
    def delete(self, leaf_name):
        index = self.name_in(leaf_name)
        if index >= 0:
            del self.children[index]
        else:
            raise Exception("Catalog without the deleted items")

    # 展示树形结构
    def display(self, depth):
        print('-'*depth + self.name)
        for child in self.children:
            child.display(depth+2)