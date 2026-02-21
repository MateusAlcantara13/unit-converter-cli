# 🔄 unit-converter-cli

> Conversor de unidades interativo para terminal, desenvolvido em Python.

---

## 📋 Sobre o projeto

O **unit-converter-cli** é uma aplicação de linha de comando que permite converter valores entre diferentes unidades de medida de forma simples e intuitiva. O projeto foi desenvolvido com foco em boas práticas de organização de código, como separação de responsabilidades e uso de estruturas de dados para evitar repetição.

---

## ⚙️ Funcionalidades

- 🌡️ **Temperatura**
  - Fahrenheit → Celsius
  - Celsius → Fahrenheit

- 📏 **Distância**
  - Quilômetros → Milhas
  - Milhas → Quilômetros

- ⚖️ **Peso**
  - Quilogramas → Libras
  - Libras → Quilogramas

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.x instalado — [Download aqui](https://www.python.org/downloads/)

### Rodando o projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/unit-converter-cli.git

# Acesse a pasta
cd unit-converter-cli

# Execute o programa
python conversor.py
```

---

## 🖥️ Exemplo de uso

```
╔══════════════════════════════════════════════════════════╗
║                      CONVERSOR                           ║
╠══════════════════════════════════════════════════════════╣
║  🌡  Temperatura                                          ║
║      → Celsius para Fahrenheit                           ║
║      → Fahrenheit para Celsius                           ║
╠══════════════════════════════════════════════════════════╣
║  📏  Distância                                           ║
║      → Km para Milhas                                    ║
║      → Milhas para Km                                    ║
╠══════════════════════════════════════════════════════════╣
║  ⚖   Peso                                                ║
║      → Kg para Libras                                    ║
║      → Libras para Kg                                    ║
╚══════════════════════════════════════════════════════════╝

Escolha a unidade que deseja trabalhar ex (Temperatura): temperatura
1: Fahrenheit para Celsius
2: Celsius para Fahrenheit
→ 2
Insira a temperatura em graus celsius, ex (32): 100
A conversão de 100.0 °C para Fahrenheit é 212.00°F
```

---

## 🗂️ Estrutura do projeto

```
unit-converter-cli/
│
├── main.py   # Código principal da aplicação
└── README.md      # Documentação do projeto
```

---

## 🧠 O que aprendi com esse projeto

- Organização de funções por responsabilidade
- Uso de dicionários para mapear lógica e evitar repetição de código
- Tratamento e formatação de entradas do usuário
- Normalização de strings com a biblioteca `unicodedata`

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

---

## 👤 Autor

Feito por **Mateus Alcantara** — sinta-se à vontade para entrar em contato!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mateus--Alcantara-blue?logo=linkedin)](https://www.linkedin.com/in/mateusalcantara13/)
[![GitHub](https://img.shields.io/badge/GitHub-MateusAlcantara13-black?logo=github)](https://github.com/MateusAlcantara13/)
