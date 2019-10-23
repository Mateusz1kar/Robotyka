class punkt():
    def __init__(self,x,y,rx,ry,g,f):
        self.poz = [x, y]
        self.r_poz = [rx,ry]
        self.g=g
        self.f=f

#sprawdza czy punkt o podanej pozycji istnieje na liście
def g_fun(z=[]):
    if len(z)>0:
        return z[len(z) - 1].g + 1
    else:
        return 0

def przeszukanie(o=[punkt],x=int,y=int,miejsce=[int]):
    for i in range(len(o)):
        if (o[i].poz==[x,y]):
            miejsce[0]=i
            return False
    return True

def show_route(z=[]):
    wypisanie = z[len(z) - 1]
    print(wypisanie.poz)
    while (wypisanie.poz != wypisanie.r_poz):
        pozycja = [0]
        przeszukanie(z, wypisanie.r_poz[0], wypisanie.r_poz[1], pozycja)
        wypisanie = z[pozycja[0]]
        print(wypisanie.poz)
#otwieranie pliku i zwraca tablice dwu wymiarowo obrazujoncą mapę
def mapowanie(sciezka=""):
    try:
        file = open(sciezka)
        mapa = (file.read().split('\n'))
        for i in range(len(mapa)):
            mapa[i] = mapa[i].split(' ')
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                mapa[i][j] = (int(mapa[i][j]))
        file.close()
    except Exception as e:
        print(e)
    return mapa
# minimalna warość funkci f w tablicy pónków
def min_p (o=[]):
    min = 0
    for i in range(len(o)):
        if o[min].f > o[i].f:
            min = i
    # dodanie go do listy zamkniętej
    return min

def a_gwiadazda(sciezka="",start=[0,0], cel=[19,19]):
    mapa=mapowanie(sciezka)
    x = len(mapa)
    y = len(mapa[0])
    if x<cel[0] or y<cel[1]:
        cel = [x, y]
    z = []
    o = []
    o.append(punkt(start[0], start[1], start[0], start[1], 0, 0))
    x = start[0]
    y = start[1]
    # dodanie jego sąsiadów do listy otwartej
    while len(o) > 0:
        z.append(o.pop(min_p(o)))
        x = z[len(z) - 1].poz[0]
        y = z[len(z) - 1].poz[1]
        if (x != cel[0]) or (y != cel[1]):
            mapa[x][y] = 3
            # dodanie jego sąsiadów do listy otwartej + sprawdzenie czy nie są one już dodane
            if (y >= 0) and (x - 1 >= 0) and (y < len(mapa[0])) and (x - 1 < len(mapa)) and (mapa[x - 1][y] == 0):
                g_poz = g_fun(z)
                f_poz = g_poz + ((x - 1 - cel[0]) ** 2 + (y - cel[1]) ** 2) ** 0.5
                pozycja = [0]
                if przeszukanie(o, x - 1, y, pozycja):
                    o.append(punkt(x - 1, y, x, y, g_poz, f_poz))
                    #mapa[x - 1][y] = 2
                else:
                    if o[pozycja[0]].f > f_poz:
                        o[pozycja[0]].f = f_poz
                        o[pozycja[0]].r_poz = [x, y]

            if (y - 1 >= 0) and (x >= 0) and (y - 1 < len(mapa[0])) and (x < len(mapa)) and (mapa[x][y - 1] == 0):
                # print(11)
                g_poz = g_fun(z)
                f_poz = g_poz + ((x - cel[0]) ** 2 + (y - 1 - cel[1]) ** 2) ** 0.5
                pozycja = [0]
                if przeszukanie(o, x, y - 1, pozycja):
                    o.append(punkt(x, y - 1, x, y, g_poz, f_poz))
                   # mapa[x][y - 1] = 2
                else:
                    if o[pozycja[0]].f > f_poz:
                        o[pozycja[0]].f = f_poz
                        o[pozycja[0]].r_poz = [x, y]

            if (y >= 0) and (x + 1 >= 0) and (y < len(mapa[0])) and (x + 1 < len(mapa)) and (mapa[x + 1][y] == 0):
                g_poz = g_fun(z)
                f_poz = g_poz + ((x + 1 - cel[0]) ** 2 + (y - cel[1]) ** 2) ** 0.5
                pozycja = [0]
                if przeszukanie(o, x + 1, y, pozycja):
                    o.append(punkt(x + 1, y, x, y, g_poz, f_poz))
                   # mapa[x + 1][y] = 2
                else:
                    if o[pozycja[0]].f > f_poz:
                        o[pozycja[0]].f = f_poz
                        o[pozycja[0]].r_poz = [x, y]

            if (y + 1 >= 0) and (x >= 0) and (y + 1 < len(mapa[0])) and (x < len(mapa)) and (mapa[x][y + 1] == 0):
                g_poz = g_fun(z)
                f_poz = g_poz + ((x - cel[0]) ** 2 + (y + 1 - cel[1]) ** 2) ** 0.5
                pozycja = [0]
                if przeszukanie(o, x, y + 1, pozycja):
                    o.append(punkt(x, y + 1, x, y, g_poz, f_poz))
                    #mapa[x][y + 1] = 2
                else:
                    if o[pozycja[0]].f > f_poz:
                        o[pozycja[0]].f = f_poz
                        o[pozycja[0]].r_poz = [x, y]
        else:
            o = []
        if len(o) <= 0:
            break;
    return z


route=a_gwiadazda("grid.txt")
show_route(route)

