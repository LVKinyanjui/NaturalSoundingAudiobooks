import requests
import os

import os
api_key = os.getenv("ELEVENLABS_API_KEY")

def main(text=None, output_filename='data/output.mp3'):
  CHUNK_SIZE = 1024
  voice_id = "pMsXgVXv3BLzUgSXRplE"
  url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

  headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": f"{api_key}"
  }

  if text is None:
      text = """Born and raised in the charming south, 
    I can add a touch of sweet southern hospitality 
    to your audiobooks and podcasts"""
       
  data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.5
    }
  }

  response = requests.post(url, json=data, headers=headers)
  with open(output_filename, 'wb') as f:
      for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
          if chunk:
              f.write(chunk)

if __name__ == "__main__":
    main()