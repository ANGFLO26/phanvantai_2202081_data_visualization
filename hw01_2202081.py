import tkinter as tk
from tkinter import messagebox
import random
from gtts import gTTS
from playsound import playsound
import tempfile
import os
from unidecode import unidecode


# Danh sách từ vựng
vocabulary = [
   ("Pink", "/pɪŋk/", "Màu hồng"),
   ("Red", "/red/", "Màu đỏ"),
   ("Green", "/ɡriːn/", "Màu xanh"),
   ("White", "/waɪt/", "Màu trắng"),
   ("Black", "/blæk/", "Màu đen"),
   ("Orange", "/ˈɒrɪndʒ/", "Màu cam"),
   ("Blue", "/bluː/", "Màu xanh da trời"),
   ("Purple", "/ˈpɜːpl/", "Màu tím"),
   ("Brown", "/braʊn/", "Màu nâu"),
   ("Gray", "/ɡreɪ/", "Màu xám"),
   ("Yellow", "/ˈjeləʊ/", "Màu vàng"),

]



class VocabularyApp:
   def __init__(self, root):
       self.root = root
       self.root.title("Learn English Vocabulary")
       self.root.geometry("700x500")


       self.root.configure(bg="#f5f5f5")


       # Shuffle vocabulary
       self.vocabulary = vocabulary.copy()
       random.shuffle(self.vocabulary)
       self.current_word = None
       self.current_phonetic = None
       self.current_meaning = None
       self.mode = None
       self.correct_count = 0
       self.wrong_count = 0


       # Khung chọn chế độ
       self.mode_frame = tk.Frame(root, bg="#f5f5f5")
       self.mode_frame.pack(expand=True)


       self.mode_label = tk.Label(self.mode_frame, text="MODE LEARNING ENGLISH", font=("Helvetica", 18, "bold"), bg="#f5f5f5")
       self.mode_label.pack(pady=20)


       self.mode_button_1 = tk.Button(self.mode_frame, text="Listen to English",
                                      font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=20, pady=10,
                                      command=lambda: self.start_learning(mode=1), width=40)
       self.mode_button_1.pack(pady=10)


       self.mode_button_2 = tk.Button(self.mode_frame, text="Listen to Vietnamese",
                                      font=("Helvetica", 14), bg="#2196F3", fg="white", padx=20, pady=10,
                                      command=lambda: self.start_learning(mode=2), width=40)
       self.mode_button_2.pack(pady=10)


       self.mode_button_3 = tk.Button(self.mode_frame, text="Phonetic look",
                                      font=("Helvetica", 14), bg="#FF5722", fg="white", padx=20, pady=10,
                                      command=lambda: self.start_learning(mode=3), width=40)
       self.mode_button_3.pack(pady=10)


       # Khung học tập
       self.learning_frame = tk.Frame(root, bg="#ffffff", relief="groove", bd=2)
       # Không đóng gói ngay lập tức, sẽ đóng gói khi cần


       # Thêm nút "Bắt đầu học"
       self.start_button = tk.Button(
       self.learning_frame,
       text="Start Learning",
       command=self.start_session,
       font=("Helvetica", 14, "bold"),  # Làm chữ đậm
       bg="#007BFF",  # Màu nền xanh dương đậm hơn
       fg="white",  # Màu chữ trắng
       activebackground="#0056b3",  # Màu nền khi nhấn
       activeforeground="white",  # Màu chữ khi nhấn
       bd=0,  # Loại bỏ đường viền
       relief="ridge",  # Hiệu ứng bo cạnh mềm mại
       padx=20,  # Khoảng cách ngang bên trong
       pady=10,  # Khoảng cách dọc bên trong
       width=30  # Chiều rộng của nút
   )
   # Đưa nút vào chính giữa
       self.start_button.place(relx=0.5, rely=0.5, anchor="center")






       # Khung hiển thị thông tin
       self.info_frame = tk.Frame(self.learning_frame, bg="#ffffff")
       # Chưa đóng gói, sẽ đóng gói khi "Bắt đầu học" được nhấn


       self.word_label = tk.Label(self.info_frame, text="", font=("Helvetica", 24), pady=10, bg="#ffffff", fg="#333")
       self.word_label.pack()


       self.repeat_button = tk.Button(self.info_frame, text="Listen again", command=self.repeat_audio, font=("Helvetica", 12),
                                      bg="#2196F3", fg="white", padx=20, pady=5)
       self.repeat_button.pack()


       # Khung nhập liệu
       self.input_frame = tk.Frame(self.learning_frame, bg="#f9f9f9", relief="groove", bd=2)
       # Chưa đóng gói, sẽ đóng gói khi "Bắt đầu học" được nhấn


       self.input_label_1 = tk.Label(self.input_frame, text="Enter English words:", font=("Helvetica", 14), bg="#f9f9f9", fg="#555")
       self.input_label_1.pack(anchor="w", pady=5)
       self.input_box_1 = tk.Entry(self.input_frame, font=("Helvetica", 14), justify="center", bd=2, relief="groove")
       self.input_box_1.pack(fill=tk.X, padx=10, pady=5, ipady=5)
       self.input_box_1.bind('<Return>', self.check_answer_event)


       self.input_label_2 = tk.Label(self.input_frame, text="Enter Vietnamese meaning:", font=("Helvetica", 14), bg="#f9f9f9", fg="#555")
       self.input_label_2.pack(anchor="w", pady=5)
       self.input_box_2 = tk.Entry(self.input_frame, font=("Helvetica", 14), justify="center", bd=2, relief="groove")
       self.input_box_2.pack(fill=tk.X, padx=10, pady=5, ipady=5)
       self.input_box_2.bind('<Return>', self.check_answer_event)


       self.check_button = tk.Button(self.input_frame, text="Check", command=self.check_answer, font=("Helvetica", 12),
                                      bg="#4CAF50", fg="white", padx=20, pady=5)
       self.check_button.pack(pady=10)


       self.result_label = tk.Label(self.input_frame, text="", font=("Helvetica", 14), bg="#f9f9f9", fg="#333")
       self.result_label.pack()


       # Khung điều khiển
       self.control_frame = tk.Frame(self.learning_frame, bg="#ffffff", relief="groove", bd=2)
       # Chưa đóng gói, sẽ đóng gói khi "Bắt đầu học" được nhấn


       self.answer_button = tk.Button(self.control_frame, text="See Answer", command=self.show_answer, font=("Helvetica", 12),
                                      bg="#FF9800", fg="white", padx=20, pady=5)
       self.answer_button.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)


       self.back_button = tk.Button(self.control_frame, text="Back to mode selection", command=self.back_to_mode, font=("Helvetica", 12),
                                    bg="#FF9800", fg="white", padx=20, pady=5)
       self.back_button.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)


       self.exit_button = tk.Button(self.control_frame, text="Exit", command=self.exit_program, font=("Helvetica", 12),
                                    bg="#F44336", fg="white", padx=20, pady=5)
       self.exit_button.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)


   def start_learning(self, mode):
       self.mode = mode
       self.mode_frame.pack_forget()
       self.learning_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
       # Hiển thị chỉ nút "Bắt đầu học"
       self.start_button.pack()
       # Ẩn các thành phần học tập khác nếu đã được hiển thị từ trước
       self.info_frame.pack_forget()
       self.input_frame.pack_forget()
       self.control_frame.pack_forget()
       self.result_label.config(text="")
       self.input_box_1.delete(0, tk.END)
       self.input_box_2.delete(0, tk.END)


   def start_session(self):
       # Khi nhấn "Bắt đầu học", ẩn nút này và hiển thị các thành phần học tập
       self.start_button.pack_forget()
       self.info_frame.pack(fill=tk.BOTH, pady=10)
       self.input_frame.pack(fill=tk.BOTH, padx=20, pady=10)
       self.control_frame.pack(fill=tk.X, padx=20, pady=10)
       self.result_label.config(text="")
       self.input_box_1.delete(0, tk.END)
       self.input_box_2.delete(0, tk.END)
       self.next_word()


   def play_audio(self, text, lang='en'):
       try:
           tts = gTTS(text=text, lang=lang)
           with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
               tts.save(temp_file.name)
               temp_path = temp_file.name
           playsound(temp_path)
       except Exception as e:
           messagebox.showerror("Error", f"No sound can be played: {e}")
       finally:
           if os.path.exists(temp_path):
               os.remove(temp_path)


   def repeat_audio(self):
       if self.mode in [1, 2]:
           text = self.current_word if self.mode == 1 else self.current_meaning
           lang = 'en' if self.mode == 1 else 'vi'
           self.play_audio(text, lang)


   def next_word(self):
       if self.vocabulary:
           self.current_word, self.current_phonetic, self.current_meaning = self.vocabulary.pop()
           if self.mode == 1:
               self.word_label.config(text="")
               self.repeat_button.pack()  # Hiển thị nút "Nghe lại"
               self.play_audio(self.current_word, 'en')
           elif self.mode == 2:
               self.word_label.config(text="")
               self.repeat_button.pack()  # Hiển thị nút "Nghe lại"
               self.play_audio(self.current_meaning, 'vi')
           elif self.mode == 3:
               self.word_label.config(text=self.current_phonetic)
               self.repeat_button.pack_forget()  # Ẩn nút "Nghe lại"
       else:
           response = messagebox.askyesno("Complete", "You have learned all the vocabulary! Do you want to learn it all over again?")
           if response:
               self.vocabulary = vocabulary.copy()
               random.shuffle(self.vocabulary)
               self.next_word()
           else:
               self.back_to_mode()


   def check_answer(self):
       user_word_input = unidecode(self.input_box_1.get().strip().lower())
       user_meaning_input = unidecode(self.input_box_2.get().strip().lower())
       correct_word = unidecode(self.current_word.strip().lower())
       correct_meaning = unidecode(self.current_meaning.strip().lower())


       feedback = []
       if user_word_input != correct_word:
           feedback.append(f"The correct English word is: {self.current_word}")
       if user_meaning_input != correct_meaning:
           feedback.append(f"The correct Vietnamese meaning is: {self.current_meaning}")


       if not feedback:
           self.result_label.config(text="✅ Exactly!", fg="green")
           self.input_box_1.delete(0, tk.END)
           self.input_box_2.delete(0, tk.END)
           self.next_word()
       else:
           self.result_label.config(text="❌ Wrong! " + " ".join(feedback), fg="red")


   def check_answer_event(self, event):
       self.check_answer()


   def show_answer(self):
       self.result_label.config(text=f"Answer: {self.current_word} - {self.current_meaning}", fg="blue")


   def back_to_mode(self):
       self.vocabulary = vocabulary.copy()
       random.shuffle(self.vocabulary)
       self.learning_frame.pack_forget()
       self.mode_frame.pack(expand=True)
       self.input_box_1.delete(0, tk.END)
       self.input_box_2.delete(0, tk.END)
       self.result_label.config(text="")
       # Ẩn các thành phần học tập khi quay lại chế độ
       self.info_frame.pack_forget()
       self.input_frame.pack_forget()
       self.control_frame.pack_forget()
       self.start_button.pack()


   def exit_program(self):
       self.root.quit()


# Chạy ứng dụng
if __name__ == "__main__":
   root = tk.Tk()
   app = VocabularyApp(root)
   root.mainloop()




