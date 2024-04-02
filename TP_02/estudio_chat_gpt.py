"""Programa de consultas a Chat GPT"""

import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

"""Verifica si el argumento --convers fue proporcionado"""
modo_conversacion = "--convers" in sys.argv

"""Buffer para almacenar la conversación"""
conversacion = []

def consulta_uruario():
    while True:
        try:
            pregunta_usuario=input("Ingrese una consulta a ChatGPT: ")

            if pregunta_usuario == "":
                raise Exception("No escribio ninguna consulta, por favor reingrese una")

            if modo_conversacion:
                conversacion.append({"role": "user", "content": consulta_uruario})

            print("You: "+pregunta_usuario)

            respuesta = consulta_chat_gpt(pregunta_usuario)

            if modo_conversacion:
                conversacion.append({respuesta.choices[0].message})

            print("ChatGPT: "+ respuesta.choices[0].message.content)

        except Exception as e:
            print(e)


def consulta_chat_gpt(consulta, conversacion=None):
    if conversacion is None:
        conversacion = []

    """Prepara los mensajes, incluyendo la conversación existente y la nueva consulta"""
    mensajes = conversacion + [
        {
            "role": "user",
            "content": consulta
        }
    ]

    respuesta_gpt = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=mensajes,
        temperature=1,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return respuesta_gpt


consulta_uruario()
