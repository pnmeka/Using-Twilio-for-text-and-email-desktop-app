#text message app and email desktop app
import tkinter as tk
from tkinter import *
import twilio
import webbrowser
from twilio.rest import Client

#define sending a message
# Account SID and Auth Token at twilio.com/console and set Twilio variables
def send_message():
    phone=ent_phone.get()
    message=ent_message.get()
    account_sid = 'Enter account SID'
    auth_token = 'Enter your token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                     body=str(message),
                     from_='+1<Number from twilio>',
                     to=int(phone)
                 )
    #creat new window on success
    new_win=Toplevel(window)
    new_win.title("SUCCESS")
    new_win.configure(bg="light green")
    Label(new_win, text=message.sid, bg="light green").pack(pady=15)
    new_win.after(1000, lambda:new_win.destroy())

#define clear button
def clear_text():
   ent_phone.delete(2, END)
   ent_message.delete(0, END)
   ent_message.insert(0, "Twilio here: We anticipate the team will call you during rounds. The team will tentatively round between *** am.  Text M for more information and STOP to stop receiving messages.")

#define email RC
def mail_to():
    webbrowser.open("mailto:?subject=Patient representative wishes to be called during rounds&body=Dear RC and Dr ***,\n\nThe following patient representative wishes to be called daily during rounds.\n\n\nPatient Identifier: \nRepresentative:\nTime slot: \ntel:*67***\n\n\n Please note: \n\n1. Use the one-click-anonymized-call-format to call the patient. (it is preformatted to *67 format) \n2. Please document in your progress note that the patient representative was called.\n\n\nBest, \nP Meka\ntel:********")
    
# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("6B text to call pilot")

# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=5)
# Pack the frame into the window
frm_form.pack(padx=10, pady=10)

# Create the Label and Entry widgets for "Phone"
lbl_phone = tk.Label(master=frm_form, text="Phone:")
ent_phone = tk.Entry(master=frm_form, width=10, bg="light grey")
# Use the grid to place the Label and Entry widgets in the first and second columns of the
lbl_phone.grid(row=0, column=0, sticky="e")
ent_phone.grid(row=0, column=1, sticky="w")
ent_phone.insert(0,"+1")


# Create the Label and Entry widgets for "Message"
lbl_message = tk.Label(master=frm_form, text="Message:")
ent_message = tk.Entry(master=frm_form, width=100, bg="light grey")
# Use the grid geometry manager to place the Label andEntry widgets in the first and second columns of the
lbl_message.grid(row=1, column=0, sticky="e")
ent_message.grid(row=1, column=1)
ent_message.insert(0, "Pod 6B here: We anticipate the team will call you during rounds. The team will tentatively round between *** am.  Text M for more information and STOP to stop receiving messages.")


# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Email" button and pack it to the left side `frm_buttons`
btn_email = tk.Button(master=frm_buttons, text="Email RC", fg="blue", bg="light grey", relief=tk.RAISED, command=mail_to )
btn_email.pack(side=tk.LEFT, padx=5, ipadx=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
btn_submit = tk.Button(master=frm_buttons, text="Submit", fg="green", relief=tk.RAISED, command=send_message)
btn_submit.pack(side=tk.RIGHT, padx=5, ipadx=5)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear", fg="red", relief=tk.RAISED, command=clear_text)
btn_clear.pack(side=tk.RIGHT, ipadx=5)

# Start the application
window.mainloop()


