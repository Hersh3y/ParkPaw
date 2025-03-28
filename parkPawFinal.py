import tkinter as tk
from tkinter import messagebox

# Constants
P_SPACE_C1 = 200  # Number of parking spaces for C1
P_SPACE_C2 = 150 # Number of parking spaces for C2
dict_of_spaces_c1 = {f"C{i}": 0 for i in range(1, P_SPACE_C1 + 1)}  # Initialize all C1 spaces as available (0)
dict_of_spaces_c2 = {f"C{i}": 0 for i in range(1, P_SPACE_C2 + 1)}  # Initialize all C2 spaces as available (0)
SPACE_ROWS = 20  # Number of rows for displaying spaces in the grid
current_parked_spot = [None]  # Tracks the current parked spot of the user (None if no spot is assigned)
current_parking_lot = [1]  # 1 for C1, 2 for C2

# Credentials storage (for simplicity, hardcoded)
USER_CREDENTIALS = {}  # This will store usernames and passwords

# Initialize the root window
root = tk.Tk()
root.title('Clemson Parking')
root.attributes('-fullscreen', True)
root.configure(bg='#FFEABD')

# Frames for switching screens
loginFrame = tk.Frame(root, bg='#FFEABD')
createAccountFrame = tk.Frame(root, bg='#FFEABD')
startFrame = tk.Frame(root, bg='#FFEABD')
parkFrame = tk.Frame(root, bg='#FFEABD')
parkFrame2 = tk.Frame(root, bg='#FFEABD')  # Frame for second parking lot

# Function to exit fullscreen
def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)
    return "break"

# Bind Escape key to exit fullscreen
root.bind("<Escape>", end_fullscreen)

# Function to switch frames
def go_Start():
    startFrame.pack(fill='both', expand=1)
    parkFrame.pack_forget()
    parkFrame2.pack_forget()
    loginFrame.pack_forget()
    createAccountFrame.pack_forget()

def go_Park_C1():
    current_parking_lot[0] = 1  # Switch to C1 parking lot
    parkFrame.pack(fill='both', expand=1)
    startFrame.pack_forget()
    loginFrame.pack_forget()
    createAccountFrame.pack_forget()
    update_parking_grid()

def go_Park_C2():
    current_parking_lot[0] = 2  # Switch to C2 parking lot
    parkFrame2.pack(fill='both', expand=1)
    startFrame.pack_forget()
    loginFrame.pack_forget()
    createAccountFrame.pack_forget()
    update_parking_grid()


def go_Login():
    loginFrame.pack(fill='both', expand=1)
    startFrame.pack_forget()
    parkFrame.pack_forget()
    parkFrame2.pack_forget()
    createAccountFrame.pack_forget()

def go_CreateAccount():
    createAccountFrame.pack(fill='both', expand=1)
    loginFrame.pack_forget()
    startFrame.pack_forget()
    parkFrame.pack_forget()
    parkFrame2.pack_forget()

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Successful", "Welcome to Clemson Parking!")
        go_Start()
    else:
        messagebox.showerror("Invalid Login", "Incorrect username or password.")

def create_account():
    username = new_username_entry.get()  # type: ignore
    password = new_password_entry.get()  # type: ignore
    confirm_password = confirm_password_entry.get()  # type: ignore

    if username in USER_CREDENTIALS:
        messagebox.showerror("Account Exists", "This username already exists.")
        return
    
    if password != confirm_password:
        messagebox.showerror("Password Mismatch", "Passwords do not match.")
        return
    
    if username and password:  # Ensure both fields are filled
        USER_CREDENTIALS[username] = password
        messagebox.showinfo("Account Created", f"Account for {username} created successfully!")
        go_Login()  # Switch to login screen after account creation
    else:
        messagebox.showerror("Incomplete Fields", "Please fill in all fields.")

def logout():
    global current_parked_spot
    current_parked_spot[0] = None
    go_Login()
    
def quitPark():
    exit()
    

loginGreet = tk.Label(loginFrame, bg='#FFEABD', text='Please Log In To ParkPaw', font=("Bell Gothic Std Black", 30))
loginGreet.place(x=400, y=15)

username_label = tk.Label(loginFrame, bg='#FFEABD', text='Username:', font=("Bell Gothic Std Black", 14))
username_label.place(x=400, y=100)

username_entry = tk.Entry(loginFrame, font=("Bell Gothic Std Black", 14), width=20)
username_entry.place(x=510, y=100)

