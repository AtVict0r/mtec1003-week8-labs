partyCountDown = int(input("Let's party...\nHow long 'til the party? "))
if partyCountDown < 1:
    print("PARTY NOW!!!")
else:
    for i in range(partyCountDown, 0, -1):
        print("PARTY IN", i)
    print("PARTY TIME!!!")