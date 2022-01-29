'''
    
hackinscience.org

Training #15

Find the distance between the two furthest apart values in a list.
    
'''


def dist(points):
    distance = 0
    for idx, element1 in enumerate(points):
        for element2 in points:
            temp_distance = abs(element2 - element1)
            if temp_distance > distance:
                distance = temp_distance
    return distance
