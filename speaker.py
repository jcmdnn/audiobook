import pyttsx3
import pdfplumber

# inicializando a engine de NLP
engine = pyttsx3.init()
# lendo o arquivo pdf
pdf = pdfplumber.open('O elefante em apuros.pdf')
# gerando uma lista de páginas a serem lidas
paginas = pdf.pages[2:-3]

texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()

texto_livro_final = texto_livro.replace('.', '. ').replace(',', ', ').replace('!', '! ').replace('?', '? ')

engine.save_to_file(texto_livro_final, 'speaker.mp3')
engine.runAndWait()
