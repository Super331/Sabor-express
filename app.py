import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]




def exibir_nome_do_programa():
   print('Sabor Express\n')

def exibir_opcoes():
   print('1. Cadastrar restaurante');
   print('2. Listar restaurante');
   print('3. Ativar restaurante');
   print('4. Sair\n');

def finaliza_app():
  exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
   print('Opção inválida \n')
   voltar_ao_menu_principal()

def  exibir_subtitulo(texto):
   os.system('cls')
   print(texto)
   print()
   
def cadastrar_novo_restaurante(): 
   exibir_subtitulo('Cadastro de novos restaurantes')
   nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
   restaurantes.append(nome_do_restaurante)
   print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso \n')
   voltar_ao_menu_principal()

def listar_restaurantes(): 
   exibir_subtitulo('Listando restaurantes')
   for restaurante in restaurantes:
             nome_restaurante = restaurante['nome']
             categoria = restaurante['categoria']
             ativo = restaurante['ativo']
             print(f' - {nome_restaurante} | {categoria} | {ativo}')
   voltar_ao_menu_principal()    

   
   


def escolher_opcao():
   try: 
      opção_escolhida =int(input('Escolha uma opção: '));
      if opção_escolhida == 1 :
         cadastrar_novo_restaurante()
         print('Cadastrar restaurante')
      elif opção_escolhida == 2: 
        listar_restaurantes()
      elif opção_escolhida == 3: 
         print('Ativar restaurante')
      elif opção_escolhida == 4:
         finaliza_app()
      else:
         opcao_invalida()
   except:
      opcao_invalida()

def main():
   os.system('cls')
   exibir_nome_do_programa() 
   exibir_opcoes()
   escolher_opcao();

if __name__ =='__main__':
    main()



