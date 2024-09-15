import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Điều chỉnh độ nhạy micro
        recognizer.adjust_for_ambient_noise(source)
        try:
            # Yêu cầu người dùng nói
            messagebox.showinfo("Nhận diện giọng nói", "Hãy bắt đầu nói...")
            audio = recognizer.listen(source, timeout=5)
            
            text = recognizer.recognize_google(audio, language="vi-VN")
            text_box.delete(1.0, tk.END) 
            text_box.insert(tk.END, text)  
        except sr.UnknownValueError:
            messagebox.showerror("Lỗi", "Không thể nhận diện giọng nói")
        except sr.RequestError as e:
            messagebox.showerror("Lỗi", f"Yêu cầu gặp lỗi; {e}")
        except sr.WaitTimeoutError:
            messagebox.showerror("Lỗi", "Hết thời gian chờ, vui lòng thử lại.")

root = tk.Tk()
root.title("Nhận Diện Giọng Nói Tiếng Việt")

mic_button = tk.Button(root, text="🎤 Nhấn để nói", font=("Arial", 14), command=recognize_speech)
mic_button.pack(pady=20)

text_box = tk.Text(root, font=("Arial", 14), height=10, width=50)
text_box.pack(pady=20)

root.mainloop()
