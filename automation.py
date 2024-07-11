import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")

product_list = inv_file["Sheet1"]

product_per_suplier = {}

for product_row in range(2, product_list.max_row + 1):
    suplier_names = product_list.cell(product_row, 4).value
    print(product_row, suplier_names)