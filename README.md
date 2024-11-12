<h3 align="center">
  <img height="30%" width="30%" src="https://github.com/vondas-network/illogica-factory/blob/main/img/illogica-factory-logo.png"/>
</h3>

<p align="center"><em>Automate Creation of YouTube Shorts using AI feedback loops</em></p> 

## What does this do?

<h3 align="center">
  <img height="60%" width="60%" src="https://github.com/vondas-network/illogica-factory/blob/main/img/illogica-factory-diagram.jpg"/>
</h3>

## Setup 

`illogica-factory` requires [Python 3.11](https://www.python.org/downloads/) to run effectively.

### Install the project requirements
``` bash
git clone git@github.com:vondas-network/illogica-factory.git
cd illogica-factory
pip install -r requirements.txt
```

### Create Python virtual environment
In a nutshell, Python virtual environments help decouple and isolate Python installs and associated pip packages. This allows end-users to install and manage their own set of packages that are independent of those provided by the system or used by other projects.
```bash
python3 -m venv env
```

### Activate Python virtual environment
This will activate your virtual environment. Immediately, you will notice that your terminal path includes env, signifying an activated virtual environment.
``` bash
source env/bin/activate
```

After you finished installing Python, you can install `illogica-factory` by following the steps below:

### Create .env file
See [`.env.example`](.env.example) for the required environment variables. Once you've added all the necessary data, name the file _.env_

``` bash
# See EnvironmentVariables.md for more information.

# Necessary API Keys
# -------------------

# TikTok Session ID
# Obtain your session ID by logging into TikTok and copying the sessionid cookie.
TIKTOK_SESSION_ID=""

# ImageMagick Binary Path
# Download ImageMagick from https://imagemagick.org/script/download.php
IMAGEMAGICK_BINARY=""

# Pexels API Key
# Register at https://www.pexels.com/api/ to get your API key.
PEXELS_API_KEY=""

# Optional API Keys
# -----------------

# OpenAI API Key
# Visit https://openai.com/api/ for details on obtaining an API key.
OPENAI_API_KEY=""

# Cohere API Key
# Visit https://docs.cohere.com/ for details on obtaining an API key.
COHERE_API_KEY=""

# AssemblyAI API Key
# Sign up at https://www.assemblyai.com/ to receive an API key.
ASSEMBLY_AI_API_KEY=""

# Google API Key
# Generate your API key through https://makersuite.google.com/app/apikey
GOOGLE_API_KEY=""

```
### Run the project

``` bash
cd Backend
python main.py
```

## Music 

To use your own music, compress all your MP3 Files into a ZIP file and upload it somewhere. Provide the link to the ZIP file in the Frontend.

It is recommended to use Services such as [Filebin](https://filebin.net) to upload your ZIP file. If you decide to use Filebin, provide the Frontend with the absolute path to the ZIP file by using More -> Download File, e.g. (use this [Popular TT songs ZIP](https://filebin.net/klylrens0uk2pnrg/drive-download-20240209T180019Z-001.zip), not this [Popular TT songs](https://filebin.net/2avx134kdibc4c3q))

You can also just move your MP3 files into the `Songs` folder.

## Fonts 

Add your fonts to the `fonts/` folder, and load them by specifying the font name on line `124` in `Backend/video.py`.

If you were not able to find your solution, please ask in the discord or create a new issue, so that the community can help you.

## Where can I find this stuff?

- [YouTube](https://www.youtube.com/@schwwaaa)
- [Instagram](https://www.instagram.com/schwwaaa/)

Schwwaaa, the pioneering global conglomerate, leads the charge in providing innovative corporate solutions designed to address everyday challenges and shape a brighter future. With a commitment to excellence and efficiency, Schwwaaa empowers businesses and communities alike to thrive in an ever-evolving world. Through its visionary leadership and cutting-edge technologies, Schwwaaa exemplifies the transformative potential of corporate ingenuity in creating a better tomorrow for all.

## Notes 
* The project is a forked enhancement of [Money Printer](https://github.com/FujiwaraChoki/MoneyPrinter/)

## FAQ

## How do I get the TikTok session ID?

You can obtain your TikTok session ID by logging into TikTok in your browser and copying the value of the `sessionid` cookie.

## My ImageMagick binary is not being detected

Make sure you set your path to the ImageMagick binary correctly in the `.env` file, it should look something like this:

```env
IMAGEMAGICK_BINARY="C:\\Program Files\\ImageMagick-7.1.0-Q16\\magick.exe"
```

Don't forget to use double backslashes (`\\`) in the path, instead of one.

### I can't install `playsound`: Wheel failed to build

If you're having trouble installing `playsound`, you can try installing it using the following command:

```bash
pip install -U wheel
pip install -U playsound
```