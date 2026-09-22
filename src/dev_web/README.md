# 🧮 Calculadora Web com Flask

Uma aplicação web interativa de calculadora desenvolvida em Python com o microframework **Flask**, criada para demonstrar a evolução de um script em linha de comando (CLI) para uma interface web moderna e responsiva.

---

## 📌 Sobre o Projeto

O objetivo deste projeto foi refatorar um código em lote/console para a arquitetura Web stateless do Flask. A aplicação processa operações matemáticas básicas, permite a execução simultânea de todas as operações e mantém um histórico de consultas persistido na sessão do navegador de cada usuário.

### ✨ Funcionalidades
- **Operações Básicas:** Soma, Subtração, Multiplicação e Divisão (com tratamento de erro para divisão por zero).
- **Execução em Lote:** Botão para calcular todas as quatro operações de uma só vez.
- **Histórico por Sessão:** Cada usuário possui um histórico único de operações salvo na `session` do Flask.
- **Interface Moderna:** Design responsivo com estética *Glassmorphism* usando CSS3 puro e ícones da FontAwesome.
- **Segurança:** Configuração de chave secreta protegida via variáveis de ambiente com `python-dotenv`.

---

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python 3, Flask, Jinja2, `python-dotenv`
- **Front-end:** HTML5, CSS3, FontAwesome Icons
- **Versionamento:** Git & GitHub

---


Desenvolvido com 💜 por [Ezequiel Amorim](https://github.com/quel-amorim).
