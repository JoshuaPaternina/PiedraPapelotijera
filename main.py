import random

opciones=("roca","papel","tijera")
rondas = 1
ganar_usurio = 0
ganar_cpu = 0
empatar = 0

while True:
  
  print("|||||"*4)
  print(f"|||||| Ronda {rondas} |||||")
  print("|||||"*4)
  usuario = input("Escoga entre roca, papel o tijera => ")
  usuario = usuario.lower()
  
  
  CPU = random.choice(opciones)
  if not usuario in opciones:
    print("Esa opción NO es valido")
    print("-----------"*5)
    continue  
  rondas += 1
  
  print("-----------"*5)
  print(f"Usted escogio {usuario}")
  print(f"El computador escogio {CPU}")
  print("-----------"*5)
  
  if usuario == CPU:
    print("Empate")
    print("-----------"*5)
    empatar += 1
  elif usuario == "roca":
    if CPU == "tijera":
      print("Piedra gana a tijera")
      print("Usted gano!!!")
      print("-----------"*5)
      ganar_usurio +=1
    else:
    
      print("Papel gana a roca")
      print("Usted perdio 😢")
      print("-----------"*5)
      ganar_cpu +=1
      
  
  elif usuario == "papel":
     if CPU == "roca":
        print("Papel gana a roca")
        print("Usted gano!!!")
        print("-----------"*5)
        ganar_usurio +=1
     else:
        print("Tijera gana a papel")
        print("Usted perdio 😢")
        print("-----------"*5)
        ganar_cpu +=1
  elif usuario == "tijera":
    if CPU == "papel":
      print("Tijera gana a papel")
      print("Usted gano!!!")
      print("-----------"*5)
      ganar_usurio +=1
    else:
      print("Roca gana a tijera")
      print("Usted perdio 😢")
      print("-----------"*5)
      ganar_cpu +=1
      
  if ganar_usurio >= 2:
    print("°°°°°°°°"*4)
    print("Felicitaciones usted gano!!! °°")
    print(f"Se empato {empatar} veces")
    print("°°°°°°°°"*4)
    break
  if ganar_cpu >=2:
    print("°°°°°°°°"*4)
    print("Lo sentimos usted perdio 😭😭")
    print(f"Se empato {empatar} veces")
    print("°°°°°°°°"*4)
    break
  