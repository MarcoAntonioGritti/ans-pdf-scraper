# Projeto de Web Scraping para Download e Compactação de PDFs

Este projeto realiza o download automático de arquivos PDF de páginas da web e os compacta em um arquivo ZIP. Ele foi desenvolvido para simplificar o processo de coleta e organização de documentos.

---

## 📂 Estrutura do Projeto

```
test_web_scraping_ans/
│
├── src/
│   ├── main.py               # Script principal para execução do processo
│   ├── utils/                # Funções auxiliares (ex.: download e compactação)
│
└── README.md             # Documentação do projeto
```

---

## 🚀 Funcionalidades

- **Download Automático**: Realiza o download de arquivos PDF de URLs específicas.
- **Organização**: Salva os PDFs em um diretório dedicado.
- **Compactação**: Gera um arquivo ZIP contendo todos os PDFs baixados.

---

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- **Python 3.13+** instalado.
- Gerenciador de pacotes `poetry`.
- Ambiente virtual configurado (recomendado).

---

### Passos para Execução

1. **Acesse o projeto**
```bash
cd test_web_scraping_ans #Ira entrar na pasta
```

2. **Crie e ative um ambiente virtual**:
   ```bash
   pip install poetry #Instalar o gerenciador caso não tenha
   poetry install #Ira instalar as depenências
   source venv/bin/activate  # Linux/Mac
   ./.venv/Scripts/activate  # Windows
   ```
   
### 3. Configure o script
Abra o arquivo `utils/config.py` e ajuste os parâmetros para definir:
- URLs das páginas que contêm os PDFs.
- Diretórios de saída para os PDFs e o arquivo ZIP.

### 4. Execute o script
```bash
poetry run python -m src.main
```

### 5. Verifique os resultados
- Os PDFs serão salvos no diretório `data/`.
- O arquivo ZIP será salvo no diretório `output/`.

---

## ⚠️ Observações

- Certifique-se de que as URLs fornecidas contêm arquivos PDF válidos.
- Respeite os **Termos de Serviço** dos sites que você está acessando.

---

## 📖 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## 📞 Contato

- **Autor**: Marco Antônio
- **Email**: marco_gritti15@hotmail.com
- **LinkedIn**: (https://www.linkedin.com/in/marco-antonio-gritti-pazza-091938232/)
