class Market:
    def __init__(self):
        self.filename="product.txt"
        self.file=open(self.filename,"a+",encoding="utf-8")
        
    def __del__(self):
        print("Destructor")
        if self.file:
            self.file.close()


    def list_product(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            content = file.read()
            lines = content.splitlines()

        if not lines:
            print("No products found in the file.")
            return
        for line in lines:
            line_lst = line.split(",")
            if len(line_lst) == 1:  # Eğer boş satır varsa, atla
                continue
            print("Product name: " + line_lst[0] + ", Category: " + line_lst[1] + ", Price: " + line_lst[
                2] + ", stock quantity: " + line_lst[3])


    def add_product(self):
        product_name=input("Enter the name of the product:")
        category=input("Enter the category of the product:")
        price=input("Enter the price:")
        stock_quantity=input("Enter the stock quantity:")

        self.file.write(product_name+","+category+","+price+","+stock_quantity+"\n")
        self.file.flush()
        print(f"{product_name} has been added to the file.")
        
        

    def delete_product(self):
        lst_lines=[]
        product_name = input("Enter the name of the product or product no:")

        self.file.seek(0)
        for line in self.file:
            line_lst=line.split(",")
            if len(line_lst)==1:    #Boş satır varsa bu satırı atla
                continue
            if product_name in line_lst:
                continue
            lst_lines.append(line)

        self.file.close()

        with open(self.filename, "w", encoding="utf-8") as file:
            for line in lst_lines:
                file.write(line)


        self.file = open(self.filename, "a+", encoding="utf-8")
        print(f"The book named {product_name} has been removed from the file.")

        
try:
    market = Market()
    while True:
        choice=input("""
        *** MENÜ ***
        1) Ürünleri Listele
        2) Ürün Ekle
        3) Ürün Sil
        4) Çıkış
                     """)
        if choice == "1":
            market.list_product()
        elif choice == "2":
            market.add_product()
        elif choice == "3":
            market.delete_product()
        elif choice ==  "4":
            print("Exiting the program...")
            break
        else:
            print("Please enter 1, 2, 3 or 4")
finally:
    del market

