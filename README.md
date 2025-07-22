# 📄 changelog-report

Ferramenta leve em Python para gerar relatórios de alterações com base nos arquivos *staged* no Git.

---

## ✨ Visão Geral

O `changelog-report` analisa os arquivos adicionados ao staging (`git add .`) e gera:

- 💘 Um **relatório completo (`logs/changelog.txt`)** com diffs e arquivos binários listados
- 🧾 Um **resumo (`logs/commit_details.txt`)** pronto para ser usado como mensagem de commit

Também conta com uma **interface gráfica (GUI)** opcional, ativada via `--gui`, ideal para uso mais visual.

---

## 🚀 Como Usar

### 🔧 Modo CLI (padrão)

```bash
git add .
python .
```

Isso irá gerar os relatórios na pasta `logs/`.

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
✅ Não usa inteligência artificial — ideal para projetos offline/locais

---

## 🔎 Exemplo de commit_details.txt

```
Resumo do commit:
- Modificações em `src/utils.py`
- Alteração em `image/logo.png` (binário)
```

---

## 📆 Requisitos

- Python 3.7+
- Git instalado e configurado no ambiente
- Tkinter (já incluído com o Python em Windows/macOS/Linux)

---

## 📌 Observações

- A análise considera apenas arquivos já adicionados (`staged`)
- Não envia dados para nenhuma API externa
- Pode ser integrado com hooks do Git (ex: `prepare-commit-msg`)

---

## 🔄 Integração com Hook (opcional)

Adicione ao seu repositório Git:

```bash
echo 'python /caminho/para/changelog-report' > .git/hooks/prepare-commit-msg
chmod +x .git/hooks/prepare-commit-msg
```

---

## 📜 Licença

MIT © 2025 — SeuNomeAqui
