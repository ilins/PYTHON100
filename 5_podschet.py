def podvar_001(x,y,z,f):
    result = (x*(y-x)/z + x + (f+z)/f**y - (z-f)/z)/((z+f)/z**y -f)
    return result

print(podvar_001(5,2.3,2,7.8))
print(podvar_001(1234,37872,1231,12314))