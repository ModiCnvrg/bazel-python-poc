from transformers import GPT2LMHeadModel, GPT2Tokenizer
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
current_directory = os.path.dirname(os.path.realpath(__file__))

# Load the model and tokenizer
model_name = 'gpt2'
model_dir = os.path.join(current_directory, 'model')
model = GPT2LMHeadModel.from_pretrained(model_dir)
tokenizer = GPT2Tokenizer.from_pretrained(model_dir)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    inputs = data.get('inputs')
    parameters = data.get('parameters', {})

    # Tokenize input
    input_ids = tokenizer.encode(inputs, return_tensors='pt')

    # Generate text
    output = model.generate(input_ids, **parameters)
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({'generated_text': output_text})

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)