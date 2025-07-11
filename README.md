# 🚨 Sistema de Entrega Emergencial com Drones

Este projeto simula um sistema de pedidos e entregas de **kits de emergência** (médicos e alimentícios) usando **drones autônomos**, com foco em eficiência e suporte a múltiplos pedidos simultâneos. O sistema calcula o limite de kits por pessoa, o peso total, a quantidade de drones necessários e o tempo estimado de entrega. A iniciativa do projeto foi tomada devido à um projeto da faculdade onde teríamos que criar um sistema para ajudar pessoas em situações de emergência após desastres naturais.

## 📌 Objetivo

Criar uma solução tecnológica para ajudar comunidades em situações de emergência, como desastres naturais, pandemias ou zonas de risco, automatizando o processo de solicitação e entrega de suprimentos essenciais.

---

## 🧠 Funcionalidades

- Cadastro de pedidos com múltiplos kits e quantidades.
- Tipos de kits disponíveis:
- 🏥 Kit Médico
- 🍞 Kit Alimentício
- Cálculo do peso total da carga.
- Definição do número necessário de drones para a entrega.
- Estimativa de tempo total da missão.
- Limite de até **3 kits por pessoa** por pedido.
- Interface por linha de comando (CLI).

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- Programação Orientada a Objetos (POO)
- Estruturas condicionais e de repetição
- Funções e métodos

---

## 📦 Estrutura do Projeto

sistema_emergencial/
├── calculos/
│ ├── calcular_drones.py # Lógica para cálculo de drones necessários
│ ├── calcular_tempo.py # Estimativa de tempo de entrega
│ ├── distancia.py # Cálculo da distância
│ └── quantidade_pessoas.py # Limite de kits por pessoa
│
├── estoque/
│ └── estoque.py # Gerenciamento do estoque dos kits
│
├── exibicao_dados_pedido/
│ └── exibicao_pedido.py # Exibição dos pedidos feitos
│
├── kits_emergenciais/
│ └── kits.py # Tipos de kits: médicos e alimentícios
│
├── main.py # Menu principal do sistema
└── README.md # Este arquivo

## 💡 Funcionalidades

- Cadastro de pedidos com múltiplos kits
- Tipos de kits: médicos 🏥 e alimentícios 🍞
- Cálculo da quantidade de drones necessários
- Estimativa de tempo com base na distância
- Controle de estoque e limite de kits por pessoa
- Exibição dos pedidos feitos

---

## 🚀 Como Executar o Projeto

- Clone o repositório
- Abra o GitBash
- git clone https://github.com/Nicolas-Jacob/sistema-emergencial-py
- cd sistema_emergencial
- Certifique-se de estar com o Python 3.11+ instalado: python --version
- Execute o sistema pelo terminal: python main.py

---

📈 Possíveis Melhorias Futuras:

Interface gráfica com Tkinter
Armazenamento dos dados em .json ou banco de dados
Geração de relatórios (PDF ou Excel)
Animação da rota do drone em tempo real
Modo de simulação visual com mapa

---
