import tkinter as tk

MILE_TO_KM_RATE = 1.60934
FONT = ('Arial', 12)


def main():
    window = tk.Tk()
    window.config(width=300, height=100)
    window.config(padx=30, pady=30)
    window.title('Miles to KM Converter')

    # Equal to Label
    lbl_equal = tk.Label(text='is equal to', font=FONT)
    lbl_equal.grid(column=0, row=1)

    # Input Entry
    ent_input = tk.Entry(width=7)
    ent_input.focus()
    ent_input.grid(column=1, row=0)

    # Output Label
    lbl_output = tk.Label(text='0', font=FONT)
    lbl_output.grid(column=1, row=1)

    # Input unit Label
    lbl_unit_input = tk.Label(text='Miles', font=FONT)
    lbl_unit_input.grid(column=2, row=0)

    # Output unit Label
    lbl_unit_output = tk.Label(text='Km', font=FONT)
    lbl_unit_output.grid(column=2, row=1)

    def convert():
        result = round(float(ent_input.get()) * MILE_TO_KM_RATE, 2)
        lbl_output.config(text=f'{result}')
        return result

    # Button
    btn_calc = tk.Button(text='Calculate', command=convert)
    btn_calc.grid(column=1, row=2)

    window.mainloop()


if __name__ == '__main__':
    main()
