import os
import shutil
import subprocess
from pathlib import Path
import pytest

def setup_module(module):
    # Cria um diretório temporário para o teste
    os.makedirs('test_repo', exist_ok=True)
    os.chdir('test_repo')
    subprocess.run(['git', 'init'], check=True)
    with open('arquivo.py', 'w', encoding='utf-8') as f:
        f.write('print("Hello World!")\n')
    subprocess.run(['git', 'add', 'arquivo.py'], check=True)
    # Copia o script principal para o diretório de teste usando caminho absoluto
    base_dir = Path(__file__).parent.parent.resolve()
    shutil.copyfile(str(base_dir / 'changelog_report.py'), 'changelog_report.py')
    shutil.copyfile(str(base_dir / '__main__.py'), '__main__.py')


def teardown_module(module):
    os.chdir('..')
    def onerror(func, path, exc_info):
        import errno
        if exc_info[1].errno == errno.EACCES:
            os.chmod(path, 0o777)
            func(path)
        else:
            raise
    shutil.rmtree('test_repo', onerror=onerror)


def test_gera_logs_e_commit_details():
    # Executa o script principal
    subprocess.run(['python', '__main__.py'], check=True)
    logs_dir = Path('logs')
    assert logs_dir.exists()
    changelog = logs_dir / 'changelog.md'
    commit_details = logs_dir / 'commit_details.txt'
    assert changelog.exists()
    assert commit_details.exists()
    # Verifica se o changelog tem conteúdo
    changelog_content = changelog.read_text(encoding='utf-8')
    assert 'arquivo.py' in changelog_content
    # Verifica se o commit_details tem comando de commit
    commit_cmd = commit_details.read_text(encoding='utf-8')
    assert commit_cmd.startswith('git commit -m')


## Executa o teste
if __name__ == "__main__":
    pytest.main([__file__]) 
