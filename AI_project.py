import random
import pygame
import sys

STEPS = 1000
GEN = 20
X_LIM = 180
Y_LIM = 0
GRID_SIZE = 200
num_objects = 1000
mutation_factor = 50
geneNo = 100
CELL_SIZE = 3
ratio_Collector = [None] * GEN

CNT = 0

two_d_array = [[
    1 if i == 0 or i == GRID_SIZE - 1 or j == 0 or j == GRID_SIZE - 1 else 0
    for j in range(GRID_SIZE)
] for i in range(GRID_SIZE)]

#Coll
for j in range(0,180):
  two_d_array[j][int(GRID_SIZE/2)] = 1

# for j in range(120,200):
#   two_d_array[j][int(GRID_SIZE/2)+20] = 1


objects = []

pygame.init()


screen_width = GRID_SIZE * CELL_SIZE
screen_height = GRID_SIZE * CELL_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GAME")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)

#clock = pygame.time.Clock()


class CustomObject:
  next_id = 1  # Class variable to keep track of the next object ID

  # Adjust as needed

  def __init__(self, x, y, lr_value, ud_value, t_value, hv_value, pass_value):
    self.obj_id = CustomObject.next_id
    CustomObject.next_id += 1
    self.x = x
    self.y = y
    self.lr_value = random.randint(1, geneNo)
    self.ud_value = random.randint(1, geneNo)
    self.hv_value = random.randint(1, geneNo)
    self.pass_value = random.randint(1, geneNo)
    self.t_value = round(random.uniform(1, geneNo))

  def __str__(self):
    return f"O{self.obj_id}: (x={self.x}, y={self.y}), HV={self.hv_value}, LR={self.lr_value}, UD={self.ud_value}, T={self.t_value}, P = {self.pass_value}"

  # def generate_child(self, parent2):
  #     lr_child = (self.lr_value + parent2.lr_value) // 2
  #     ud_child = (self.ud_value + parent2.ud_value) // 2
  #     t_child = (self.t_value + parent2.t_value) // 2
  #     hv_child = (self.hv_value + parent2.t_value) // 2
  #     child = CustomObject(self.x, self.y)

  #     return child
  def generate_child(self, parent2, mutation_constant):
    # Calculate the average of corresponding attributes
    lr_child = 0
    ud_child = 0
    t_child = 0
    hv_child = 0
    pass_child = 0
    # Apply mutation to the child's values


    # Create a new child object with mutated values
    child = CustomObject(self.x,
                         self.y,
                         lr_value=lr_child,
                         ud_value=ud_child,
                         t_value=t_child,
                         hv_value=hv_child,
                         pass_value=pass_child)

    return child

  @classmethod
  def reset_next_id(cls):
    cls.next_id = 1


#This is for making new babies with 2 parents and add it to objects
def makingNewGen():
  if len(objects) > 0:
    temp_objects = []
    a = 1
    b = 1
    for i in range(num_objects):

      parent1 = random.choice(objects)
      parent2 = random.choice(objects)

      # Generate a child from the selected parents
      child = parent1.generate_child(parent2, mutation_factor)

      child.x = a
      child.y = b
      two_d_array[b][a] = 1
      b = b + 1

      if b == GRID_SIZE - 1:
        a = a + 1
        b = 1
      # Print information about the parents and the child
      child = newChildGeneration(parent1,parent2,child)

      temp_objects.append(child)
      #PRINT
      #print(f"Child: {child}")
      two_d_array[child.y][child.x] = f"O{child.obj_id}"
    # Reset the next_id counter for the new generation
    CustomObject.reset_next_id()

    #kill parents
    for ob in objects:
      Xi = ob.x
      Yi = ob.y
      two_d_array[Yi][Xi] = 0
    objects.clear()
  else:
    print("The list is empty.")

  return temp_objects


