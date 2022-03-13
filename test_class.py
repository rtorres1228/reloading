class PERSON:
    @classmethod
    def print_all(cls):
        child_classes = cls.__subclasses__()
        for child_class in child_classes:
            print('this all the full names {0}, {1}'.format(child_class.name, child_class.last_name))

class Roberto(PERSON):
    name = 'Roberto'
    last_name= 'Torres'
    def __init__(self):
        ...


class MD(PERSON):
    name = 'MD'
    last_name = 'Ullah'

    def __init__(self):
        ...

def main():
    PERSON.print_all()

if __name__ == '__main__':
    print('running test')
    main()
    
