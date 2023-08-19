# Створіть метаклас, який викидає помилку при спробі створити клас з атрибутами, що починаються з
# '__' (два нижніх підкреслення)

class NoDunderAttributes(type):
    def __new__(cls, name, bases, attrs):
        for el in attrs.keys():
            if f'_{name}__' in el:
                raise AttributeError('Cannot have attribute names starting with "__"')
        return super().__new__(cls, name, bases, attrs)


class MyPrivateClass(metaclass=NoDunderAttributes):
    __secret_attribute = 10 # Raises error: 'Cannot have attribute names starting with "__"'
