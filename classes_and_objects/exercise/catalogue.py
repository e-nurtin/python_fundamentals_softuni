class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]
        # products_by_letter = []
        # for product in self.products:
        #     if product[0] == first_letter:
        #         products_by_letter.append(product)
        # return products_by_letter

    def __repr__(self):
        string_to_return = f"Items in the {self.name} catalogue:\n"
        string_to_return += '\n'.join(sorted(self.products))
        return string_to_return
    # self.products.sort()
    # newline = '\n'
    # return f"Items in the {self.name} catalogue:\n" \
    #        f"{f'{newline.join(self.products)}'}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")


a = Catalogue('Guitarists')
a.add_product('John Frusciante')
a.add_product('Jimi Hendrix')
a.add_product('John Mayer')
a.add_product('Eric Clapton')
a.add_product('James Heatherfield')
a.add_product('Arctic Monkeys')

print(a.get_by_letter('J'))
print(a)
print(catalogue.get_by_letter("C"))
print(catalogue)
