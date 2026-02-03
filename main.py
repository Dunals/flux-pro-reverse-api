import requests
import time
import os

# --- Configuration ---
API_URL = "https://fluxai.pro/api/tools/fast"
OUTPUT_FILENAME = "flux_image.jpg"

# Headers to act like a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Origin": "https://fluxai.pro",
    "Referer": "https://fluxai.pro/",
    "Content-Type": "application/json"
}

def generate_image(prompt):
    print(f"🚀 Generating: '{prompt}'...")

    payload = {
        "prompt": prompt,
        "aspect_ratio": "1:1" # You can change to "16:9" or "9:16"
    }

    try:
        # 1. Send Prompt to API
        response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=60)
        
        if response.status_code != 200:
            print(f"❌ Error: API returned status {response.status_code}")
            print(response.text)
            return

        data = response.json()
        
        # 2. Extract Image URL
        if data.get("ok") and "data" in data and "imageUrl" in data["data"]:
            image_url = data["data"]["imageUrl"]
            print(f"🔗 Link found: {image_url}")
            
            # 3. Download the Image
            print("⬇️  Downloading...")
            img_response = requests.get(image_url, timeout=30)
            
            if img_response.status_code == 200:
                # Save to file
                with open(OUTPUT_FILENAME, "wb") as f:
                    f.write(img_response.content)
                print(f"✅ Success! Saved as: {OUTPUT_FILENAME}")
            else:
                print("❌ Failed to download the image file.")
        
        else:
            print("⚠️ API returned success but no image link found.")
            print(data)

    except Exception as e:
        print(f"💥 Critical Error: {e}")

if __name__ == "__main__":
    # Change prompt here
    user_prompt = "ultra detailed dark enchanted forest at night, narrow dirt path leading into the darkness, tall pine trees forming a tunnel overhead, almost black silhouettes, faint cold blue moonlight leaking through the branches, light mist at ground level, tiny glowing fireflies floating in the air, subtle fog rays, cinematic composition, high contrast, volumetric lighting, hyper realistic, 4k"
    
    generate_image(user_prompt)
