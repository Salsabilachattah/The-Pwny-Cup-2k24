import wave
sound = wave.open("sound.wav", mode='rb')
frame_bytes = bytearray(list(sound.readframes(sound.getnframes())))
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
LAST = string.split("#")
#print("flag : " + string)
print("flag : " + LAST[0])
sound.close()
