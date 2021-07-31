# TODO
#   - lot of test
#   - should work with dict, list, tuple

# TODO: Some useful preimplemented verifier:
#   - has_len() or SomeWithLen()
#   - is_in() or SomeIn()
#   - expect_strict()
#   - Email
#   - Json (as string for exampel)
#

# FEATURES/IDEAS/MAYBE:
#   - .why() -> auto-assert with explanation? (maybe some other form of explanation)
#   - left Side of dict {"a": 12} in VSet({Some(str): 12}) -> needs to be hashable -> then also set?
#   - also useful as iterator and template for fast creation? -> need to give the wildcards a name?

class VSet:
    def __init__(self, template):
        self.template = template
        pass

    def __contains__(self, item):
        return self.template == item


class Some:
    # Todo:
    #  - verifiable with arg function
    #  - strict? no subclasses -> Strict itself is a subclass of Some
    #       or as option for Some but then valid for all
    #  - also except other Some as args so
    #       - EMail(Some): -> VSet({"mail": Some(EMail, str)})
    #       - Some(Strict(int), str)

    def __init__(self, *args):
        self.types = args

    def __eq__(self, other):
        for t in self.types:
            if isinstance(other, t):
                return True
        return False

class Foo:
    def __init__(self):
        pass

class Foo2(Foo):
    def __eq__(self, other):
        return False
    pass




