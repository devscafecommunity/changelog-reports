# 📄 changelog-report

Ferramenta leve em Python para gerar relatórios de alterações com base nos arquivos *staged* no Git.

---

## ✨ Visão Geral

O `changelog-report` analisa os arquivos adicionados ao staging (`git add .`) e gera:

- 📘 Um **relatório completo (`logs/changelog.txt`)** com diffs e arquivos binários listados
- 🧾 Um **resumo (`logs/commit_details.txt`)** pronto para ser usado como mensagem de commit

Também conta com uma **interface gráfica (GUI)** opcional, ativada via `--gui`, ideal para uso mais visual.

---

## 🚀 Como Usar

### 🔧 Modo CLI (padrão)

```bash
git add .
python .
