from gradio_client import Client

client = Client("https://d3b3469b66358c749b.gradio.live")
result = client.predict(
    "i want the interface code",  # Substitua pela entrada desejada
    api_name="/predict"
)
print(result)