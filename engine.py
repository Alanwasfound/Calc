from py4j.java_gateway import JavaGateway
import subprocess
import threading
import time
import os


if not os.path.exists("server.class"):
    print("Compilando o arquivo Java...")
    # Compila o arquivo Java e espera a conclusão
    subprocess.run(["javac", "-cp", ".:./py4j.jar", "AppJava.java"], check=True)

def start_java_server():
    subprocess.run(["java", "-cp", ".:./py4j.jar", "server"])

server_thread = threading.Thread(target=start_java_server)
server_thread.start()

time.sleep(10)

gateway = JavaGateway()

app_java = gateway.entry_point

print("--- Comunicação Python -> Java ---")
mensagem = app_java.saudacao("Alisson")
print(mensagem)

with open("result.txt", "w") as f:
    f.write(mensagem)

print("\n--- Finalizando o servidor Java ---")
gateway.shutdown()

