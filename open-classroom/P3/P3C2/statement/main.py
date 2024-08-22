# Write your code here!
import os
from bs4 import BeautifulSoup

# print("Current working directory:", os.getcwd())

with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

page_title = soup.title.string

text_h1 = soup.h1.string

products = soup.find_all("li")
products_list = []
for product in products:
    name = product.h2.string
    price = product.find("p", string=lambda s:"Price" in s).string
    products_list.append((name, price))

description_list = []
for product in products:
    description = product.find("p", string=lambda s:"Description" in s).string
    description_list.append(description)

print("Title of the page: ", page_title)
print("text of the h1 tag: ", text_h1)
print("Product list: ", products_list)
print("List of product description : ", description_list)

for i, (name, price) in enumerate(products_list):
    euro_price = int(price.split()[2].replace("€",""))
    dollar_price = euro_price * 1.2
    products_list[i] = (name, f"{dollar_price}$")


print("List of products : ", products_list)





