class Circle:
    def __init__(self, r):
       radius = r


    def get_radius(self, r):
        return r

    def surface_area(self, r):
        surfacearea = 4 * 3.14 * (r*r)
        return surfacearea

    def volume(self,r):
        volumenum = (4/3) * 3.24 * (r * r *r)
        return volumenum









def main():
    inp = int(input('Write a radius: '))

    er =  Circle(inp)


    print('The radius is', er.get_radius(inp))
    print('The surface area is', er.surface_area(inp))
    print('The volume is', er.volume(inp))


main()