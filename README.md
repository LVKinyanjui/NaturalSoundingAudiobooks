# NaturalSoundingAudiobooks
An open source text to speech service using a variety of techniques (whatever works)

## Prerequisites
If you intend to run this locally first clone the repo with
`git clone <repo-url>`
Then change into the local repo directory.

## How to Run
1.Ensure you have python installed (This was tested with python 3.10). If not, download it for your operating system [here](https://www.python.org/downloads/).

2. (Optional) Create and activate a virtual environment
    This isn't strictly necessary but is good practice. You can skip this point.
   `python -m venv venv`
   
   Linux
   `source venv/bin/activate`
   Windows (cmd)
   `myenv\Scripts\activate`

3. With the environment now activated, install dependencies.
   `pip install -r requirements.txt`
   
4. Start the application
   `streamlit run app,py`


