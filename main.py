from source.grafo import *
from time import perf_counter

akinator = Akinator()
akinator.load_json("init.json")

while True:
    print("""
      /$$$$$$  /$$       /$$                       /$$                        
     /$$__  $$| $$      |__/                      | $$                        
    | $$  \\ $$| $$   /$$ /$$ /$$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
    | $$$$$$$$| $$  /$$/| $$| $$__  $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
    | $$__  $$| $$$$$$/ | $$| $$  \\ $$  /$$$$$$$  | $$    | $$  \\ $$| $$  \\__/
    | $$  | $$| $$_  $$ | $$| $$  | $$ /$$__  $$  | $$ /$$| $$  | $$| $$      
    | $$  | $$| $$ \\  $$| $$| $$  | $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
    |__/  |__/|__/  \\__/|__/|__/  |__/ \\_______/   \\___/   \\______/ |__/      
                                                                          
                                                                          
""")
    print("Menu:\n1 - Akinator\n2 - BFS vs DFS\n3 - sair")
    x = str(input("-> ")).strip()
    if x == "1":
        print("\n")
        akinator.start()
    elif x == "2":
        print("\n")
        inic = perf_counter()
        test_BFS = akinator.BFS()
        end = perf_counter()
        temp_BFS = end-inic

        inic = perf_counter()
        test_DFS = akinator.DFS()
        end = perf_counter()
        temp_DFS = end-inic
        print(f"BFS tempo: {temp_BFS}\nCaminho:")
        for y in test_BFS:
                print(f"{y.keyword} -> ", end="")
        print(f"end\n{len(test_BFS)} nós foram explorados.\n")
        print(f"DFS tempo: {temp_DFS}\nCaminho:")
        for y in test_DFS:
                print(f"{y.keyword} -> ", end="")
        print(f"end\n{len(test_DFS)} nós foram explorados.\n")
        input("...")
    elif x == "3":
        break
    else:
        print("\nPor favor digite as opções no menu!")
        input("...")
    print("\n\n\n")

