import openai

openai.api_type = "azure"
openai.api_base = "https://azopenai-demo1.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = "f90f1208c5e04148b33839150faf5807"

# Get the user input
user_prompt = input("Enter the prompt for the image: ")

# Generate the image
response = openai.Image.create(
    prompt=user_prompt,
     size='1024x1024',
     n=2
)

try:
    image_url = response["data"][0]["URL"]
except KeyError:
    print("Image generation failed.")
else:
    print("Image URL:", image_url)