class Coord:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __repr__(self):
        return f'({self.row}, {self.column})'


class Place:
    def __init__(self, coord: Coord, neib_coord):
        self.coord = coord
        self.neib_coord = neib_coord
        self.item = None


class VPlace:
    def __init__(self, me: Coord, place: Place):
        self.me = me  # Визуальные координаты
        self.place = place  # не визуальные


class Column:
    def __init__(self, column):
        self.column = column
        self.places = []

    def add(self, col, row, vplace, item):
        self.places.append(vplace)
        row = vplace.me.row
        col = vplace.me.column


class VTable:
    table_text = '''
          7/3           
     9/5   |   8/4      
6/4   |   6__   |       
 |   6__   |   6__      
5__   |   5__   |       
 |   5__   |   5__      
 |    |   4__   |   3/2 
 |   4__   |   4__   |  
3__   |    |    |   3__ 
 |   3__   |   3__   |  
2__   |   2__   |   2__ 
 |   2__   |   2__   |  
1__   |   1__   |   1__ 
 |   1__   |   1__   |  
 |    |    |    |    |  
 =    =    =    =    =

'''

    def __init__(self):
        self.table = []
        for row in VTable.table_text.split('\n'):
            self.table.append(list(row))

        # row=5, col=1   -> vrow=5, vcol=4
        self.column = Column(1)
        vp = VPlace(Coord(row=1, column=5), Place(coord=Coord(row=4, column=5), neib_coord=[]))

    def __repr__(self):
        s = []
        for row in self.table:
            s.append("".join(row))
        return '\n'.join(s)

    def append(self, coord, item, vplace):
        row = coord.row
        col = coord.column
        # потом вcтавлять в тот column и на этаж row
        self.column.add(col, row, vplace, item)


t = VTable()

# Вызов метода add_item и передача соответствующих аргументов
coord = Coord(row=5, column=1)
item = "X"
vplace = VPlace(Coord(row=5, column=4), Place(coord=Coord(row=4, column=5), neib_coord=[]))

t.append(coord, item, vplace)
print(t)
