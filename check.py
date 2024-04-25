import pandas as pd
import json

with open('data.json', 'r') as file:
    data = json.load(file)

# Chuyển đổi dữ liệu thành DataFrame
df = pd.json_normalize(data)

# Lưu DataFrame vào file Excel
df.to_excel('publications.xlsx', index=False)

print("Data saved to publications.xlsx")