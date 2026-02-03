# Flux Pro Reverse API Client

A lightweight Python client to interact with the high-performance **Flux.1 AI image generation model**. This tool demonstrates how to reverse-engineer web-based generation tools to integrate state-of-the-art AI imagery into Python applications without official paid SDKs.

## 🚀 Key Features

* **Flux.1 Model Access:** Generates high-fidelity, photorealistic images using the latest Flux architecture.
* **Header Spoofing:** Implements browser mimicry (`User-Agent`, `Origin`, `Referer`) to bypass basic bot detection logic.
* **Direct Image Retrieval:** Automates the full flow from prompt submission to JSON parsing and binary image downloading.
* **Configurable Aspect Ratios:** Supports dynamic payload modification for 1:1, 16:9, or 9:16 outputs.

## 🛠 Dependencies

* Python 3.x
* `requests`

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/flux-pro-reverse-api.git](https://github.com/yourusername/flux-pro-reverse-api.git)
    cd flux-pro-reverse-api
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Usage

Run the script to generate an image based on the predefined prompt:

```bash
python main.py
