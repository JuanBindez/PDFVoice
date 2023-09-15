
import PyPDF2
from gtts import gTTS
import os

from src.extract_text_from_pdf import extract_text_from_pdf
from src.text_to_audio import text_to_audio


def main():
    pdf_path = str(input("PDF name ->"))
    extracted_text = extract_text_from_pdf(pdf_path)

    output_audio_path = pdf_path + ".mp3"
    text_to_audio(extracted_text, output_audio_path)

    print("Áudio gerado com sucesso!")
    print("Aviso: O áudio foi criado e está pronto para ser reproduzido.")

if __name__ == "__main__":
    main()




