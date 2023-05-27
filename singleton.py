class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance: 'Singleton' = super(Singleton, cls).__new__(cls)
        return cls.instance

singleton = Singleton()
new_singleton = Singleton()
print(singleton is new_singleton)