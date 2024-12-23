from flask import Flask, Blueprint, jsonify, abort, request, render_template
from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

chat = Blueprint('chat',__name__)


@chat.route("/image_generation", methods=["POST"])
def get_chat_index():
    args = request.get_json()

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    response = client.images.generate(
        model="dall-e-2",
        prompt=args.get('prompt'),
        size="512x512",
        n=1,
    )
    print(response)
    return jsonify({'url':response.data[0].url})

