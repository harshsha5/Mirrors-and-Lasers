import ast
import copy
import sys
def make_grid(r,c,m,n):
    """
    :Input: max number of row, max number of column, Placement of / mirrors, Placement of \ mirrors
    :Return: 2D List representing the grid from user input
    """
    grid=[[0 for c in range(C)] for r in range(R)]
    for elt in M:
        grid[elt[0]-1][elt[1]-1]=1                      #1 indicates/
    for elto in N:
        if(elto not in M):                                              #ensures only 1 mirror per cell. Avoids error on part of user to put two mirrors in the same cell. / Is taken by default 
            grid[elto[0]-1][elto[1]-1]=2                #2 indicates\
    return grid

def validate_mirror(r,c,grid):
    """
    :Input: max number of row, max number of column, The grid
    :Return: If the safe is sceure or not (ie. The final output required)
    """
    status=current(r,c,grid)
    if(status[0]==0):
        print("0")                                              #Opens without mirror insertion
        return 0
    else:
        #print("Doesn't open without mirror insertion")
        k,lowr,lowc=add_mirror(r,c,grid,status[1])
        if(k):
            print(k,lowr+1,lowc+1)           #Can open in "k" ways with insertion of mirror. Least possible combo is ("lowr+1,lowc+1")
        else:
            print("Impossible")

def add_mirror(r,c,grid,visit):
    """
    :Input: max number of row, max number of column, The grid
    :Return: A tuple with the number of possible mirror orientations through which safe opens via mirror insertion, the row and column of the first (lexicographically) such position
    """
    k=0
    lowr=-1
    lowc=-1
    for elt in visit:
        if(grid[elt[0]][elt[1]]==0):                                 #Here I have assumed that I can only add mirrors in the vacant cells (where there is no mirror already present)
            grid1=copy.deepcopy(grid)
            grid1[elt[0]][elt[1]]=1                                    # Adding / and testing if it clears
            found1=current(r,c,grid1)
            grid1[elt[0]][elt[1]]=2
            found2=current(r,c,grid1)
            if(found1[0]==0 or found2[0]==0):
                if(k==0):
                    lowr=elt[0]                         #Assuming (x,y) lexicographically means find the least x and then the least y
                    lowc=elt[1]
                k+=1

    return (k,lowr,lowc)

def current(r,c,grid):
    """
    :Input: max number of row, max number of column, The grid
    :Return: Returns 0 if the safe opens with the current mirror arrangement otherwise 0
    """
    positionr=0
    positionc=0
    multiplierr=0
    multiplierc=1
    visited=[]
    dirn="row+"
    while((-1<positionc<c) and (-1<positionr<r)):
        if(grid[positionr][positionc]==1):
            if(dirn=="row+"):
                dirn="col-"
                multiplierr=-1
                multiplierc=0
                positionr+=multiplierr
            elif(dirn=="row-"):
                dirn="col+"
                multiplierr=1
                multiplierc=0
                positionr+=multiplierr
            elif(dirn=="col+"):
                dirn="row-"
                multiplierc=-1
                multiplierr=0
                positionc+=multiplierc
            elif(dirn=="col-"):
                dirn="row+"
                multiplierc=1
                multiplierr=0
                positionc+=multiplierc
        elif(grid[positionr][positionc]==2):
            if(dirn=="row+"):
                dirn="col+"
                multiplierc=0
                multiplierr=1
                positionr+=multiplierr
            elif(dirn=="col+"):
                dirn="row+"
                multiplierc=1
                multiplierr=0
                positionc+=multiplierc
            elif(dirn=="row-"):
                dirn="col-"
                multiplierc=0
                multiplierr=-1
                positionr+=multiplierr
            elif(dirn=="col-"):
                dirn="row-"
                multiplierc=-1
                multiplierr=0
                positionc+=multiplierc
        else:
            if(dirn=="row+" or dirn=="row-"):
                positionc+=multiplierc
            elif(dirn=="col+" or dirn=="col-"):
                positionr+=multiplierr

        visited.append((positionr,positionc))

    if(positionr==r-1 and positionc==c):
        return [0,None]                                    #If the safe opens without the mirror insertion, we don't really need the visited array hence put None there.
    else:
        return [1,visited[:-1]]                                 #If the safe doesn't open without mirror insertion we, need to evaluate the safe further, and hence we pass the visited array


'''def get_coords():                                    #An improved method to input M and N, but since I had to stick to the format of the input given in the question, I have commented this part and coded it accordingly
    """
    :Input: -
    :Return: Coordinates inputted by the user in the form of a tuple
    """                                                  #Correct this part to accept only correct inputs
    try:
        print("Enter a list of points. For example (0,0) (0,1) (1,1) (1,0)")
        coords = [ast.literal_eval(coord) for coord in raw_input().split()]
        return coords
    except ValueError:
        print "Please enter the coordinates in the format mentioned"
        exit()
'''

def get_coords():
    n=input("Enter number of mirrors to place ")
    list1=[]
    for i in range(n):
        a=input("Enter coodinate: eg.(1,0) ")
        list1.append(a)
    return list1

#MAIN BODY

R=input("Enter number of rows in the grid ")
C=input("Enter number of columns in the grid ")
M=get_coords()                                          #Stores coordinates of / mirror
N=get_coords()                                          #Stores coordinates of \ mirror
grid=make_grid(R,C,M,N)
#print(grid)
validate_mirror(R,C,grid)

