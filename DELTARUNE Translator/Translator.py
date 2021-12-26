from deep_translator import GoogleTranslator
import json

file = open("lang_en_ch1.json").read()
data = json.loads(file)

for key, value in data.items():
    print(f"KEY: {key}, VALUE: {value}")
    try:
        translated = GoogleTranslator(source='auto', target="pt").translate(value)
        print("Valores Traduzidos.")
        
        data[key] = translated

        with open("lang_en_ch1.json","w") as outfile:
            json.dump(data,outfile,indent=4)
            outfile.close()

        print("Valor aplicado")

    except Exception as e:
        print(e)
        continue