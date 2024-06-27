import json, os

file_name = './texts/example.txt'
file = open(file_name)
text = file.read()
file.close()
words = text.split()

translation_file_name = './texts/example-translation.json'
if os.path.exists(translation_file_name):
  file = open(translation_file_name, 'r')
  translation = file.read()
  file.close()
  translation = json.loads(translation)
else:
  translation = {}

print("Translate words into your language. To stop translating, type q. To see translated text, type p.")
for word in words:  
    if word not in translation: 
      cmd = input("Translation for " + word + ": ")
      if(cmd == "q"):
        break
      elif(cmd == "p"):
        print(" ".join(str(value) for value in translation.values()))
        continue
      translation[word] = cmd
      file = open(translation_file_name, 'w')
      file.write(json.dumps(translation))  
      file.close()



