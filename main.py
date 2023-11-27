import random

class CustomObject:
    next_id = 1  # Class variable to keep track of the next object ID

    def __init__(self, x, y):
        self.obj_id = CustomObject.next_id
        CustomObject.next_id += 1
        self.x = x
        self.y = y
        self.lr_value = random.randint(-10, 10)
        self.ud_value = random.randint(-10, 10)
        self.t_value = round(random.uniform(0, 10))

    def __str__(self):
        return f"O{self.obj_id}: (x={self.x}, y={self.y}), LR={self.lr_value}, UD={self.ud_value}, T={self.t_value}"

GRID_SIZE = 5
num_objects = 3

two_d_array = [[1 if i == 0 or i == GRID_SIZE - 1 or j == 0 or j == GRID_SIZE - 1 else 0
                for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

objects = []
for _ in range(num_objects):
    x_coord = random.randint(1, GRID_SIZE - 2)
    y_coord = random.randint(1, GRID_SIZE - 2)

    obj = CustomObject(x_coord, y_coord)
    objects.append(obj)

    two_d_array[y_coord][x_coord] = f"O{obj.obj_id}"

for row in two_d_array:
    print(row)

for obj in objects:
    print(obj)
