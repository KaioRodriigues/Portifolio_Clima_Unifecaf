# Portifolio_Clima_Unifecaf

# Captador de Clima - São Paulo

Este é um programinha simples que busca a temperatura e umidade do ar de São Paulo e salva os dados em um arquivo Excel.

# O que ele faz?

Usa o Selenium para pegar a previsão do tempo de um site.
Mostra uma interface simples com um botão para buscar os dados.
Salva as informações de temperatura, umidade e data/hora em um arquivo chamado clima.xlsx.

# O que você precisa?

Python 3
Google Chrome
ChromeDriver (compatível com a versão do seu Chrome)

# Como instalar as bibliotecas?
# No terminal ou prompt de comando, rode:

pip install selenium openpyxl

# Como rodar o programa?
# Execute o script principal:

python main.py

# Estrutura do Projeto
/
├── clima.py  # Faz a busca dos dados
├── main.py   # Interface gráfica
├── clima.xlsx  # Arquivo onde os dados são salvos
├── README.md # Este arquivo

# Melhorias Futuras

Permitir escolher outras cidades.
Melhorar a interface.,
Agendar buscas automáticas.
