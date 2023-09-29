#Note: The openai-python library support for Azure OpenAI is in preview.
import openai

openai.api_type = "azure"
openai.api_base = "https://azopenai-demo1.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = "f90f1208c5e04148b33839150faf5807" #//" os.getenv("f90f1208c5e04148b33839150faf5807")  # noqa: E501

response = openai.Image.create(
    prompt='Car on the moon',    #'USER_PROMPT_GOES_HERE'
    size='1024x1024',
    n=1
)

image_url = response["data"][0]["url"]







# # #Note: The openai-python library support for Azure OpenAI is in preview.
# # import os
# # import openai
# # openai.api_type = "azure"
# # openai.api_base = "https://azopenai-demo1.openai.azure.com/"
# # openai.api_version = "2023-06-01-preview"
# # openai.api_key = os.getenv("f90f1208c5e04148b33839150faf5807")

# # response = openai.Image.create(
# #     prompt='USER_PROMPT_GOES_HERE',
# #     size='1024x1024',
# #     n=1
# # )

# # image_url = response["data"][0]["url"]

# import azure.ai.openai as openai

# # Create an OpenAI client with your Azure OpenAI subscription key and authorization token.  # noqa: E501
# client = openai.Client(subscription_key="688ff410-b717-4bbb-81a4-33b7540fcb71", authorization_token="f90f1208c5e04148b33839150faf5807")  # noqa: E501

# # Generate an image with Azure Dell-E.
# response = client.create_image(prompt="A photo of a cat sitting on a beach")

# # Save the generated image to a file.
# with open("image.png", "wb") as f:
#     f.write(response.content)
