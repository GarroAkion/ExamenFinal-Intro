
#Pregunta 1
class Dibujar ():
    def __init__(self):
        self.fila=["_"]*n
        self.tablero=[self.fila]*m

    def dibujarTriangulo(self,n,m):
        if isinstance (n,int) and(m,int):
            self.dibujarTriangulo_aux(n,m)
        else:
            return"No esta ingresando numeros enteros"
        
    def dibujarTriangulo_aux(self,n,m):
        indice=0
        indice2=-(n//2)
        top=n//2
        for i in range(top):
            if m%2 == 1:
                self.tablero[indice][m//2]=["*"]
                indice+=1

            elif self.tablero[indice][indice] or self.tablero[indice][indice2]:
                self.tablero[indice][indice]=["*"]
                self.tablero[indice][indice2]=["*"]
                indice+=1
                indice2+=1
            else:
                self.tablero[indice][indice]=["*"]or
                self.tablero[indice][indice2]=["*"]
                indice+=1
                indice+=1
        print(self.tablero)
            
            

#Pregunta 3

class criba():
    def __init__(self):
        pass
    def criba(self,lista):
        if isinstance(lista,list):
            self.criba_aux(lista)
        else:
            return"Error"

    def criba_aux(self,lista):
        indice,indice2= (0,0)
        tamaño=len(lista)
        nueva=[]
        for i in range(tamaño):
            if primo(indice)==True:
                lista[indice]=[1]
                indice+=1
            else:
                lista[indice]=[0]
                indice+=1
        print(lista)
        if lista[indice2]==[1]:
            nueva=[[indice2]]
            indice2+=1
        else:
            nueva=[]
            



#Pregunta 4
class AdmisionRegistro():
    def __init__(self):
        pass

    def admision(self):
        while agregar==True
        estu=Estudiante()
        admitidos.append(estu)
        agregar=input("Desea agregar otro")

    def prioridad(self,admision):
        self.promedioadmision=promedio
        while cola is.empty!=True:
            estu=cola.dequeue()
            nombre=estu.getnombre()
            if nombre(promedio)>nombre2(promedio):
                matri[]=[nombre]
                del miLista[nombre]
            else:
                matri[]=[nombre2]
                del miLista[nombre2]

    def matricula(self):
        while matri is.empty!=True:
            estudiante=matri.dequeue()
            nombre=estudiante.getnombre()
            matri={}
            matri[nombre]=listaCursosMatriculados
        print(ListaCursosMatriculados)
