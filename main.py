def count_notes(value, notes):
  notes_count = []
  for i in range(len(notes)):
    note = value//notes[i]
    value = value%notes[i]
    notes_count.append(note)
  return notes_count

def run_program():
  car = []
  NOTES = [100, 50, 20, 10, 5, 2, 1]
  while True:
    product = {"name":"", "price":0}
    name = input("Insira o nome do produto: ")
    if not name: print("\nNome inválido\n")
    else:
      while True:
        price = float(input("insira o valor do produto: "))
        if not price or price < 0 or type(price) != float: print("Valor inválido")
        else: product["name"] = name; product["price"] = price; break
      car.append(product)
      choice = input("Deseja inserir mais itens?(s/n): ")
      if choice == "n": break
      if len(car) >= 10: print("Número máximo de produtos excedido."); break
  total = sum(list(map(lambda item: item['price'], car)))
  print(f"total: {total}")
  print(*list(map(lambda product: f"{product['name']} --- R${product['price']}\n", car)))
  print("serão necessários: \n")
  for i in range(len(NOTES)): 
    if count_notes(total, NOTES)[i] > 0: print(f"{int(count_notes(total, NOTES)[i])} notas de {NOTES[i]}")



run_program()
