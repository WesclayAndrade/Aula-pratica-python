from flask import Flask, render_template, request, redirect
import os 
import pandas as pd
from datetime import datetime


#caminho do arquivo 
ARQUIVO_ESTOQUE = '/Users/wesclayandrade/Desktop/Hora do pijama /APP Loja/Estoque_pijama.xlsx'
#garantir letras maiusculas 
if os.path.exists(ARQUIVO_ESTOQUE):
    try:
        df_inicial = pd.read.excel(ARQUIVO_ESTOQUE, sheet_name = 'Produtos', engine = 'openpyxl')
        colunas_para_ajusatr = [ 'Produto', 'Comprador']
        for coluna in colunas_para_ajusatr:
            if coluna in df_inicial.columns:
                df_inicial[coluna] = df_inicial[coluna].str.upper()
        try:
            df_venas_inicial = pd.read_excel(ARQUIVO_ESTOQUE, sheet_name = 'Vendas', engine= 'openpyxl')
        except:
            df_vendas_inicial = pd.DataFrame()

        with pd.ExcelWriter(ARQUIVO_ESTOQUE, engine='openpyxl') as writer:
            if not df_inicial.empty:
                df_inicial.to_excel(writer, sheet_name ='Produtos', index = False)
            if not df_vendas_inicial.empty:
                df_vendas_inicial.to.excel(writer, sheet_name ='Vendas', index= False)
            print('Colunas Iniciais Atualziadas com sucesso.')
    except Exception as e:
        print(f"Aviso no ajuste inicial: {e}. O arquivo pode estar vazio ou aberto.")
                     

def carregar_dados():
    if os.path.exists(ARQUIVO_ESTOQUE):
        try: 
            #buscar aba especifica 
            df = pd.read_excel(ARQUIVO_ESTOQUE, sheet_name='Produtos', engine='openpyxl')
            #evitar key erro com colunas necessárias 
            colunas_obrigatorias = [ 'Estoque Atualizado', 'Valor de Venda', 'Total de Saídas', 'Quantidade Inicial', 'Total']
            for col in colunas_obrigatorias:
                if col not in df.columns:
                    df[col] = 0
            
            df['Estoque Atualziado'] = pd.to_numeric(df['Estoque Atualziado'], errors='coerce').fillna(0).astype(int)
            df['Valor de venda'] = pd.to_numeric(df['Valor de venda'], errors='coerce').fillna(0.0)
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"Erro ao ler aba Preodutos: {e}")
            return[]      
    return []

    

def salvar_venda_e_estoque(estoque, nova_venda=None):
    vendas = [ ]
    #Tenta carregar as vendas que já existem para não apagar o histórico
    if os.path.exists(ARQUIVO_ESTOQUE):
        try: #leitura da aba vendas 
              df_vendas_antigas = pd.read_excel(ARQUIVO_ESTOQUE, sheet_name='Vendas', engine='openpyxl')
              vendas = df_vendas_antigas.to_dict(orient='records')
        except: 
            vendas = [] #se a aba Vendas não existir, comeca do zero.
    if nova_venda:
        vendas.append(nova_venda)

#Grava as duas abas no mesmo arquivo de excel.
    with pd.ExcelWriter(ARQUIVO_ESTOQUE, engine='openpyxl') as writer:
         pd.DataFrame(estoque).to_excel(writer, sheet_name='Produtos', index=False)
         pd.DataFrame(vendas).to_excel(writer, sheet_name='Vendas', index=False)
   
    

app = Flask(__name__)

app.template_folder =  os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))

@app.route('/')
def index():
    lista_estoque = carregar_dados()
   
    return render_template('index.html', estoque=lista_estoque)


@app.route('/cadastrar', methods = ['POST'])
def cadastrar():
    try:
        #recebe o que foi digitado no formulário 
        nome = request.form.get('nome', '').strip().upper()
        quantidade_str = request.form.get('quantidade', '0')
        preco_str = request.form.get('preco', '0')
        
        # Validação e conversão
        if not nome:
            return "Erro: Nome do produto é obrigatório."
        
        try:
            quantidade = int(quantidade_str)
            preco = float(preco_str.replace(',','.'))
        except ValueError as e:
            return f"Erro: Valor Inválido. {str(e)}"
        
        if quantidade < 0 or preco < 0:
            return "Erro: Quantidade e Preço não podem ser negativos."
        
        #carregar a lista atual 
        lista_estoque = carregar_dados()
