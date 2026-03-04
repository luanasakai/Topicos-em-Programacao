# Define the __all__ variable
__all__ = ["menu_produto", "menu_cliente", "menu_venda", "main"]

# Import the submodules
from . import menu_produto
from . import menu_cliente
from . import menu_venda
from . import main
