import string

string_com_caracteres_especiais_padrao = string.punctuation

caracteres_normais = string.printable + 'áàâãéèêíìîóòôõúùûç' + 'áàâãéèêíìîóòôõúùûç'.upper()

lista_com_palavras_de_escape_padrao_frequencia = ['a','à','as','às','ao','aos','da','das','na','nas','numa','numas',
                                       'o','os','ou','do','dos','no','nos',
                                       'de','e','é','ser','será','serão','são','está','estão','foi','em','num','nuns',
                                       'são','sem','mais','menos',
                                       'um','uma','uns','umas',
                                       'sua','suas','seu','seus',
                                       'nosso','nossos','nossa','nossas',
                                       'esse','esses','essa','essas',
                                       'só','tão','tem','tens','nem','isso','tá','ta','eu','isto','mas',
                                       'sempre','nunca',
                                       'pelo','também','já','você','vocês','vc','vcs',
                                       'ele','eles','ela','elas','nele','neles','nela','nelas',
                                       'se','te','que','por','pro','pros','pra','pras','para','com','como','sobre','sim','não']

lista_com_palavras_de_escape_padrao_tokenizacao = ['a','à','as','às','ao','aos','da','das','na','nas','numa','numas',
                                       'o','os','ou','do','dos','no','nos',
                                       'de','e','em','num','nuns','ser','será','seres',
                                       'se','te','que','por','com','sobre']

lista_de_pontos_finais_nas_frases_padrao = ['.','!','?',';',':']

digito_dia = r'(0?[1-9]|1[0-9]|2[0-9]|3[0-1])'
digito_mes = r'(0?[1-9]|1[0-2])'
digito_ano = r'\d{2,4}'
padrao_regex_data = r'\b{dia}\/{mes}\/{ano}\b|\b{ano}\/{mes}\/{dia}\b|\b{dia}\-{mes}\-{ano}\b|\b{ano}\-{mes}\-{dia}\b'.format(dia=digito_dia,mes=digito_mes,ano=digito_ano)

padrao_regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

ddd_pais = r'(\+(\s+)?)?\d{2,3}'
ddd_estado = r'(\((\s+)?)?\d{2}((\s+)?\))?'
ddd_celular = r'\d{4,5}([-\s])?\d{4}'
padrao_regex_telefone_celular = r'({pais})?({estado})({celular})|({pais}(\s+)?)?({estado}(\s+)?)({celular})'.format(pais=ddd_pais,estado=ddd_estado,celular=ddd_celular)

padrao_regex_links = r'https?://\S+'

padrao_regex_numeros = r'(\b)?\d+(\S+)?(,\d+)?(\b)?|(\b)?\d+(\S+)?(.\d+)?(\b)?'

padrao_regex_dinheiro = r'R\$(\s+)?\d+(\S+)?(,\d{2})?|\$(\s+)?\d+(\S+)?(\.\d{2})?'