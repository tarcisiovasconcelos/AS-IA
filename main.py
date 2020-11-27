from analise_sentimentos import AnaliseSentimentos

analise = AnaliseSentimentos()

print("Comentários legais são bem vistos pela comunidade")
print("comentários recomendados |Eu gostei.!|Eu odiei.!|Eu visitei.!")

txt = input("Deixe um comentário...")

resultado = analise.avalia(txt)

if resultado['score'] > 0 :
	print("Frase Positiva, Good Vibes")

if resultado['score'] == 0 :
	print("Frase Neutra")

if resultado['score'] < 0 :
	print("Frase Negativa, Melhore")

