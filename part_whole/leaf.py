from part_whole.Component import Component

class Leaves(Component):
    def __init__(self, name, value):
        super().__init__(name)
        self.children = []
        self.value = value              # 叶节点的值

    # 若向叶节点添加目录或叶节点抛出异常
    def add(self, leaf):
        raise Exception("Leaf nodes can't insert catalog")

    # 想在叶节点下访问子节点列表，抛出异常
    def name_in(self, name):
        raise Exception("Leaf nodes without subcatalog")

    # 想在叶节点下访问子节点列表，抛出异常
    def delete(self, leaf_name):
        raise Exception("Leaf nodes without subcatalog")