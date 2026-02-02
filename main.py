import os
from utils.utils import get_transactions_data



script_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(script_dir, "data")
file_path = os.path.join(target_dir, "operations.json")
print(get_transactions_data (file_path))
