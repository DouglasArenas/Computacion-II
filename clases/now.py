import asyncio

async def encontrar_divisibles(rango, div_por):
    
    print("Buscando numeros en el rango {} divisibles por {}".format(rango, div_por))
    encontrado = []
    for i in range(rango):
        if i % div_por == 0:
            encontrado.append(i)
        if i % 500000 == 0: #por cada 500000 ciclos espera y revisa el levelloop
            await asyncio.sleep(0.001)
    print("Listo con nums en el rango {} divisibles por {}".format(rango, div_por))
    return encontrado

async def main():
    
    divs1 = encontrar_divisibles(50800000, 34113)
    divs2 = encontrar_divisibles(100052, 3210)
    divs3 = encontrar_divisibles(500, 3)
    await asyncio.gather(divs1, divs2, divs3)


if __name__ == '__main__':
    asyncio.run(main())