password_label = tk.Label(loginFrame, bg='#FFEABD', text='Password:', font=("Bell Gothic Std Black", 14))
password_label.place(x=400, y=150)

password_entry = tk.Entry(loginFrame, font=("Bell Gothic Std Black", 14), width=20, show="*")
password_entry.place(x=510, y=150)

login_button = tk.Button(loginFrame, text='Login', width=20, bg="#F56600", font=('Bell Gothic Std Black Bold', 14), command=login)
login_button.place(x=510, y=200)

create_account_button = tk.Button(loginFrame, text='Create an Account', width=20, bg="#F56600", font=('Bell Gothic Std Black Bold', 14), command=go_CreateAccount)
create_account_button.place(x=510, y=250)

# Add widgets to the create account frame
createAccountGreet = tk.Label(createAccountFrame, bg='#FFEABD', text='Create an Account', font=("Bell Gothic Std Black", 30))
createAccountGreet.place(x=450, y=15)

new_username_label = tk.Label(createAccountFrame, bg='#FFEABD', text='Username:', font=("Bell Gothic Std Black", 14))
new_username_label.place(x=400, y=100)

new_username_entry = tk.Entry(createAccountFrame, font=("Bell Gothic Std Black", 14), width=20)
new_username_entry.place(x=510, y=100)

new_password_label = tk.Label(createAccountFrame, bg='#FFEABD', text='Password:', font=("Bell Gothic Std Black", 14))
new_password_label.place(x=400, y=150)

new_password_entry = tk.Entry(createAccountFrame, font=("Bell Gothic Std Black", 14), width=20, show="*")
new_password_entry.place(x=510, y=150)

confirm_password_label = tk.Label(createAccountFrame, bg='#FFEABD', text='Confirm Password:', font=("Bell Gothic Std Black", 14))
confirm_password_label.place(x=340, y=200)

confirm_password_entry = tk.Entry(createAccountFrame, font=("Bell Gothic Std Black", 14), width=20, show="*")
confirm_password_entry.place(x=510, y=200)

create_account_submit_button = tk.Button(createAccountFrame, text='Create Account', width=20, bg="#F56600", font=('Bell Gothic Std Black Bold', 14), command=create_account)
create_account_submit_button.place(x=510, y=250)

back_to_login_button = tk.Button(createAccountFrame, text='Back to Login', width=20, bg="#F56600", font=('Bell Gothic Std Black Bold', 14), command=go_Login)
back_to_login_button.place(x=510, y=300)

# Add widgets to the start frame
clemGreet = tk.Label(startFrame, bg='#FFEABD', text='Clemson Parking', font=("Bell Gothic Std Black", 30))
clemGreet.place(x=450, y=15)

startButton = tk.Button(startFrame, text='See C1 Parking', width=25, bg="#F56600", font=('Bell Gothic Std Black Bold', 20), command=go_Park_C1)
startButton.place(x=440, y=70)
startButton2 = tk.Button(startFrame, text='See C2 Parking', width=25, bg="#F56600", font=('Bell Gothic Std Black Bold', 20), command=go_Park_C2)
startButton2.place(x=440, y=150)

