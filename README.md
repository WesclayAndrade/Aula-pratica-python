# 🐍 Repositório de Aulas Práticas e Projetos em Python

Este repositório centraliza os sistemas, projetos e exercícios desenvolvidos durante a minha trajetória de aprendizado em Python, cobrindo desde a lógica de programação em terminal até o desenvolvimento de aplicações web completas com persistência de dados.

---

## 📂 Projetos Inclusos

Atualmente, esta pasta contém os seguintes projetos desenvolvidos do zero:

### 1. 👕 Sistema Web "Hora do Pijama" (Gestão de Estoque e Vendas)
Uma aplicação web completa desenvolvida para automatizar o controle de estoque e o fluxo de vendas de uma loja de pijamas.
- **Como funciona:** O sistema possui uma interface web onde é possível cadastrar novos produtos com validação de duplicados, registrar vendas abatendo o estoque em tempo real e adicionar novos lotes de mercadoria.
- **Tecnologias:** Python, Flask (Back-end), Jinja2 (Templates HTML dinâmicos), CSS3 para estilização, e Pandas integrado com o Excel para persistência de dados de forma segura em planilhas automatizadas.

### 🥑 2. Calculadora de Proteína Diária (Utilitário de Nutrição)
Um software interativo executado via linha de comando (CLI) voltado para o monitoramento nutricional e cálculo de macronutrientes.
- **Como funciona:** O usuário realiza um cadastro inicial e pode gerenciar sua alimentação diária informando o peso dos alimentos consumidos. O script calcula a porção exata de proteína ingerida baseando-se na densidade nutricional por 100g e gera um resumo total do dia com alertas visuais.
- **Tecnologias:** Python 3, manipulação avançada de Estruturas de Dados (listas e dicionários aninhados) e loops de repetição para menus interativos.

  
### 📈 3. Gerenciador de Ativos Financeiros (Simulador de Home Broker)
Um sistema em linha de comando (CLI) projetado para gerenciar uma carteira de investimentos, permitindo o controle de posições em Ações e Fundos Imobiliários (FIIs).
- **Como funciona:** O usuário pode simular a compra de ativos informando o ticker, a quantidade e o preço pago. O sistema calcula o preço médio/total investido por ativo, permite buscar posições individuais de forma rápida e gera um relatório consolidado com a soma de todo o patrimônio acumulado na carteira.
- **Tecnologias:** Python 3, manipulação de strings (`.upper()` para padronização de tickers), tratamento de dados e estruturas de repetição para busca linear.
---

## 🛠️ Competências e Conceitos de ADS Aplicados

Nesses projetos, foram consolidados conceitos fundamentais de engenharia de software e desenvolvimento back-end:
- **Arquitetura Web e Rotas:** Criação e mapeamento de rotas HTTP (`GET` e `POST`) com Flask e envio de dicionários estruturados para renderização no front-end.
- **Tratamento de Erros e Exceções:** Implementação robusta de blocos `try/except` para prevenir travamentos (ex: tratamento de conversão de tipos de dados numéricos no formulário e leitura de arquivos).
- **Manipulação de Arquivos e Dados:** Uso da biblioteca Pandas e do motor `openpyxl` para ler, validar, filtrar e reescrever abas específicas de arquivos externos de dados de forma assíncrona.
- **Interface e Experiência do Usuário (UX):** Validações com JavaScript no front-end para evitar exclusões acidentais no banco e formatação de dados decimais (`:.1f` e filtros Jinja) para melhor leitura de preços e quantidades.
- ** Busca linear com Flag Booleana permite consitência do BD temporário, além da interrupção programada, necessária padronização de entradas apesar de toda comunidade saber que se utiliza caracteres maiusculos, algum equivoco pode incluir em minusculos então o `upper()` me garante uma consistência não permitindo erro no sistema. Zerar a variável `soma_patrimonio=0` e recalcular a cada nova visualizcão para evitar acumulo de memória que pode chocar com consultas anteriores.

---

## 🚀 Como Executar os Projetos

Cada projeto pode ser executado de forma independente no seu ambiente local (Mac, Windows ou Linux):

### Executando a Loja (Interface Web)
1. Certifique-se de ter as dependências instaladas na sua pasta ou ambiente virtual:
```bash
   pip install flask pandas openpyxl
