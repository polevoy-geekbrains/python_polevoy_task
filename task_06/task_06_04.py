import os

os.system('cls' if os.name=='nt' else 'clear')

domain_list = \
['https://habrahabr.ru/blogs/search_engines/123671/', 
'https://www.avito.ru/profile/messenger/channel/u2i-wfpvp7KkQK~df_x_Rv3p1w',              
'https://yandex.ru/video/preview/5060008104288795387',
'https://marketplace.loginom.ru/?_ga=2.220110494.683433624.1671138691-590799211.1668850187',
'https://www.googletagmanager.com/gtag/js?id=UA-726094-1',           
'https://assets.habr.com/habr-web/js/chunk-vendors.2f41be27.js',
'https://programforyou.ru/block-diagram-redactor']

domain_names = list(map(lambda i: i[ : i.find('/')], [i for i in map(lambda i: i.replace('https://', ''), domain_list)] ))
print('Список доменных имен:\n')
print("\n".join(domain_names))

# Насколько я понял в модуле urllib.parse есть специальная функция urlsplit() которая делит любой URL на  
# список кортежей из которого можно выдернуть домен, но не понял можно ли ее использовать в домашней работе