# 🎬 Sistema de Indicação de Filmes

Este projeto é uma aplicação desktop desenvolvida em **Python** que funciona como um catálogo interativo de recomendações cinematográficas. Ele utiliza uma interface gráfica para exibir sinopses, categorias detalhadas e pôsteres de filmes.

---

## 🚀 Funcionalidades

* **Navegação por Gêneros:** O sistema organiza os filmes em 12 categorias principais (Ação, Animação, Terror, etc.).
* **Subgêneros Detalhados:** Classificação específica para cada obra (ex: Aventura Épica, Comédia Romântica).
* **Interface Visual:** Exibição dinâmica de pôsteres (ex: *Parasita, Gladiador, Minha Mãe é uma Peça*).
* **Base de Dados Externa:** Carregamento de dados via arquivos `.txt` para fácil manutenção.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **GUI:** `tkinter` (Biblioteca padrão)
* **Processamento de Imagem:** `Pillow` (PIL)

---

## 📂 Estrutura de Pastas

Para o correto funcionamento, certifique-se de que os arquivos estejam organizados no mesmo diretório:

```text
/Projeto-Filmes
├── IndicacaoDeFilmes.py       # Script principal
├── sinopses.txt               # Lista de filmes e descrições
├── Filmes e gêneros.txt       # Estrutura de classificação
└── imagens/                   # Pasta com os arquivos de imagem (.jpg, .png)
```
---

## 📦 Como Rodar o Projeto

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em sua máquina. Além disso, é necessário instalar a biblioteca **Pillow**, responsável pelo processamento e exibição das imagens dos pôsteres:

```bash
pip install pillow 
```

---


### 2. Execução

Com as dependências instaladas e todos os arquivos na mesma pasta (conforme a estrutura de diretórios mencionada anteriormente), siga os passos abaixo:

1. Abra o **Terminal** ou **Prompt de Comando**.
2. Navegue até a pasta onde os arquivos foram extraídos.
3. Execute o script principal com o comando:

```bash
python IndicacaoDeFilmes.py
```

---

Se você estiver utilizando Linux ou macOS, e possuir múltiplas versões do Python instaladas, utilize:

```bash
python3 IndicacaoDeFilmes.py 
```

---

## 🎨 Interface e Categorias

O sistema organiza o catálogo em 12 gêneros principais, permitindo uma navegação fluida entre as seguintes categorias:

* **Ação, Animação e Aventura**
* **Comédia, Documentário e Drama**
* **Fantasia, Ficção e Musical**
* **Romance, Terror, Suspense e Trash**

---

## 🛠️ Detalhes Técnicos

* **Persistência:** Os dados são lidos em tempo real dos arquivos `.txt`, permitindo que novos filmes sejam adicionados sem a necessidade de alterar o código-fonte.
* **Interface Gráfica:** Utiliza o gerenciador de exibição do `tkinter` para garantir que as sinopses e imagens sejam apresentadas de forma clara e organizada.

---

## 👨‍💻 Autor

**Rodrigo Corrêa de Sá Farah**
*Estudante de Ciência da Computação – Universidade Veiga de Almeida (UVA)*

---

## 📜 Licença

Este projeto foi desenvolvido para fins acadêmicos e de estudo de interface gráfica com Python. Sinta-se à vontade para clonar, explorar e sugerir melhorias!
