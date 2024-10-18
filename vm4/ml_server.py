from flask import Flask, request, jsonify
import torch
import torchvision.transforms as transforms
from PIL import Image
import io
import base64
import os

app = Flask(__name__)

# Load the model
model_path = "cifar10_resnet20.pt"
if not os.path.exists(model_path):
    print(f"Warning: Model file {model_path} not found. Downloading...")
    model = torch.hub.load('chenyaofo/pytorch-cifar-models', 'cifar10_resnet20', pretrained=True)
    torch.save(model.state_dict(), model_path)
else:
    model = torch.hub.load('chenyaofo/pytorch-cifar-models', 'cifar10_resnet20', pretrained=False)
    model.load_state_dict(torch.load(model_path))

model.eval()

# Preprocessing
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.4914, 0.4822, 0.4465], std=[0.247, 0.243, 0.261]),
])

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

def decode_image(img_data):
    img_bytes = base64.b64decode(img_data)
    return Image.open(io.BytesIO(img_bytes))

def infer_image(image):
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)
    with torch.no_grad():
        output = model(input_batch)
    predicted_idx = torch.max(output, 1)[1]
    return classes[predicted_idx.item()]

@app.route('/infer', methods=['POST'])
def infer():
    if 'image' not in request.json:
        return jsonify({"error": "No image data provided"}), 400
    
    image = decode_image(request.json['image'])
    inferred_value = infer_image(image)
    
    return jsonify({"InferredValue": inferred_value})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
