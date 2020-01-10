# 让用户输入
print("Welcome to make your own PC.\nLET'S START!")
input("Enter to Start")


def computer(gpu, cpu, motherboard, ram, harddisk, psu):
    print(f"Your PC has a {gpu} graphics card")
    print(f"And a powerful {cpu}")
    print(f"{ram}GB is enough for you")
    print(f"You must have many blue movie because you choose a {harddisk}GB harddisk")
    print(f"So you need a {psu}W psu to supply power")
    print(f"Finally,they will plug in the {motherboard}")


gpu_1 = input("Type your graphics card here >>>")
cpu_1 = input("Type your cpu here >>>")
ram_1 = input("Choose a type of RAM (GB) >>>")
harddisk_1 = input("Your storage (GB) >>>")
psu_1 = input("Your psu (W) >>>")
motherboard_1 = input("Your motherboard >>>")

computer(gpu_1, cpu_1, motherboard_1, ram_1, harddisk_1, psu_1)
