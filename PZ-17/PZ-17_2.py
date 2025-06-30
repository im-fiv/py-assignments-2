'''
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать 
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально 
приближенный к оригиналу
'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Event Registration Form')
root.geometry('620x540')
root.configure(bg='white')

header = tk.Label(
    root,
    text='EVENT REGISTRATION FORM', bg='black', fg='white',
    font=('Helvetica', 14, 'bold'),
    pady=12
)
header.pack(fill=tk.X)

form_frame = tk.Frame(root, bg='white', padx=30, pady=20)
form_frame.pack(fill=tk.BOTH, expand=True)

entry_opts = {
    'bg': 'white',
    'fg': 'black',
    'relief': tk.SOLID,
    'bd': 1,
    'font': ('Helvetica', 10)
}

tk.Label(
    form_frame,
    text='Name',
    anchor='w',
    bg='white',
    font=('Helvetica', 10, 'bold')
).grid(row=0, column=0, sticky='w', pady=8)
name_frame = tk.Frame(form_frame, bg='white')
name_frame.grid(row=0, column=1, columnspan=2, sticky='w', pady=8)

fname_entry = tk.Entry(name_frame, width=20, **entry_opts)
fname_entry.grid(row=0, column=0, padx=(0, 10))
lname_entry = tk.Entry(name_frame, width=20, **entry_opts)
lname_entry.grid(row=0, column=1)

tk.Label(
    form_frame,
    text='Company',
    anchor='w',
    bg='white',
    font=('Helvetica', 10, 'bold')
).grid(row=1, column=0, sticky='w', pady=8)
company_entry = tk.Entry(form_frame, width=45, **entry_opts)
company_entry.grid(row=1, column=1, columnspan=2, sticky='w')

tk.Label(
    form_frame,
    text='Email',
    anchor='w',
    bg='white',
    font=('Helvetica', 10, 'bold')
).grid(row=2, column=0, sticky='w', pady=8)
email_entry = tk.Entry(form_frame, width=45, **entry_opts)
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')

tk.Label(
    form_frame,
    text='Phone',
    anchor='w',
    bg='white',
    font=('Helvetica', 10, 'bold')
).grid(row=3, column=0, sticky='w', pady=8)
area_entry = tk.Entry(form_frame, width=8, **entry_opts)
area_entry.grid(row=3, column=1, sticky='w')
phone_entry = tk.Entry(form_frame, width=30, **entry_opts)
phone_entry.grid(row=3, column=2, sticky='w', padx=(10, 0))

tk.Label(
    form_frame,
    text='Subject',
    anchor='w',
    bg='white',
    font=('Helvetica', 10, 'bold')
).grid(row=4, column=0, sticky='w', pady=8)
subject_var = tk.StringVar()
subject_dropdown = ttk.Combobox(form_frame, textvariable=subject_var, width=42, state='readonly')
subject_dropdown['values'] = ('Choose option', 'Product Inquiry', 'Support', 'Feedback')
subject_dropdown.current(0)
subject_dropdown.grid(row=4, column=1, columnspan=2, sticky='w')

tk.Label(
    form_frame,
    text='Are you an existing customer?',
    bg='white',
    font=('Helvetica', 10, 'bold')
).grid(row=5, column=0, columnspan=3, sticky='w', pady=(20, 5))
is_customer_var = tk.StringVar(value='Yes')
radio_frame = tk.Frame(form_frame, bg='white')
radio_frame.grid(row=6, column=0, columnspan=3, sticky='w')
tk.Radiobutton(
    radio_frame,
    text='Yes',
    variable=is_customer_var,
    value='Yes',
    bg='white'
).pack(side='left', padx=(0, 10))
tk.Radiobutton(
    radio_frame,
    text='No',
    variable=is_customer_var,
    value='No',
    bg='white'
).pack(side='left')

def register():
    print('Form submitted!')

btn_frame = tk.Frame(root, bg='white')
btn_frame.pack(fill=tk.X, padx=30, pady=10)

register_btn = tk.Button(
    btn_frame,
    text='REGISTER',
    bg='#f44336',
    fg='white',
    font=('Helvetica', 10, 'bold'),
    padx=20,
    pady=10,
    command=register
)
register_btn.pack(side='left', anchor='w')

root.mainloop()