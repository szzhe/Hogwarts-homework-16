import pytest
from part_whole.catalog import Catalog
from part_whole.leaf import Leaves

class TestZh:
    def test_szz(self):
        root = Catalog("root")
        SubCatalog1 = Catalog("SubCatalog1")
        SubCatalog2 = Catalog("SubCatalog2")
        leaf1 = Leaves("leaf1", "1")
        leaf2 = Leaves("leaf2", "2")
        leaf3 = Leaves("leaf3", "3")
        leaf4 = Leaves("leaf4", "4")

        root.add(SubCatalog1)
        root.add(SubCatalog2)
        root.add(leaf1)

        SubCatalog1.add(leaf2)
        SubCatalog1.add(leaf3)
        SubCatalog1.add(leaf4)

        # root.display(0)

        # SubCatalog2.delete("leaf4")
        # root.display(0)

        new_leaf1 = Leaves("new_leaf1", "1")
        # leaf1.add(new_leaf1)  # Exception: Leaf nodes can't insert catalog

        new_leaf2 = Leaves("new_leaf2", "2")
        SubCatalog2.add(new_leaf1)
        SubCatalog2.add(new_leaf2)
        # root.display(0)

        # root.delete("SubCatalog2")
        root.display(0)

if __name__ == '__main__':
    pytest.main(["test_zuhe.py", "-s", "-v"])