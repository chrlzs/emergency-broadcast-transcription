# Emergency Broadcast Transcription

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)


## Description
The Emergency Broadcast Transcription project aims to capture public emergency broadcasts from local paramedic and fire channels, convert the voice broadcast to text using speech-to-text technology, and provide the transcribed text as a web service for other applications to consume. This project leverages the EPC-R3720 NXP i.MX8MPlus Cortex-A53 Edge AI Box Computer for efficient edge computing.

## Features
- **Audio Capture**: Capture emergency broadcasts using a Software Defined Radio (SDR) receiver.
- **Speech-to-Text**: Convert the captured audio to text using speech recognition technology.
- **Web Service**: Serve the transcribed text via a RESTful API.
- **Real-time Processing**: Process and provide transcriptions in near real-time.

## Project Structure
```
emergency-broadcast-transcription/
├── src/
│   ├── audio_capture.py
│   ├── transcribe.py
│   └── web_server.py
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites
- **Hardware**: EPC-R3720 NXP i.MX8MPlus Cortex-A53 Edge AI Box Computer, SDR receiver.
- **Software**: Python 3.x, Git, `rtl_fm`, `sox`.

### Installation Steps
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/YOUR_USERNAME/emergency-broadcast-transcription.git
    cd emergency-broadcast-transcription
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up the Database**:
    ```python
    import sqlite3

    conn = sqlite3.connect('transcriptions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE transcriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    ```

## Usage

### Capturing Audio
Run the audio capture script to start capturing emergency broadcasts:
```sh
python src/audio_capture.py
```

### Transcribing Audio
Transcribe the captured audio file:
```sh
python src/transcribe.py
```

### Running the Web Server
Start the Flask web server to serve the transcriptions:
```sh
python src/web_server.py
```

### API Endpoints
- **GET /transcriptions**: Retrieve the latest transcriptions.
- **POST /transcriptions**: (Internal use) Add new transcriptions to the database.

### Example Requests
- **Retrieve Transcriptions**:
    ```sh
    curl -X GET http://localhost:5000/transcriptions
    ```

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Inspired by the need for efficient and accessible emergency broadcast information.
- Utilizes open-source tools and libraries such as Flask and SpeechRecognition.

## Troubleshooting
- Ensure that the SDR receiver is properly connected and configured.
- Verify that the necessary software dependencies are installed.
- Check the Flask server logs for any errors.

## Contact
For questions or support, please open an issue on this repository or contact me at [your email address].