#verificar a existência do produto em estoque.
        for p in lista_estoque:
            if p['Produto'].upper() == nome:
                return "Erro: Este produto já está cadastrado no esqtoque."

        #adicionar dicionário 
        lista_estoque.append({
                            "Produto": nome, 
                            "Código pijama":  len(lista_estoque) + 1,
                            "Quantidade Inicial": quantidade, 
                            "Total Saídas": 0,
                            "Estoque Atualizado": quantidade,
                            "Total": 0,
                            "Valor de venda": preco})
        salvar_venda_e_estoque(lista_estoque)

        #volta para a página inciial 
        return redirect('/')
    except Exception as e:
        return f"Erro ao cadastrar: {str(e)}"
    
from datetime import datetime


@app.route('/vender', methods=["POST"])
def vender():
    try:
    
        lista_estoque = carregar_dados()
        nome_venda = request.form.get('nome_venda', '').strip()
        qtd_vendida = int(request.form.get('quantidade_vendida', '0'))
        comprador = request.form.get('comprador', '').strip().upper()

        if not comprador: 
            return "Erro: Nome do comprador é obrigatório."
        if qtd_vendida <= 0:
            return "Erro: A quantidade vendiada deve ser maior que zero."
        
        for produto in lista_estoque:
             if produto['Produto'].lower() == nome_venda.lower():
                if produto["Estoque Atualizado"] >= qtd_vendida:
                    produto['Estoque Atualizado'] -= qtd_vendida
                    produto['Total Saídas'] += qtd_vendida
                    produto['Total'] = produto['Total Saídas'] * produto['Valor de venda']

                    nova_venda = {
                                "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                                "Comprador": comprador,
                                "Produto": produto['Produto'],
                                "Quantidade": qtd_vendida,
                                "Valor Unitário": produto['Valor de venda'],
                                "Total": qtd_vendida * produto['Valor de venda']
                              }

                    salvar_venda_e_estoque(lista_estoque, nova_venda)
                    return redirect('/')
                else:
                    return f"Erro: Estoque insuficiente. Estoque atual: {produto['Estoque Atualizado']}"
        return "Erro: Produto não encontrado."
    except Exception as e:
        return f"Erro ao vender: {str(e)}"

@app.route('/excluir', methods=['POST'])
def excluir():
    try:
        #pega o nome do produto escondido no botão
        nome_excluir = request.form.get('nome_excluir')
        if not nome_excluir:
            return "Erro: Nome do produto não fornecido para exclusão."
        
        lista_estoque = carregar_dados()
        #list comprehension - cria um novo estoque mantendo apenas produtos que não tem nome a ser excluido
        estoque_atualizado = [produto for produto in lista_estoque if produto['Produto'] != nome_excluir]

        #salva o novo estoque no excel- vendas antigas continuam salvas 
        salvar_venda_e_estoque(estoque_atualizado)
        return redirect('/')
    except Exception as e:
        return f"Erro ao excluir: {str(e)}"

@app.route('/entrada', methods=['POST'])
def entrada():
        try:
            nome_entrada = request.form.get('nome_entrada', '').strip()
            qtd_entrada = int(request.form.get('quantidade_entrada', '0'))

            if qtd_entrada <= 0:
                return "Erro: A quantidade de entrdada deve ser maior que zero."
            
            lista_estoque = carregar_dados()
            produto_encontrado = False
        
            for produto in lista_estoque:
                if produto['Produto'].lower() == nome_entrada.lower():
                    #soma nova quantidade estoque atualziado
                    produto['Estoque Atualizado'] += qtd_entrada
                    #atualização de quantidade inicial 
                    produto['Quantidade Inicial'] += qtd_entrada
                    produto_encontrado = True
                    break

            if not produto_encontrado:
                return "Erro: Produto não encontrado para atualziação"
            
            salvar_venda_e_estoque(lista_estoque)
            return redirect('/')
        except Exception as e:
            return f"Erro ao atualizar estoque: {str(e)}"
            

if __name__ == '__main__':
    app.run(debug=True, port=5005)

    
