from collections import namedtuple

Obj_w_id_name = namedtuple('Obj', "id name")

user = Obj_w_id_name(id =1, name = 'sven')

print(user.id, user.name)