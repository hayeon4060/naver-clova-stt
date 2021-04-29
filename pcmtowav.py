import wave
import glob
import os

input_path = './KsponSpeech_0001'
output_path = 'wav'
LENGTH = 1000
channels=1
bit_depth=16
sampling_rate=16000

for i in range(0, LENGTH):
    for input_file in glob.glob(os.path.join(input_path, 'KsponSpeech_00{0:04d}'.format(i+1)+str(".pcm"))):
        with open(input_file, 'rb') as opened_pcm_file:
            pcm_data = opened_pcm_file.read()
            wav_file = str('KsponSpeech_00{0:04d}'.format(i+1))+str(".wav")

            obj2write = wave.open( output_path+"/"+wav_file, 'wb')
            obj2write.setnchannels( channels )
            obj2write.setsampwidth( bit_depth // 8 )
            obj2write.setframerate( sampling_rate )
            obj2write.writeframes( pcm_data )
            obj2write.close()