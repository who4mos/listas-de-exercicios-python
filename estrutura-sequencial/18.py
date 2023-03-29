from math import ceil, trunc

mb = float(input("Tamanho do arquivo (MB): "))
mbps = float(input("Velocidade da internet (Mbps): "))

mbps /= 8 # transformar Mb em MB (1 byte sao 8 bits)

seconds = ceil(mb / mbps)

minutes = trunc(seconds // 60)
seconds_remaining = seconds - (minutes * 60)

print(f"ETA: {minutes:02}:{seconds_remaining:02} min")
