
class SingletonClass:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance
