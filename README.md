
# 📄 changelog-report

**changelog-report** é uma ferramenta leve e automatizada para gerar relatórios de alterações de código a partir dos arquivos *staged* do Git, com suporte a resumo automático por IA local (T5/flan-t5-small) e interface gráfica opcional.

Ideal para equipes, projetos open source ou uso individual, o changelog-report facilita a documentação de mudanças, criação de mensagens de commit e auditoria de código — tudo sem depender de internet ou serviços externos.

**Destaques:**
- Geração de changelog detalhado e resumo de commit prontos para uso
- IA local para sumarização automática das alterações (sem custo, sem nuvem)
- Interface gráfica (Tkinter) e scripts de execução rápida para todos os sistemas
- Totalmente offline, seguro e fácil de integrar a qualquer fluxo Git

---

## ✨ Visão Geral

O `changelog-report` analisa os arquivos adicionados ao staging (`git add .`) e gera:

- 💘 Um **relatório completo (`logs/changelog.txt`)** com diffs e arquivos binários listados
- 🧾 Um **resumo (`logs/commit_details.txt`)** pronto para ser usado como mensagem de commit

Também conta com uma **interface gráfica (GUI)** opcional, ativada via `--gui`, ideal para uso mais visual.

---

## 🚀 Como Usar


### 🔧 Execução rápida (recomendado)

No Windows:
```bat
run-changelog.bat
```
No Linux/macOS:
```sh
./run-changelog.sh
```
Esses scripts ativam o ambiente virtual automaticamente e executam o relatório sem comandos manuais.

### Modo CLI tradicional

```bash
git add .
python .
```
Gera os relatórios na pasta `logs/`.

### 🖼 Modo GUI (opcional)

```bash
python . --gui
```
A GUI inclui:
- Botão "Gerar relatório"
- Exibição do resumo do commit
- Acesso rápido à pasta de logs

---

## 📁 Estrutura de Arquivos

```
changelog-report/
├── changelog_report.py      # Lógica principal
├── gui.py                   # Interface gráfica opcional
├── __main__.py              # Entrypoint CLI/GUI
├── logs/
│   ├── changelog.txt        # Relatório detalhado
│   └── commit_details.txt   # Resumo para commit
└── README.md
```

---


## 💠 Funcionalidades

✅ Detecta arquivos modificados com `git diff --cached`
✅ Mostra diffs apenas de arquivos de texto legíveis
✅ Identifica arquivos binários e apenas os lista
✅ Ignora arquivos do `.gitignore`
✅ Interface gráfica opcional com Tkinter (leve e nativa)
✅ **Resumo automático com IA (T5/flan-t5-small local, sem internet)**
✅ Scripts de execução rápida para Windows e Linux/macOS

---

## 🔎 Exemplo de commit_details.txt

```
Resumo do commit:
- Modificações em `src/utils.py`
- Alteração em `image/logo.png` (binário)
```

---




## 📦 Dependências/Requisitos

- **Software:**
  - Python 3.7+
  - Git instalado e configurado
  - Tkinter (já incluso na maioria dos sistemas)
  - Recomendado: instalar as dependências com o comando abaixo (no ambiente virtual):
    ```bash
    pip install -r requirements.txt
    ```
  - As dependências de IA (transformers, torch, sentencepiece) e testes (pytest) estão listadas no `requirements.txt`.

- **Hardware mínimo recomendado:**
  - 2 GB de RAM (mínimo absoluto para uso básico)
  - 4 GB de RAM ou mais recomendado para uso confortável com IA local (T5)
  - CPU dual-core ou superior
  - Espaço em disco: ~500 MB livres (incluindo modelo T5)
  - Não é necessário GPU, mas acelera a geração de resumos se disponível

---



## ♻️ Atualização e Instalação

Sempre que atualizar o projeto, recomenda-se rodar:
```bash
pip install -r requirements.txt
```
para garantir que todas as dependências estejam corretas.

## 📌 Observações

- A análise considera apenas arquivos já adicionados (`staged`)
- Não envia dados para nenhuma API externa
- Pode ser integrado com hooks do Git (ex: `prepare-commit-msg`)
- O resumo IA é totalmente local e opcional (pode ser removido ou ajustado no código)

---

## 🔄 Integração com Hook (opcional)

Adicione ao seu repositório Git:

```bash
echo 'python /caminho/para/changelog-report' > .git/hooks/prepare-commit-msg
chmod +x .git/hooks/prepare-commit-msg
```

---

## 📜 Licença

MIT © 2025 — devs café community
