from main import removerCaracteresEspeciais, formatacaoTotalDeTexto,contarFrequenciaDePalavras,tokenizarTexto

texto = '''Se eu tiver um texto com e-mail tipo esteehumemail@gmail.com ou noreply@hotmail.com ou até mesmo emaildeteste@yahoo.com.br.
Além disso terei também vários telefones do tipo +55 48 911223344 ou 4890011-2233 e por que não um fixo do tipo 48 0011-2233?
Pode-se ter também datas como 12/12/2024 ou 2023-06-12 em variados tipos tipo 1/2/24
E se o texto tiver muito dinheiro envolvido? Falamos de R$ 200.000,00 ou R$200,00 ou até com 
a formatação errada tipo R$   2500!
Além disso podemos simplesmente padronizar números como 123123 ou 24 ou 129381233 ou até mesmo 1.200.234!'''

texto_formatado = formatacaoTotalDeTexto(texto=texto,                                        
                                         padronizar_com_unidecode=True,
                                         padronizar_datas=True,
                                         padrao_data='_data_',
                                         padronizar_dinheiros=True,
                                         padrao_dinheiro='$',
                                         padronizar_emails=True,
                                         padrao_email='_email_',
                                         padronizar_telefone_celular=True,
                                         padrao_tel='_tel_',
                                         padronizar_numeros=True,
                                         padrao_numero='0',
                                         padronizar_texto_para_minuscula=True)

print(texto_formatado)