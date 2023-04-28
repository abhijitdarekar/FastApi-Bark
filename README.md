
# TTS with Bark🐶 and FastApi

The project is pulled from the official project Repository [Bark 🐶](https://github.com/suno-ai/bark).


It takes text from the user as input and converts it to a speech and responds with link to audio_file.wav. It is built in fastApi , it has two parameters. data and language. (Please refer net section for api references.)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhijitdarekar/)




## Installation

git clone the project the URL : [FastApi-Bark](https://github.com/JeetDarekar001/FastApi-Bark)

```bash
  git clone https://github.com/JeetDarekar001/FastApi-Bark.git
```

Create a new python envorienment and install the depedencies.
Run the below commands.
```
python -m venv barkenv
.\barkenv\Scripts\activate
cd FastApi-Bark
pip install -r app/requirements.txt
```
This project required GPU to work faster, on the CPU envorienments it takes time.

After Installation, run the below command, form ```FastApi-Bark``` directory.
```
uvicorn app.app:app --reload
```

Open your brwoser and load the link ```http://127.0.0.1:8000```, you should see the below output.

```{"Message":"Yeahh!! Server is Online."}```

Finally its done.💫

## API Reference

#### Root

```http
  GET /
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None` | `None` | Points to the root of the serever. Display's message “Yeahh!! Server is Online." |

#### Api Root

```http
  GET /api/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `None`      | `None` | Root of api endpoint. Displays Message "Welcome to Text to Speech Conversion with Bark." |

#### Test to speech Conversion

```http
    POST /api/text_to_speech/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `data`      | `str` | text that should be converted to speech. Input should not be empty however it responses with error code 422 if input is null or less then 5 character. |
|`language`|`str`| Output langugae of the speech. [Bark](https://github.com/suno-ai/bark) supports multiple languages, some are Hindi, English, Spanish, Italian, Chinese etc. Please Refer to the documnetation for more details. Do not provide additional languahe that is not present in [ Bark documnetation](https://github.com/suno-ai/bark#%EF%B8%8F-details). |



### API responses

Api reposnse on successfully converting text to speech is as follows.

```
{
  "speech": {
    "path": "./app/Audio_files/Audio_2023-04-28_21-29-17.wav",
    "status_code": 200,
    "filename": "speech.mp3",
    "send_header_only": false,
    "media_type": "audio/mpeg",
    "background": null,
    "raw_headers": [
      [
        "content-type",
        "audio/mpeg"
      ],
      [
        "content-disposition",
        "attachment; filename=\"speech.mp3\""
      ]
    ],
    "_headers": {
      "content-type": "audio/mpeg",
      "content-disposition": "attachment; filename=\"speech.mp3\""
    },
    "stat_result": null
  },
  "data": "Welcome to London!!"
}

```