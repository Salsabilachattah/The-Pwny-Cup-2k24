import numpy as np
from pydub import AudioSegment
from scipy.io.wavfile import write

# Frequencies for DTMF tones (Dual-tone multi-frequency)
DTMF_FREQS = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477), 'A': (697, 1633),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477), 'B': (770, 1633),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477), 'C': (852, 1633),
    '*': (941, 1209), '0': (941, 1336), '#': (941, 1477), 'D': (941, 1633)
}

def generate_sine_wave(frequency, duration_ms, sample_rate=44100, amplitude=0.5):
    """ Generate a sine wave at a specific frequency and duration. """
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * duration_ms / 1000), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave

def generate_dtmf_tone(digit, duration_ms=300, sample_rate=44100):
    """ Generate a DTMF tone for a given digit by combining two sine waves. """
    if digit not in DTMF_FREQS:
        raise ValueError(f"Invalid DTMF digit: {digit}")
    
    freq1, freq2 = DTMF_FREQS[digit]
    tone1 = generate_sine_wave(freq1, duration_ms, sample_rate)
    tone2 = generate_sine_wave(freq2, duration_ms, sample_rate)
    
    # Combine the two tones by adding them together
    combined_tone = tone1 + tone2
    combined_tone *= (2**15 - 1) / np.max(np.abs(combined_tone))  # Normalize to 16-bit range
    return combined_tone.astype(np.int16)

def create_dtmf_sequence(sequence, output_file="dtmf_sequence.wav", gap_duration_ms=100, sample_rate=44100):
    """ Create a sequence of DTMF tones and export as a WAV file. """
    audio_data = []

    for digit in sequence:
        if digit == ' ':
            # Insert a gap between sequences (silence)
            audio_data.append(np.zeros(int(sample_rate * gap_duration_ms / 1000), dtype=np.int16))
        else:
            # Generate DTMF tone for the digit
            tone = generate_dtmf_tone(digit, sample_rate=sample_rate)
            audio_data.append(tone)
        
        # Add a gap after each tone
        audio_data.append(np.zeros(int(sample_rate * gap_duration_ms / 1000), dtype=np.int16))

    # Concatenate the array of tones and silence
    audio_data = np.concatenate(audio_data)
    
    # Save the audio data as a WAV file
    write(output_file, sample_rate, audio_data)
    print(f"DTMF sequence saved as {output_file}")

if __name__ == "__main__":
    # Example: Create a DTMF sequence for the flag
    dtmf_sequence = '706C6561736547657443686970735769746855'
    create_dtmf_sequence(dtmf_sequence, "dtmf_flag_challenge.wav")
