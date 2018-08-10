def measure():
    """测量"""
    print("start...")
    temp = 39
    wetness = 50
    print("end...")

    return temp, wetness


result = measure()
print(result)

print(result[0])
print(result[1])

gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