def newChildGeneration(obj1,obj2,child):
  # for i in range(1,mutation_factor):
  #   if i % mutation_factor == 0:
  #     HV = random.randint(1, geneNo)
  #     LR = random.randint(1, geneNo)
  #     UD = random.randint(1, geneNo)
  #     T = round(random.uniform(1, geneNo))
  #     print("HV=" + int(HV) + " LR=" + int(LR) + " UD=" + int(UD) + " T=" + int(T) )
  #   else:
  #     HV = int((obj1.hv_value + obj2.hv_value)/2)
  #     LR = int((obj1.lr_value + obj2.lr_value)/2)
  #     UD = int((obj1.ud_value + obj2.ud_value)/2)
  #     T = int((obj1.t_value + obj2.t_value)/2)
  # child.hv_value = HV
  # child.lr_value = LR
  # child.ud_value = UD
  # child.t_value = T
  global CNT
  CNT = CNT + 1
  if CNT % mutation_factor == 0:
    HV = random.randint(1, geneNo)
    LR = random.randint(1, geneNo)
    UD = random.randint(1, geneNo)
    P = random.randint(1, geneNo)
    T = round(random.uniform(1, geneNo))
    CNT = 0
    #print("HV=" + str(HV) + " LR=" + str(LR) + " UD=" + str(UD) + " T=" + str(T) )

  else:
    HV = int((obj1.hv_value + obj2.hv_value)/2)
    LR = int((obj1.lr_value + obj2.lr_value)/2)
    UD = int((obj1.ud_value + obj2.ud_value)/2)
    P = int((obj1.pass_value + obj2.pass_value)/2)
    T = int((obj1.t_value + obj2.t_value)/2)
  child.hv_value = HV
  child.lr_value = LR
  child.ud_value = UD
  child.pass_value = P
  child.t_value = T

  return child

def generate_output(n):
  if n == 0:
    return 0
  else:
    # Probability for +1 is n/10, for -1 is 1 - (n/10)
    return 1 if random.random() < n / geneNo else -1


def moving():
  j = 0
  update_display()
  for obj in objects:
    t = generate_output(obj.t_value)
    hv = generate_output(obj.hv_value)
    lr = generate_output(obj.lr_value)
    ud = generate_output(obj.ud_value)
    p = generate_output(obj.pass_value)
    if t > 0:

      if hv > 0:

        if lr > 0:
          if two_d_array[obj.y][obj.x + 1] != 1:
            two_d_array[obj.y][obj.x + 1] = 1
            two_d_array[obj.y][obj.x] = 0
            obj.x = obj.x + 1
            two_d_array[obj.y][obj.x] = f"O{obj.obj_id}"
          elif p > 0:
            if ud > 0:
              if two_d_array[obj.y + 1][obj.x] != 1:
                two_d_array[obj.y + 1][obj.x] = 1
                two_d_array[obj.y][obj.x] = 0
                obj.y = obj.y + 1
                two_d_array[obj.y][obj.x] = f"O{obj.obj_id}"
            else:
              if two_d_array[obj.y - 1][obj.x] != 1:
                two_d_array[obj.y - 1][obj.x] = 1
                two_d_array[obj.y][obj.x] = 0
                obj.y = obj.y - 1
                two_d_array[obj.y][obj.x] = f"O{obj.obj_id}"
        else:
          if two_d_array[obj.y][obj.x - 1] != 1:
            two_d_array[obj.y][obj.x - 1] = 1
            two_d_array[obj.y][obj.x] = 0
            obj.x = obj.x - 1
            two_d_array[obj.y][obj.x] = f"O{obj.obj_id}"
      else:

        if ud > 0:
          if two_d_array[obj.y + 1][obj.x] != 1:
            two_d_array[obj.y + 1][obj.x] = 1
            two_d_array[obj.y][obj.x] = 0
            obj.y = obj.y + 1
            two_d_array[obj.y][obj.x] = f"O{obj.obj_id}"
        else:
          if two_d_array[obj.y - 1][obj.x] != 1:
            two_d_array[obj.y - 1][obj.x] = 1
            two_d_array[obj.y][obj.x] = 0
            obj.y = obj.y - 1
            two_d_array[obj.y][obj.x] = f"O{obj.obj_id}"
    #print("t=" + str(t) + " hv=" + str(hv) + " lr=" + str(lr) + " ud=" + str(ud) )
    # for row in two_d_array:
    #     print(row)


