# Manga Downloader API

## Overview

The Manga Downloader API is a FastAPI-based application that allows users to download manga chapters as ZIP files. The application fetches images for a given manga chapter from the MangaDex API, compiles them into a ZIP archive, and returns the archive as a downloadable file.

## Features

- Welcome endpoint to test if the API is running.
- Fetches manga chapter images from the MangaDex API.
- Compiles images into a ZIP file and returns it as a downloadable response.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/manga-downloader-api.git
    cd manga-downloader-api
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```bash
    uvicorn main:app --host 127.0.0.1 --port 3000 --reload
    ```

2. **Endpoints:**

    - **Welcome Endpoint:**
        ```
        GET /
        ```
        Response:
        ```json
        {
            "message": "welcome"
        }
        ```

    - **Get Manga Chapter:**
        ```
        GET /{manga_id}
        ```
        Path Parameters:
        - `manga_id`: The ID of the manga chapter to download.

        Response:
        - A ZIP file containing the manga chapter images.

        Example:
        ```
        GET /e71d0d5c-ddc6-42ea-b40d-799983b5eb89
        ```

        This will return a ZIP file named `manga_e71d0d5c-ddc6-42ea-b40d-799983b5eb89.zip`.

## Example

To download a manga chapter, make a GET request to the `/{manga_id}` endpoint with the appropriate manga ID. For example:
```bash
curl -o manga_e71d0d5c-ddc6-42ea-b40d-799983b5eb89.zip http://127.0.0.1:3000/e71d0d5c-ddc6-42ea-b40d-799983b5eb89
```

Live demo available at: [manga-downloader-api.vercel.app](https://manga-downloader-api.vercel.app/)

This command will download the manga chapter with ID `e71d0d5c-ddc6-42ea-b40d-799983b5eb89` and save it as `manga_e71d0d5c-ddc6-42ea-b40d-799983b5eb89.zip`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [MangaDex API](https://api.mangadex.org/)
- [Requests](https://docs.python-requests.org/en/latest/)

---

**Note:** This project is for educational purposes and should be used in compliance with MangaDex's terms of service.
