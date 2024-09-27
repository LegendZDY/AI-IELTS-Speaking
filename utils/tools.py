from pydub import AudioSegment
import json

def model_message_get(model_config_path):
    with open(model_config_path, 'r') as f:
        model_messages = json.load(f)
    return model_messages

def wav_to_pcm(wav_file, pcm_file):
    # 加载 WAV 文件
    audio = AudioSegment.from_wav(wav_file)
    audio = audio.set_channels(1).set_sample_width(2).set_frame_rate(16000)
    # 导出为 PCM 格式
    audio.export(pcm_file, format="s16le")  # s16le 表示 16 位小端 PCM 格式

