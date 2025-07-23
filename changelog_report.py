
import subprocess
import os
from pathlib import Path

TEXTUAL_TYPES = {'.py', '.js', '.ts', '.java', '.c', '.cpp', '.cs', '.html', '.css', '.go', '.rs'}

def get_git_diff_files():
    result = subprocess.run(['git', 'diff', '--cached', '--name-status'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    return [line.split('\t') for line in lines if line]

def is_binary(file_path):
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            return b'\0' in chunk
    except:
        return True

def get_file_diff(file_path):
    result = subprocess.run(['git', 'diff', '--cached', '--', file_path], capture_output=True, text=True)
    return result.stdout.strip()

def summarize_changes(files):
    summary = []
    for status, file_path in files:
        if status == 'A':
            summary.append(f"Adicionado `{file_path}`")
        elif status == 'M':
            summary.append(f"Modificado `{file_path}`")
        elif status == 'D':
            summary.append(f"Removido `{file_path}`")
        else:
            summary.append(f"Alteração em `{file_path}`")
    return summary

def generate_report():
    cwd = Path.cwd()
    log_dir = cwd / 'logs'
    log_dir.mkdir(exist_ok=True)
    import datetime
    def run_git(cmd):
        return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()

    # Informações extras
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = run_git(['git', 'config', 'user.name'])
    email = run_git(['git', 'config', 'user.email'])
    branch = run_git(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])

    changelog = [f"# Changelog das alterações\n",
                f"**Data/Hora:** {now}",
                f"**Usuário:** {user} <{email}>",
                f"**Branch:** `{branch}`\n"]

    files = get_git_diff_files()
    commit_lines = []
    table = ["| Arquivo | Tipo |", "|---|---|"]

    for status, file_path in files:
        suffix = Path(file_path).suffix
        if status == 'A': tipo = 'Adicionado'
        elif status == 'M': tipo = 'Modificado'
        elif status == 'D': tipo = 'Removido'
        else: tipo = 'Alteração'
        if suffix in TEXTUAL_TYPES and not is_binary(file_path):
            diff = get_file_diff(file_path)
            changelog.append(f"## {file_path}\n\n```diff\n{diff}\n```")
            commit_lines.append(f"{tipo} {file_path}")
        else:
            changelog.append(f"## {file_path} (binário ou não analisável)\n")
            commit_lines.append(f"Alteração em {file_path} (binário)")
        table.append(f"| `{file_path}` | {tipo} |")

    changelog.insert(4, f"**Total de arquivos alterados:** {len(files)}\n")
    changelog.insert(5, '\n'.join(table) + '\n')

    # Markdown formatado
    Path(log_dir / 'changelog.md').write_text('\n'.join(changelog), encoding='utf-8')

    # Mensagem de commit descritiva
    commit_message = "; ".join(commit_lines)
    commit_cmd = f'git commit -m "{commit_message}"'
    Path(log_dir / 'commit_details.txt').write_text(commit_cmd, encoding='utf-8')

    print(f"Relatórios gerados em '{log_dir}/'")