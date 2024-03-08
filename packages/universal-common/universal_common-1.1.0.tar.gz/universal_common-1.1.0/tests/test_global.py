from universal_common import coalesce, Dictionary

class TestGlobal:
    def test_coalesce_works(self):
        assert coalesce() is None
        assert coalesce(None, 1) == 1
        assert coalesce(2, 1) == 2
        assert coalesce(3) == 3
        assert coalesce(4, None) == 4

    def test_dictionary(self):
        dictionary: Dictionary = Dictionary({ "asdf": 1 })
        assert dictionary.asdf == 1
        assert dictionary["asdf"] == 1

        dictionary.b = 5
        assert dictionary.b == 5
        assert dictionary["b"] == 5

        assert dictionary.c is None

        del dictionary.b

        assert dictionary.b is None