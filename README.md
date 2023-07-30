# Text to MP3 Converter

This Python script allows you to convert text from a TXT file to an MP3 audio file using the Google Text-to-Speech (gTTS) library. It provides a simple graphical user interface (GUI) using the `tkinter.filedialog` module to select the input TXT file. The converted MP3 audio will be saved as `output.mp3` in the same directory as the script.

## Requirements

- Python 3.x
- gTTS library

To install the required library, you can use pip:

```
pip install gtts
```

## How to Use

1. Make sure you have Python 3.x installed on your system.

2. Install the required gTTS library by running the command mentioned above.

3. Clone or download this repository to your local machine.

4. Place the TXT file containing the text you want to convert to MP3 in the same directory as the script.

5. Run the Python script `txt_to_mp3.py`:

```
python txt_to_mp3.py
```

6. A graphical file dialog will open up, allowing you to choose the input TXT file.

7. After selecting the file, the script will read its contents, convert it to an MP3 file using the specified language (English by default), and save it as `output.mp3` in the same directory.

8. Once the conversion is complete, the MP3 file will automatically open and start playing.

## Note

- The script is set to use the English language for text-to-speech conversion by default. If you want to use a different language, you can modify the `language` variable in the script. Refer to the [gTTS documentation](https://gtts.readthedocs.io/en/latest/langs.html) for language codes.

- Please ensure that the TXT file contains valid text content, and the file's encoding should be compatible with the Python script.

- For large files or slower systems, the text-to-speech conversion may take some time. Be patient until the conversion process is complete.

## Disclaimer

This script utilizes the Google Text-to-Speech (gTTS) service, which is subject to its terms of service and usage limitations. Please review the [gTTS terms of service](https://cloud.google.com/text-to-speech/docs/data-usage-and-pricing) to ensure compliance with their policies before using this script.

**Use the script responsibly and respect the terms of service of the external services you are using.**

---

Feel free to contribute to this project by creating pull requests or submitting issues if you encounter any problems or have suggestions for improvements. Happy coding!
