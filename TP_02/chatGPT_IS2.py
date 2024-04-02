import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Carga las variables de entorno del archivo '.env'
load_dotenv()

client = OpenAI()

# Verifica si el argumento --convers fue proporcionado
modo_conversacion = "--convers" in sys.argv

# Buffer para almacenar la conversación
conversacion = []

def main():
    while True:
        try:
            user_query = input("Ingrese su consulta: ")
            if user_query.lower() == "salir":
                break
            if not user_query.strip():
                print("Por favor, ingrese una consulta válida.")
                continue
            
            # Agrega la consulta al buffer si está en modo conversación
            if modo_conversacion:
                conversacion.append({"role": "user", "content": "You: " + user_query})

            print("You:", user_query)
            response = enviar_consulta_a_chatgpt(user_query)

            print("chatGPT:", response)

            # Agrega la respuesta al buffer si está en modo conversación
            if modo_conversacion:
                conversacion.append({"role": "assistant", "content": response})

        except Exception as e:
            print("Ocurrió un error:", e)
            break

def enviar_consulta_a_chatgpt(query):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=conversacion if modo_conversacion else [
                {"role": "system", "content": "Aquí tu contexto general si es necesario."},
                {"role": "user", "content": "You: " + query}
            ],
            #temperature=1,
            #max_tokens=4096,
            #top_p=1,
            #frequency_penalty=0,
            #presence_penalty=0
        )
        return response.choices[0].message['content']
    except Exception as e:
        print("Error al enviar consulta a ChatGPT:", e)
        return "Error en la respuesta de ChatGPT"

if __name__ == "__main__":
    main()
