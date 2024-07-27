import math

angle_degrees = int(input())

angle_radians = angle_degrees * (math.pi / 180)

cotangent = 1 / math.tan(angle_radians)

print(round(cotangent, 10))
