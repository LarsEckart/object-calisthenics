class Collection:
    def __init__(self, collection = None):
        self.collection = collection or []

    def add(self, items):
        self.collection.extend(items)

    def display(self):
        return ["%s" % item for item in self.collection]

    def filter(self, filter_function):
        collection_list = filter(filter_function, self.collection)
        return self.__class__(collection_list)
