import colorama

map1 = [
    ['██', '██', '██', '██', '██', '██', '██'],
    ['██', '  ', '  ', '  ', '  ', 'BB', '██'],
    ['██', '  ', '██', '██', '██', '██', '██'],
    ['██', '  ', '  ', '  ', '██', '██', '██'],
    ['██', '██', '██', '  ', '██', '██', '██'],
    ['██', 'AA', colorama.Back.GREEN+'  ', '  ', '██', '██', '██'],
    ['██', '██', '██', '██', '██', '██', '██']
]

def displaymap(maptoprint):
    for row in maptoprint:
        for cell in row:
            print(cell, end='')
        print()

displaymap(map1)