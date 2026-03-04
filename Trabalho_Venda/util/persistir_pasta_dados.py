import os

PASTA_DADOS = "dados"

def garantir_pasta_dados():
    """Cria a pasta dados caso não exista."""
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)


def caminho_arquivo(nome):
    """Retorna o caminho completo do arquivo."""
    garantir_pasta_dados()
    return os.path.join(PASTA_DADOS, nome)