def pesquisa(codigo):
    if codigo in tracking_codes:
        print(f'O código {codigo} esta na lista!!!')
    else:
        print('O código Não está na lista')

tracking_codes = ["JN426598162BR", "JN426598255BR","JN426598247BR","JN426598145BR","JN426598057BR","JN426598074BR","JN426598233BR","JN426598220BR","JN426598278BR","JN426598281BR","JN426598043BR","JN426598030B"]
print(f"Existe o código de rastreio {'JN426598255BR'}?")

codigo = 'JN426598255BR'

pesquisa(codigo)







