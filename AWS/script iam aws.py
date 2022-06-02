import boto3
from botocore.exceptions import ClientError
import json
import sys
import time

iam = boto3.client('iam')

#Criando uma barra de progresso
def barra_de_progresso(seconds):

	for _ in range(seconds):
		time.sleep(1)
		print('.', end='')
		sys.stdout.flush()
	print()

#Criando usuário
def criarUsuario(iam_resource):
	try:
		username = input("Informe o nome do usuário: ")
		response = iam.create_user(UserName = username)
		response = iam.create_access_key(UserName= username)
		print(f"Usuário Criado: {username}.")
        print(response[f"AccessKey:"['AccessKey'])
	except ClientError as error:
		print(f"Usuário não pode ser criado! Erro: " f"{error.response['Error'['Message']}")
		
		raise		
	print(f"Aguarde enquanto o usuário é criado.", end='')
    barra_de_progresso(10)
 
 #Listando os usuários:   
 def listarUsuario(iam_resource):
        user = iam.get_paginator('list_users')
        for response in user.paginate():
...     print(response)
...
#Alterando usuário:
def atualizarUsuario(iam_resource):
    nome = input("Informe o nome do usuário que deseja alterar: ")
    novoNome = input("Infome o novo nome para conta: ")
    iam.update_user(UserName=nome, NewUserName=novoNome)
    
#Deletando usuário:
def deletandoUsuario(iam_resource)
    usuario = input("Informe o nome do usuário que deseja deletar: ")
    iam.delete_user(UserName=usuario) 
#Regra para atribuir politica aos usuários:

try:
        role = iam_resource.create_role(
            RoleName=f'RegraIAM',
            AssumeRolePolicyDocument=json.dumps({
                'Version': '2022-05-27',
                'Statement': [{
                    'Effect': 'Allow',
                    'Principal': {'AWS': user.arn},
                    'Action': 'sts:AssumeRole'}]}))
        print(f"Regra Criada: {role.name}.")
    except ClientError as error:
        print(f"Regra não pode ser criada! Erro:  "
              f"{error.response['Error']['Message']}")
        raise
   
#Criando politicas de acesso: 
#Politica de acesso somente leitura
policy_readOnly = {
	"Version": "2022-05-27"
	"Statement": {
			"Effect":  "Allow",
			"Action":  ["iam:Get*", "iam:List*"],
			"Resource": ["arn:aws:iam::*:user/${aws:username}"]
            role.attach_policy(PolicyArn=policy.arn)
	}
}
#Politica de acesso leitura e escrita
policy_read_write = {
	"Version": "2022-05-27"
	"Statement": {
		"Sid: "AllObjectActions",
		"Effect": "Allow",
		"Action": "iam:*Object",
		"Resource": ["arn:aws:iam::*:user/${aws:username}"]
	}
}
#Politica de acesso admin
Policy_admin_aws = {
	"Version": "2022-05-28"
	"Statement": {
		"Effect": "Allow"
		"Action": "iam:*",
		"Resource": "*"
	}
}
while == true {
	print("Selecione uma opção: ")
	print("1 - Criar usuário")
	print("2 - Pesquisar usuário")
	print("3 - Alterar usuário")
	print("4 - Deletar usuário")
	print("5 - atribuir uma politica ao usuário")
	print("6 - Sair")

