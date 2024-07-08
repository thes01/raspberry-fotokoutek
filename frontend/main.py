import os
import random
# import time
from tkinter import Tk, Label
from PIL import Image, ImageTk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app

    def on_created(self, event):
        self.app.new_image = event.src_path

class App:
    def __init__(self, root, folder):
        self.root = root
        self.folder = folder
        self.new_image = None
        self.image_files = os.listdir(folder)
        random.shuffle(self.image_files)
        self.image_label = Label(root)
        self.image_label.pack()
        self.display_next_image()

    def display_next_image(self):
        if self.new_image:
            image_file = self.new_image
            self.new_image = None
        else:
            if not self.image_files:
                self.image_files = os.listdir(self.folder)
                random.shuffle(self.image_files)
            image_file = os.path.join(self.folder, self.image_files.pop())
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        self.root.after(5000, self.display_next_image)  # change to desired time in ms

if __name__ == "__main__":
    folder = "pictures"  # change to your folder
    root = Tk()
    root.attributes('-fullscreen', True)
    app = App(root, folder)
    event_handler = MyHandler(app)
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=False)
    observer.start()
    root.mainloop()
    observer.stop()
    observer.join()