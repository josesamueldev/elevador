# 🛗 Sistema de Controle de Elevador

Sistema de simulação de elevador desenvolvido em Python, com controle de andares e verificação de capacidade de peso.

## 📋 Sobre o projeto

Este projeto simula o funcionamento básico de um elevador em um prédio de 10 andares. O sistema permite que o usuário selecione o andar de destino e informe o peso dos ocupantes, verificando se a carga está dentro do limite seguro antes de liberar o acesso.

**Funcionalidades:**
- Exibição de todos os andares disponíveis (1 ao 10)
- Seleção de andar de destino com validação de entrada
- Verificação de peso com limite de 300 kg
- Feedback visual com status de operação (✅ seguro / ⚠ limite / ❌ excedido)
- Separação de configurações em arquivo dedicado (`config.py`)

## 🚀 Como executar

**Pré-requisitos:** Python 3.8 ou superior

```bash
# Clone o repositório
git clone https://github.com/josesamueldev/elevador.git

# Acesse a pasta
cd elevador

# Execute o projeto
python main.py
```

## 🗂️ Estrutura do projeto

```
elevador/
├── main.py        # Ponto de entrada da aplicação
├── elevador.py    # Lógica principal do sistema
└── config.py      # Configurações (peso máximo, andares)
```

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

## 📌 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

- Modularização de código com múltiplos arquivos
- Tratamento de exceções com `try/except`
- Validação de entrada do usuário
- Separação de configurações da lógica de negócio

## 👨‍💻 Autor

**José Samuel Oliveira**

[![Instagram](https://img.shields.io/badge/@s.o.samuel-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/s.o.samuel)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jos%C3%A9-samuel-oliveira-745867377/)
