import sys

filename = sys.argv[1]
r_value = int(sys.argv[2])
g_value = int(sys.argv[3])
b_value = int(sys.argv[4])

def distance3d(x1,y1,z1,x2,y2,z2):
    return ((x2 - x1)**2 +(y2 - y1)**2 +(z2 - z1)**2)**0.5

with open(filename, 'r') as f:
    colorlist = f.read()

colorlist = colorlist.split('\n')
closest_index = 0
distance = [None] * 150
for index, value in enumerate(colorlist):
    sp_color = colorlist[index].split('\t')
    deci_rgb = sp_color[2].split(',')
    r_list = int(deci_rgb[0])
    g_list = int(deci_rgb[1])
    b_list = int(deci_rgb[2])
    distance[index] = distance3d(r_value,g_value,b_value,r_list,g_list,b_list)
    if distance[index] < distance[closest_index]:
        closest_index = index

result = colorlist[closest_index].split('\t')
print(f'The most closest color is {result[0]}.')
