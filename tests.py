from pocketsphinx import LiveSpeech

# Test PocketSphinx recognition with live speech input
print("Testing PocketSphinx...")
speech = LiveSpeech()
for phrase in speech:
    print(phrase)

