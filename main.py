from gradio_client import Client

client = Client("https://modelspeech.onrender.com/createspace/")
result = client.predict(
		token="Hello!!",
		space_name="Hello!!",
		plan_type="Free",
		hardware_type="cpu-basic",
		ram_size=2,
		storage_size=5,
		gpu_enabled=False,
		api_name="/add_space"
)
print(result)
