def init_space(size):
    array=[]
    for i in range(size):
        array.append(i)
    return array

def distributex(obj,space,spacebtw,width,remove):
    if not remove:
        if obj in space:
            objindex=space.index(obj)
            return objindex*(width+spacebtw)
        else:
            for num in range(len(space)):
                if num==space[num]:
                    space[num]=obj
                    return num*(width+spacebtw)
    else:
        if obj in space:
            objindex=space.index(obj)
            space[objindex]=objindex
            return True
        else:
            return False