# n = STEPS
def movements_oneGen(n):
  for i in range(1, n + 1):

    moving()


def kill(x_lim,y_lim):
  # KILL LEFT
  # filter_condition = lambda obji: obji.x >= x_lim
  # filtered_list = list(filter(filter_condition, objects))

  # filter_condition = lambda objil: objil.x < x_lim
  # filtered_objects_toMakeArray0 = list(filter(filter_condition, objects))

  # for obji in filtered_objects_toMakeArray0:
  #     two_d_array[obji.y][obji.x] = 0

  # KILL RIGHT
  # filter_condition = lambda obji: obji.x <= x_lim
  # filtered_list = list(filter(filter_condition, objects))

  # filter_condition = lambda objil: objil.x > x_lim
  # filtered_objects_toMakeArray0 = list(filter(filter_condition, objects))

  # for obji in filtered_objects_toMakeArray0:
  #     two_d_array[obji.y][obji.x] = 0

  #KILL UP
  filtered_objects = [obj for obj in objects if obj.x < x_lim or obj.y < y_lim]
  print("KILL")
  for obji in filtered_objects:
    two_d_array[obji.y][obji.x] = 0


  newfObjects = [obj for obj in objects if obj.x >= x_lim and obj.y >= y_lim]
  print("ENDKILL")

  return newfObjects


def update_display():
  # Clear the screen
  screen.fill(WHITE)

  # Draw the 2D array
#   for i in range(GRID_SIZE):
#     for j in range(GRID_SIZE):
#       if two_d_array[i][j] != 0:
#         pygame.draw.rect(screen, RED,
#                          (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
  for obj in objects:
    pygame.draw.rect(screen, RED,
                         (obj.x * CELL_SIZE, obj.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

  for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
      if two_d_array[i][j] == 1:
        pygame.draw.rect(screen, BLUE,
                         (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
  # Update the display
  pygame.display.flip()


a = 1
b = 1
for _ in range(num_objects):
  x_coord = a
  y_coord = b
  two_d_array[b][a] = 1
  obj = CustomObject(x_coord, y_coord, 0, 0, 0, 0, 0)
  b = b + 1
  if b == GRID_SIZE - 1:
    a = a + 1
    b = 1

  two_d_array[obj.y][obj.x] = f"O{obj.obj_id}"
  objects.append(obj)

# Select two objects randomly

for i in range(GEN):

  print("NEWGEN = " + str(i))
  # for obj in objects:
  #     print(obj)
  movements_oneGen(STEPS)
  # print("BeforeKill")
  # print(objects)
  # for row in two_d_array:
  #     print(row)

  objects = kill(X_LIM,Y_LIM)
  pygame.display.set_caption("GEN" + str(i) + "Survive ratio = " + str(len(objects)/num_objects))
  r = len(objects)/num_objects
  ratio_Collector[i] = r
  # for obj in objects:
  #   print(obj)

  if len(objects) < 0:
    print("Everyone Died")
    break
  objects = makingNewGen()

movements_oneGen(STEPS)
objects = kill(X_LIM,Y_LIM)
ratio_Collector.append(len(objects)/num_objects)
print("Finallllll")
for row in two_d_array:
  print(row)

for obj in objects:
  print(obj)
for i in range(GEN+1):
  print("Survive ratio " + str(i+1) + " = " + str(ratio_Collector[i]))
#print("Survive ratio = " + str(len(objects)/num_objects))

#for obj in objects:
#    print(obj.obj_id)
