class chaiOrder:
    def __init__(self, tea_type, sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(order_data['tea_type'], order_data['sweetness'], order_data['size'])

    @classmethod
    def from_string(cls, order_data):
        tea_type, sweetness, size = order_data.split('-')
        return cls(tea_type, sweetness, size)
            
class chaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ['small', 'medium', 'large']

order1 = chaiOrder.from_dict({'tea_type': 'green', 'sweetness': 'medium', 'size': 'large'})
order2 = chaiOrder.from_string('black-high-small')

print(order1.__dict__)
print(order2.__dict__)
