
from pacienteclass import paciente
class DaoPaciente:
    def inserir(self,p):
        dir = '/home/lorrana/Desktop/trabalhoPython/banco.txt'
        arquivo = open(dir,'a+')
        arquivo.close()
        f = open(dir,'r+')
        vet=[]
        vetor=[]
        for line in f:
            line = line.split(",")
            vetor.append(line)
            vet.append(line[4])
        i=0
        cod=0
        print(vet)
        while (i!=3):
            strcod = "{}".format(cod)
            try:
                if(vet.index(strcod)>=0):
                    cod+=1

            except: 
                i=3
                break
        p._set_cod(cod)
        string = "{},{},{},{},{}".format(p.nome,p.exame,p.data,p.hora,p.cod)
        f.write(string+',\n')
        f.close()

    def excluir(self,cod):
        vetor=[]
        vet = []
        arquivo = open('/home/lorrana/Desktop/trabalhoPython/banco.txt','r')
        for line in arquivo:
            line = line.split(",")
            vetor.append(line)
            vet.append(line[4])
        i=0
        print(vet)
        while (i<len(vetor)):
            strcod = "{}".format(cod)
            try:
                if(vet.index(strcod)>=0):
                    vetor.pop(vet.index(strcod))
                    print("Existe no vetor ")
                    break
            except:
                    print("Não existe no vetor")
            i+=1
        arquivo.close()
        f = open('/home/lorrana/Desktop/trabalhoPython/banco.txt', "w")
        i=0
        while (i<len(vetor)):
            string = ",".join(vetor[i])
            f.write(string)
            print(string)
            i+=1
        f.close()

    def alterar(self,p):
        vetor=[]
        vet=[]
        arquivo = open('/home/lorrana/Desktop/trabalhoPython/banco.txt','r+')
        for line in arquivo:
            line = line.split(",")
            vetor.append(line)
            vet.append(line[4])
        i=0
        print(p._get_cod())
        while (i<len(vetor)):
            strcod = "{}".format(p._get_cod())
            try:
                if(vet.index(strcod)>=0):
                    pos = vet.index(strcod)
                    vetor.pop(pos)
                    string = "{},{},{},{},{},\n".format(p.nome,p.exame,p.data,p.hora,p.cod)
                    vet = string.split(",")
                    vetor.append(vet)
                    print("Existe no vetor ")
                    break
            except:
                    print("Não existe no vetor")
            i+=1
        arquivo.close()
        f = open('/home/lorrana/Desktop/trabalhoPython/banco.txt', "w")
        i=0
        while (i<len(vetor)):
            string = ",".join(vetor[i])
            f.write(string)
            print(string)
            i+=1
        f.close()

    def buscar(self,cod):
        vetor=[]
        vet=[]
        arquivo = open('/home/lorrana/Desktop/trabalhoPython/banco.txt','r')
        for line in arquivo:
            line = line.split(",")
            vetor.append(line)
            vet.append(line[4])
        print(vet)
        aux=0
        while (aux!=3):
            strcod = "{}".format(cod)
            try:
                if(vet.index(strcod) >=0):
                    i = int(vet.index(strcod))
                    print("Nome: "+vetor[i][0]+" Exame: "+vetor[i][1]+" Data: "+vetor[i][2]+" Hora:"+vetor[i][3]+" Código: "+vetor[i][4])
                    aux=3
                    break
            except:  
                    print("Não existe no vetor")
                
        arquivo.close()
    def listar(self):
        vetor=[]
        vet=[]
        arquivo = open('/home/lorrana/Desktop/trabalhoPython/banco.txt','r')
        for line in arquivo:
            line = line.split(",")
            vetor.append(line)
        i=0
        while (i<len(vetor)):
            print("Nome: "+vetor[i][0]+" Exame: "+vetor[i][1]+" Data: "+vetor[i][2]+" Hora:"+vetor[i][3]+" Código: "+vetor[i][4])
            i+=1

        arquivo.close()



            
if __name__ == "__main__":
    d = DaoPaciente()
    p = paciente('you','consulta','10/10/2019','12:10')
    d.listar()

