from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import os


os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"
"""
git clone https://github.com/suno-ai/bark
python bark/setup.py install
"""

# download and load all models
preload_models(
    text_use_gpu=True,  # Set to False for CPU-only
    text_use_small=False,
    coarse_use_gpu=True,  # Set to False for CPU-only
    coarse_use_small=False,
    fine_use_gpu=True,  # Set to False for CPU-only
    fine_use_small=False,
    codec_use_gpu=True,  # Set to False for CPU-only
    force_reload=False
)

def tts(text_input, voice_name = 'en_speaker_2'):
    received_text = text_input
    print("Received text:", received_text)
    audio_file = generate_audio(received_text, history_prompt=voice_name )
    
    file_name = "/kaggle/working/AI-avatar-generator/src/audio.wav"
    try:
        os.remove(file_name)
    except OSError:
        pass

    try:
        write_wav(file_name, SAMPLE_RATE, audio_file)
        return True
    except OSError:
        return False


if __name__ == '__main__':
    text = "I have to make my decision since it involves Production settings later. Beside, I have invested 50K USD in GPU and servers that are idle because of just routing issues"
    voice_name = "en_speaker_2"
    print(text)
    tts(text, voice_name)