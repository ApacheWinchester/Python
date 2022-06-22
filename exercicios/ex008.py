# conversor de medidas
b = int(input("Digite o valor  que deseja ver a conversão "))
print("{} metros é equivalente á {} decâmetros(dam) \n á {} Hectômetro(hm) \n á {} Quilômetros(km) \n á {} De´cimetros(dm) \n á {} Centímetros(cm) \n á {} Milímetros(mm)"
      .format(b, b * 10, b *100, b * 1000, b / 10, b / 100, b / 1000))
