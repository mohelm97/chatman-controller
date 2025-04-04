import tkinter as tk
from tkinter import ttk, messagebox
from chatman_controller import ChatmanController, EyeMovement, HandMovement, AntennaMovement

class CheckboxGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatman Controller")
        self.root.resizable(False, False)

        try:
            self.controller = ChatmanController()
        except Exception as e:
            messagebox.showerror("Initialization Error", f"Failed to connect to Chatman:\n{e}")
            self.root.destroy()
            return

        main_frame = ttk.Frame(root, padding=10)
        main_frame.grid()

        # LED Grid Frame
        grid_frame = ttk.LabelFrame(main_frame, text="LED Matrix", padding=10)
        grid_frame.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        self.checkboxes = [[tk.IntVar() for _ in range(8)] for _ in range(3)]

        for i in range(3):
            for j in range(8):
                cb = ttk.Checkbutton(
                    grid_frame,
                    variable=self.checkboxes[i][j],
                    command=self.generate_hex,
                    takefocus=False
                )
                cb.grid(row=2 - i, column=j, padx=2, pady=2)

        # Output inside grid frame
        ttk.Label(grid_frame, text="Hex Output:").grid(row=3, column=0, columnspan=2, sticky="w", pady=(8, 0))
        self.output_text = ttk.Entry(grid_frame, width=30, font=("Courier", 10))
        self.output_text.grid(row=3, column=2, columnspan=6, pady=(8, 0), sticky="e")

        # Movement Controls
        movement_frame = ttk.LabelFrame(main_frame, text="Movements", padding=10)
        movement_frame.grid(row=1, column=0, columnspan=3, pady=(0, 10), sticky="ew")

        self.eye_combobox = ttk.Combobox(
            movement_frame,
            values=[e.name for e in EyeMovement],
            state="readonly",
            width=18
        )
        self.eye_combobox.set(EyeMovement.NO_MOVEMENT.name)
        self.eye_combobox.grid(row=0, column=0, padx=5, pady=5)

        self.hand_combobox = ttk.Combobox(
            movement_frame,
            values=[e.name for e in HandMovement],
            state="readonly",
            width=18
        )
        self.hand_combobox.set(HandMovement.NO_MOVEMENT.name)
        self.hand_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.antenna_combobox = ttk.Combobox(
            movement_frame,
            values=[e.name for e in AntennaMovement],
            state="readonly",
            width=18
        )
        self.antenna_combobox.set(AntennaMovement.NO_MOVEMENT.name)
        self.antenna_combobox.grid(row=0, column=2, padx=5, pady=5)

        self.eye_combobox.bind("<<ComboboxSelected>>", self.generate_hex)
        self.hand_combobox.bind("<<ComboboxSelected>>", self.generate_hex)
        self.antenna_combobox.bind("<<ComboboxSelected>>", self.generate_hex)

    def generate_hex(self, _=None):
        hex_values = []
        hex_values_string = []

        for row in self.checkboxes:
            byte_value = 0
            for j, checkbox in enumerate(row):
                byte_value |= checkbox.get() << j
            hex_values.append(byte_value)
            hex_values_string.append(f"{byte_value:02X}")

        try:
            eye_movement = EyeMovement[self.eye_combobox.get()]
            hand_movement = HandMovement[self.hand_combobox.get()]
            antenna_movement = AntennaMovement[self.antenna_combobox.get()]
        except KeyError:
            messagebox.showerror("Selection Error", "Invalid movement selected.")
            return

        self.controller.move(eye_movement, hand_movement, antenna_movement, hex_values)

        self.output_text.delete(0, tk.END)
        self.output_text.insert(tk.END, " ".join(hex_values_string))

if __name__ == "__main__":
    root = tk.Tk()
    app = CheckboxGridApp(root)
    root.mainloop()