quitButton = tk.Button(startFrame, text = "quit", bg = '#522D80', font=('Bell Gothic Std Black Bold', 20), command= quitPark)
quitButton.place(x=600,y=700)
def update_parking_grid():
    """Update the parking interface with a centered grid visualization and an input box for manual entry."""
    dict_of_spaces = dict_of_spaces_c1 if current_parking_lot[0] == 1 else dict_of_spaces_c2
    parkFrame_to_use = parkFrame if current_parking_lot[0] == 1 else parkFrame2
    
    # Clear the existing widgets
    for widget in parkFrame_to_use.winfo_children():
        widget.destroy()

    # Greet label and navigation button
    parkGreet = tk.Label(parkFrame_to_use, bg='#FFEABD', text='Enter Your Parking Spot:', font=("Bell Gothic Std Black", 14))
    parkGreet.place(x=550, y=15)

    endButton = tk.Button(parkFrame_to_use, text='Back to Start', bg ='#F56600', font=("Bell Gothic Std Black", 14), command=go_Start)
    endButton.place(x=8, y=15)
    #bg = '#522D80'
    #bg ='#F56600',
    logoutButton = tk.Button(parkFrame_to_use, text='Logout',  bg = '#522D80', font=("Bell Gothic Std Black", 14), command=logout)
    logoutButton.place(x=8, y=55)

    # Spacer to push the grid lower
    spacer = tk.Label(parkFrame_to_use, bg='#FFEABD', text="")
    spacer.grid(row=0, column=0, columnspan=SPACE_ROWS, pady=50)

    # Generate parking grid for visualization
    for i, spot in enumerate(dict_of_spaces.keys()):
        color = "orange" if dict_of_spaces[spot] == 0 else "purple"
        label = tk.Label(
            parkFrame_to_use,
            text=spot,
            bg=color,
            fg="white",
            width=10,
            height=2,
            font=("Bell Gothic Std Black", 12),
        )
        label.grid(
            row=i // SPACE_ROWS + 1,
            column=i % SPACE_ROWS,
            padx=5,
            pady=5
        )

    # Center the grid horizontally
    for col in range(SPACE_ROWS):
        parkFrame_to_use.grid_columnconfigure(col, weight=1, uniform="equal")

    # Input section for manual parking interaction
    input_row = (P_SPACE_C1 // SPACE_ROWS) + 2  # Position the input below the grid
    spot_label = tk.Label(parkFrame_to_use, text="Enter Spot (e.g., C1):", bg='#FFEABD', font=("Bell Gothic Std Black", 14))
    spot_label.grid(row=input_row, column=0, columnspan=SPACE_ROWS // 2, pady=10, sticky='e')

    spot_entry = tk.Entry(parkFrame_to_use, font=("Bell Gothic Std Black", 14), width=15)
    spot_entry.grid(row=input_row, column=SPACE_ROWS // 2, columnspan=SPACE_ROWS // 2, pady=10, sticky='w')

    # Submit button for parking
    submit_button = tk.Button(
        parkFrame_to_use,
        text="Submit",
        bg = '#F56600',
        font=("Bell Gothic Std Black", 14),
        command=lambda: handle_parking_input(spot_entry.get())
    )
    submit_button.grid(row=input_row + 1, column=0, columnspan=SPACE_ROWS, pady=10)

    # Leave Spot Button
    leave_button = tk.Button(
        parkFrame_to_use,
        text="Leave Spot",
        bg = '#522D80',
        font=("Bell Gothic Std Black", 14),
        command=leave_spot,
        state=tk.NORMAL if current_parked_spot[0] else tk.DISABLED
    )
    leave_button.grid(row=input_row + 2, column=0, columnspan=SPACE_ROWS, pady=10)

def handle_parking_input(spot):
    """Handle user input for parking or vacating a spot.""" 
    spot = spot.strip().upper()  # Normalize input
    dict_of_spaces = dict_of_spaces_c1 if current_parking_lot[0] == 1 else dict_of_spaces_c2 
    
    if spot not in dict_of_spaces:
        messagebox.showerror("Invalid Spot", f"{spot} is not a valid parking spot.")
        return

    if current_parked_spot[0]:
        messagebox.showerror("Error", f"You are already parked in {current_parked_spot[0]} . Leave that spot first.")
        return

    if dict_of_spaces[spot] == 0:
        confirm = messagebox.askyesno("Confirm Parking", f"Do you want to park in {spot}?")
        if confirm:
            dict_of_spaces[spot] = 1
            current_parked_spot[0] = spot
            messagebox.showinfo("Parked", f"You have parked in {spot}. Have fun!")
    else:
        messagebox.showerror("Spot Occupied", f"{spot} is currently occupied. Please select another spot.")

    update_parking_grid()

def leave_spot():
    """Vacate the current parked spot."""
    if not current_parked_spot[0]:
        messagebox.showerror("Error", "You are not parked in any spot.")
        return

    spot = current_parked_spot[0]
    confirm = messagebox.askyesno("Confirm Leaving", f"Do you want to leave {spot}?")
    if confirm:
        if current_parking_lot[0] == 1:
            dict_of_spaces_c1[spot] = 0  # Vacate spot in C1
        else:
            dict_of_spaces_c2[spot] = 0  # Vacate spot in C2
        current_parked_spot[0] = None
        messagebox.showinfo("Spot checked out", f"You have checked out of {spot}. Drive safe!")

    update_parking_grid()

# Show the login frame initially
go_Login()

# Run the main loop
if __name__ == '__main__':
    root.mainloop()

