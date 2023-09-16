import tkinter as tk

class CustomSpinBox(tk.Frame):
    def __init__(self, master=None, label_text="", sum_var=None):
        super().__init__(master, borderwidth=1, relief="solid")
        self.value = tk.IntVar()
        self.sum_var = sum_var
        
        # Create the label
        self.label = tk.Label(self, text=label_text)
        self.label.grid(row=0, column=0)

        # Create the decrement button
        self.decrement_button = tk.Button(self, text="-", command=self.decrement)
        self.decrement_button.grid(row=0, column=1)
        
        # Create the entry field for the value
        self.value_entry = tk.Entry(self, textvariable=self.value, width=5, state="readonly")
        self.value_entry.grid(row=0, column=2)
        
        # Create the increment button
        self.increment_button = tk.Button(self, text="+", command=self.increment)
        self.increment_button.grid(row=0, column=3)
        
        self.max_value = 20  # Maximum value allowed

    def increment(self):
        current_value = self.value.get()
        if current_value < self.max_value:
            self.value.set(current_value + 1)
            self.sum_var.set(self.sum_var.get() + 1)  # Update the sum_var
            self.update_button_states()

    def decrement(self):
        current_value = self.value.get()
        if current_value > 0:
            self.value.set(current_value - 1)
            self.sum_var.set(self.sum_var.get() - 1)  # Update the sum_var
            self.update_button_states()

    def update_button_states(self):
        current_value = self.value.get()
        self.decrement_button.config(state="normal" if current_value > 0 else "disabled")
        self.increment_button.config(state="normal" if current_value < self.max_value and self.sum_var.get() < 20 else "disabled")

def update_sum():
    total = sum([spin_box.value.get() for spin_box in spin_boxes])
    sum_var.set(total)  # Update the sum_var
    sum_entry.delete(0, tk.END)
    sum_entry.insert(0, total)
    for spin_box in spin_boxes:
        spin_box.update_button_states()  # Update button states for all spin boxes

def show_previous():
    global current_index
    if current_index >= 5:
        current_index -= 5
        update_spin_boxes_visibility()
        update_range_label()

def show_next():
    global current_index
    if current_index + 5 < len(spin_boxes):
        current_index += 5
        update_spin_boxes_visibility()
        update_range_label()

def update_spin_boxes_visibility():
    for i, spin_box in enumerate(spin_boxes):
        if current_index <= i < current_index + 5:
            spin_box.grid(row=i - current_index, column=0, padx=10, pady=20)
            spin_box.value.trace_add("write", lambda *args, box=spin_box: update_sum())
        else:
            spin_box.grid_forget()

def update_range_label():
    range_label.config(text=f"Displaying Boxes {current_index + 1} to {min(current_index + 5, len(spin_boxes))} of {len(spin_boxes)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Spin Box App")
    root.geometry("400x600")

    # Create a frame to hold the spin boxes
    spin_box_frame = tk.Frame(root)
    spin_box_frame.pack()

    sum_var = tk.IntVar()
    sum_var.set(0)  # Initialize the sum_var to 0

    spin_box1 = CustomSpinBox(spin_box_frame, label_text="Spin Box 1:", sum_var=sum_var)
    spin_box2 = CustomSpinBox(spin_box_frame, label_text="Spin Box 2:", sum_var=sum_var)
    spin_box3 = CustomSpinBox(spin_box_frame, label_text="Spin Box 3:", sum_var=sum_var)
    spin_box4 = CustomSpinBox(spin_box_frame, label_text="Spin Box 4:", sum_var=sum_var)
    spin_box5 = CustomSpinBox(spin_box_frame, label_text="Spin Box 5:", sum_var=sum_var)
    spin_box6 = CustomSpinBox(spin_box_frame, label_text="Spin Box 6:", sum_var=sum_var)
    spin_box7 = CustomSpinBox(spin_box_frame, label_text="Spin Box 7:", sum_var=sum_var)
    spin_box8 = CustomSpinBox(spin_box_frame, label_text="Spin Box 8:", sum_var=sum_var)
    spin_box9 = CustomSpinBox(spin_box_frame, label_text="Spin Box 9:", sum_var=sum_var)
    spin_box10 = CustomSpinBox(spin_box_frame, label_text="Spin Box 10:", sum_var=sum_var)

#    spin_boxes = [spin_box1, spin_box2, spin_box3, spin_box4, spin_box5, spin_box6, spin_box7, spin_box8, spin_box9, spin_box10]
    spin_boxes = [spin_box1, spin_box2, spin_box3]
    current_index = 0  # Current index to keep track of the displayed spin boxes

    # Create buttons to show previous and next spin boxes
    prev_button = tk.Button(root, text="Previous", command=show_previous)
    prev_button.pack()
    next_button = tk.Button(root, text="Next", command=show_next)
    next_button.pack()

    # Create a label to display the current range
    range_label = tk.Label(root, text="", pady=10)
    range_label.pack()

    # Initially, show the first 5 spin boxes and update the range label
    update_spin_boxes_visibility()
    update_range_label()

    # Create an entry box to display the sum
    sum_entry = tk.Entry(root, width=10)
    sum_entry.pack(pady=10)
    sum_entry.config(state="readonly")  # Set the sum_entry to readonly

    root.mainloop()
