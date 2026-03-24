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
        akinator.start()
    elif x == "2":
        inic = perf_counter()
        akinator.BFS()
        end = perf_counter()
        temp_BFS = end-inic

        inic = perf_counter()
        akinator.DFS()
        end = perf_counter()
        temp_DFS = end-inic
        print(f"BFS tempo: {temp_BFS}")
        print(f"DFS tempo: {temp_DFS}")
        input("...")
    elif x == "3":
        break
    else:
        print("Porfavor digite as opções no meu!")
        input("...")
    print("\n\n\n")

