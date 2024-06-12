import uvicorn
import zipfile
import requests
from io import BytesIO
from fastapi import FastAPI, Response
from concurrent.futures import ThreadPoolExecutor, as_completed

app = FastAPI()

@app.get("/")
def welcome():
	return {
		"message": "welcome"
	}

def image_fetcher(url):
	res = requests.get(url)	
	content = res.content
	return content

@app.get("/{manga_id}")
def get_manga(manga_id: str):

	res = requests.get(f"https://api.mangadex.org/at-home/server/{manga_id}")
	data = res.json()

	base_url = data["baseUrl"]
	hash = data["chapter"]["hash"]

	images_url = [f"{base_url}/data-saver/{hash}/{i}" for i in data["chapter"]["dataSaver"]]
	zip_buffer = BytesIO()

	with zipfile.ZipFile(zip_buffer, "w") as zip_file:
		with ThreadPoolExecutor(max_workers=len(images_url)) as executor:
			future_to_index = {executor.submit(image_fetcher, item): index for (index, item) in enumerate(images_url)}

			for future in as_completed(future_to_index):
				index = future_to_index[future]
				try:
					content = future.result()
					zip_file.writestr(f"image_{index}.jpg", content)
				except Exception as e:
					print(f"Error fetching image {index}: {e}")

	zip_buffer.seek(0)

	# Return the ZIP file as a response
	return Response(content=zip_buffer.getvalue(), media_type="application/zip", headers={
		"Content-Disposition": f"attachment; filename=manga_{manga_id}.zip"
	})
