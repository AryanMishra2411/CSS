graph = {
    'A':['B','C','D'],
    'B':['E','F'],
    'C':['G','H'],
    'D':['I','J'],
    'E':['K','L'],
    'F':['L','M'],
    'G':['N'],
    'H':['O','P'],
    'I':['P','Q'],
    'J':['R'],
    'K':['S'],
    'L':['T'],
    'T':['F'],
    'S':[],
    'T':[],
    'M':[],
    'N':[],
    'O':[],
    'U':[],
    'Q':[],
    'R':[]
    
}
    
start = 'A'
goal = input('Enter the goal node = ')
maxD = int(input("Enter the maximum depth limit = "))


i = 0
while(i<=maxD):
    path = list()
    def DLS(start,goal,path,level,maxD):

        if start not in path:
            

         path.append(start)
        if start == goal:

            return path

        if level==maxD:
            return False

        for child in graph[start]:
            if DLS(child,goal,path,level+1,maxD):
                return path

        return False
    res = DLS(start,goal,path,0,i)
    print('level -->',i)
    if(res):
        print("Path to goal node available")
        print("Path",path)

        path.clear()
        exit()

    else:

        print(path)
        print("No path available for the goal node in level", i)
        print("\n")
    i= i+1
