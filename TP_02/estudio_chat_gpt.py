"""Programa de consultas a Chat GPT.

Este script permite al usuario hacer consultas a ChatGPT utilizando la API de OpenAI.
Carga las credenciales de la API desde variables de entorno, permite realizar consultas
interactivas en modo de conversación, y maneja las respuestas de la API.

"""
import argparse
import os
import sys
import requests
from dotenv import load_dotenv
from rich.console import Console


console = Console()

"""Limpia la consola al inicio de la ejecución."""
os.system('cls' if os.name == 'nt' else 'clear')

#Muestra un mensaje de bienvenida.
console.print('Bienvenido al ChatGPT 3.5', style='green bold')

def load_environment_variables():
    """Carga las variables de entorno desde el archivo .env."""
    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        organizacion = os.getenv("ORGANIZACION")
        return api_key, organizacion
    except OSError as load_env_error:
        console.print(f"Error al cargar el archivo .env: {load_env_error}",
                      style="red on white")
        sys.exit("No se pudo cargar la configuración inicial.")
    return None, None

def get_models(api_key, organizacion):
    """Obtiene la lista de modelos disponibles en la API de OpenAI."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "OpenAI-Organization": organizacion
    }
    response = requests.get("https://api.openai.com/v1/models", headers=headers, timeout=10)
    return response.json()

def chat_completo(query, api_key, organizacion):
    """Realiza una consulta completa a ChatGPT y devuelve la respuesta de la API."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "OpenAI-Organization": organizacion
    }
    data = {
        "model": "gpt-3.5-turbo-0125",
        "messages": [{"role": "user", "content": f"You: {query}"}],
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/chat/completions",
                             headers=headers, json=data, timeout=10)
    if response.status_code != 200 or 'choices' not in response.json():
        console.print(f"Error en la solicitud: {response.status_code}, "
                      f"Respuesta: {response.text}", style="red on white")
        return {
            "choices": [{"message":
                         {"content": "No puedo procesar tu solicitud en este momento."}}]}
    return response.json()

def consulta_query():
    """Solicita al usuario una consulta y valida que no esté vacía."""
    while True:
        query = input("\nIngrese su consulta (pulse 'cursor Up' para obtener la última consulta): ")
        if query.strip():
            return query
        console.print('Por favor, ingrese una consulta válida.\n', style='red on white')

def procesar_query(query, api_key, organizacion):
    """Procesa la consulta del usuario a través de la API y maneja la respuesta."""
    try:
        console.print(f"\nYou: {query}\n", style='magenta')
        completo = chat_completo(query, api_key, organizacion)
        response = completo['choices'][0]['message']['content']
        print("Respuesta de chatGPT:")
        print(f"chatGPT: {response}")
        return response
    except KeyError as e:
        console.print(f"Ocurrió un error al procesar la consulta: {e}", style='red on white')
    except Exception as e:
        console.print(f"Ocurrió un error inesperado: {e}", style='red on white')

def main():
    """Función principal que maneja la lógica de modo de conversación basada en argumentos."""
    parser = argparse.ArgumentParser(description='Procesar consultas con chatGPT')
    parser.add_argument('--convers', action='store_true', help='Modo de conversación')
    args = parser.parse_args()

    api_key, organizacion = load_environment_variables()

    if api_key is None or organizacion is None:
        return

    if not args.convers:
        console.print(
            "Modo de conversación desactivado. Ejecute el script con --convers para habilitar.",
            style="red on white")
        return

    while True:
        try:
            query = consulta_query()
            procesar_query(query, api_key, organizacion)
            console.print("\n¿Desea realizar otra consulta? (s/n): "
                          , style="green on white", end="")
            choice = input().strip().lower()
            if choice != 's':
                break
        except Exception as e:
            console.print(f"Ocurrió un error en la ejecución del programa: {e}",
                          style="red on white")

if __name__ == "__main__":
    main()
