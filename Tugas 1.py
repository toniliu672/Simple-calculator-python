def calculator():
    print("""
    Calculator """)
    while True:
        try:
            angka1 = float(input("Angka pertama : "))
            angka2 = float(input("Angka kedua : "))
            break
        except ValueError:
            print("""Masukkan Angka!
            """)

    operasi = input("Operasi : ")
    if operasi == 'x':
        result = angka1 * angka2
    elif operasi == '/':
        result = angka1 / angka2
    elif operasi == '+':
        result = angka1 + angka2
    elif operasi == '-':
        result = angka1 - angka2
    elif operasi == '^':
        result = angka1 ** angka2
    elif operasi == '?':
        result = (angka1 + 5) - (angka2 - 1)

    else : 
        print("pilih operasi yang sesuai")

    print(f"hasil yang diperoleh adalah {result}")

calculator()