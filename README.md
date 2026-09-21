# TaskTracker

Aplicação de linha de comando (CLI) para gerenciamento de tarefas, desenvolvida como
projeto cumulativo do Bootcamp II.

## 📋 Descrição

O TaskTracker permite cadastrar tarefas com título, descrição, prioridade e data
limite, visualizar todas as tarefas organizadas por prioridade e acompanhar quantas
estão pendentes ou concluídas — tudo direto pelo terminal.

Este projeto é a evolução do planejamento lógico desenvolvido na **Fase 1** do
Bootcamp II (veja `docs/planejamento_logico.pdf`), agora implementado em código
Python funcional.

## 🚀 Funcionalidades

- ✅ Cadastrar nova tarefa (título obrigatório, descrição, prioridade e data limite)
- ✅ Validação estrita de prioridade (aceita apenas Alta, Média ou Baixa)
- ✅ Validação de título (não aceita campos vazios)
- ✅ Visualizar tarefas cadastradas, ordenadas por prioridade
- ✅ Contagem de tarefas pendentes e concluídas

## 🛠️ Tecnologias utilizadas

- **Python 3** (sem dependências externas)

## 📁 Estrutura do projeto

```
tasktracker-projeto/
├── README.md                     # Este arquivo
├── .gitignore                    # Arquivos ignorados pelo Git
├── docs/
│   └── planejamento_logico.pdf   # Planejamento lógico da Fase 1
└── src/
    └── main.py                   # Código-fonte da aplicação
```

## ▶️ Como executar

1. Certifique-se de ter o **Python 3** instalado:
   ```bash
   python3 --version
   ```
2. Clone este repositório:
   ```bash
   git clone https://github.com/[seu-usuario]/tasktracker-projeto.git
   cd tasktracker-projeto
   ```
3. Execute a aplicação:
   ```bash
   python3 src/main.py
   ```
4. Use o menu exibido no terminal para cadastrar e visualizar tarefas.

## 🗺️ Próximas etapas

- **Fase 3:** Empacotamento da aplicação, containerização com Docker, testes e deploy.

## 👤 Autor

[Seu Nome Completo] — Bootcamp II — [Polo/Turma]
