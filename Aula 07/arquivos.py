arquivo = open(r"C:\Users\adria\Videos\Citha-Python\Aula 07\contatos.txt", 'a')
arquivo.write('JOSE \n')
arquivo.close()

arquivo = open(r"C:\Users\adria\Videos\Citha-Python\Aula 07\contatos.txt", 'r')
for linha in arquivo:
    print(linha)
arquivo.close()
