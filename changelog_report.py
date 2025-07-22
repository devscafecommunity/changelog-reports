import subprocess
import os
from pathlib import Path

TEXTUAL_TYPES = {'.py', '.js', '.ts', '.java', '.c', '.cpp', '.cs', '.html', '.css', '.go', '.rs'}
LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)

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

def generate_report():
    changelog = []
    commit_summary = []

    files = get_git_diff_files()
    for status, file_path in files:
        suffix = Path(file_path).suffix
        if suffix in TEXTUAL_TYPES and not is_binary(file_path):
            diff = get_file_diff(file_path)
            changelog.append(f"\n### {file_path}\n```\n{diff}\n```")
            commit_summary.append(f"- Modificações em `{file_path}`")
        else:
            changelog.append(f"\n### {file_path} (binário ou não analisável)\n")
            commit_summary.append(f"- Alteração em `{file_path}` (binário)")

    Path(LOG_DIR / 'changelog.txt').write_text('\n'.join(changelog), encoding='utf-8')
    Path(LOG_DIR / 'commit_details.txt').write_text("Resumo do commit:\n" + '\n'.join(commit_summary), encoding='utf-8')
    print("✅ Relatórios gerados em 'logs/'")