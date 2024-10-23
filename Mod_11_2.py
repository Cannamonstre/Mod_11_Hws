class SuperIntrospector3000:
    def __init__(self, class_obj):
        self.class_obj = class_obj

    def obj_type(self):
        return type(self.class_obj)

    def obj_attrs(self):
        return [attr for attr in dir(self.class_obj)
                if not callable(getattr(self.class_obj, attr))
                and not attr.startswith('__')]

    def obj_meds(self):
        return [med for med in dir(self.class_obj)
                if callable(getattr(self.class_obj, med))
                and not med.startswith('__')]

    def obj_mod(self):
        return getattr(self.class_obj, '__module__', None)

    def obj_info(self):
        return {
            'type': self.obj_type(),
            'attributes': self.obj_attrs(),
            'methods': self.obj_meds(),
            'module': self.obj_mod()
        }


test_obj_1 = [4, 44, 444]
analyzer = SuperIntrospector3000(test_obj_1)
print(analyzer.obj_info())

test_obj_2 = {'a': 13, 'b': 37}
analyzer = SuperIntrospector3000(test_obj_2)
print(analyzer.obj_info())

test_obj_3 = len
analyzer = SuperIntrospector3000(test_obj_3)
print(analyzer.obj_info())
