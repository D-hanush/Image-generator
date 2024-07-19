import requests

API_KEY = "hf_geSuDCwDhDNYbuqTdZfbVlcUk********" #Your API KEY

def img_gen(prompt, output_file):
    # API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5" #generates best pic but slow

    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0" #fast but generates less quality pic

    # API_URL = "https://api-inference.huggingface.co/models/ARDICAI/stable-diffusion-2-1-finetuned" #optional link

    headers = {"Authorization": f"Bearer {API_KEY}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.content
    
    image_bytes = query({"inputs": prompt})

    with open(output_file, "wb") as f:
        f.write(image_bytes)
    print(f"Image saved as {output_file}")

if _name_ == "_main_":
    user_prompt = input("Enter the description for the image you want to generate: ")
    output_file = "generated_image.png"
    img_gen(user_prompt, output_file)
