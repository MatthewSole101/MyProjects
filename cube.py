class Cube:
    def __init__(self, l):
        length = l
    def get_volume(self,l):
        volume = l * l * l
        return volume
    def get_surfacearea(self,l ):
        area = l*l
        sarea = 6*(l*l)
        return sarea






def main ():

    length = int(input('What is the length of the cube: '))

    f = Cube(length)

    print('The volume is', f.get_volume(length),' and the surface area is', f.get_surfacearea(length))



main()