import tkinter
import customtkinter
import statistics

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Chemistry Helper")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)





# Functions

# mass calc
def find_mass():
    if volume.get() == "":
        answer_label.configure(text="ENTER A VALID FLOAT FOR VOLUME.")
    elif density.get() == "":
        answer_label.configure(text="ENTER A VALID FLOAT FOR DENSITY.")

    else:
        volume_val = float(volume.get())
        density_val = float(density.get())
        answer = volume_val * density_val
        answer_label.configure(text="Mass = " + str(answer))
        print("Mass:", answer)
    
# volume calc
def find_volume():
    if mass.get() == "":
        answer_label.configure(text="ENTER A VALID FLOAT FOR MASS.")
    elif density.get() == "":
        answer_label.configure(text="ENTER A VALID FLOAT FOR DENSITY.")

    else:
        mass_val = float(mass.get())
        density_val = float(density.get())
        answer = mass_val / density_val
        answer_label.configure(text="Volume = " + str(answer))
        print("Volume:", answer)
   
# density calc
def find_density():
    if volume.get() == "":
        answer_label.configure(text="ENTER A VALID FLOAT FOR VOLUME.")
    elif mass.get() == "":
        answer_label.configure(text="ENTER A VALID FLOAT FOR MASS.")

    else:
        mass_val = float(mass.get())
        volume_val = float(volume.get())
        answer = mass_val / volume_val
        answer_label.configure(text="Density = " + str(answer))
        print("Density:", answer)

# standard deviation calc
def find_stdev():
    # error checking
    if sample.get() == "":
        answer_label.configure(text="ENTER DATA POINTS.")
    # actual function
    else:
        sample_data = sample.get()
        sample_data_num = [float(i) for i in sample_data.split(', ')]
        print((statistics.stdev(sample_data_num)))
        answer_label.configure(text="stdev = " + str((statistics.stdev(sample_data_num))))

def find_mean():
    nums = sample.get()
    num_list = [float(i) for i in nums.split(', ')]
    sum_nums = sum(num_list)
    no_nums = len(num_list) 
    mean = sum_nums / no_nums
    print("sum =", sum_nums)
    print("number of entries =", no_nums)
    print("Mean =", mean)
    answer_label.configure(text="mean = " + str(mean))

def find_median():
    nums = sample.get()
    num_list = [float(i) for i in nums.split(', ')]
    median = statistics.median(num_list)
    print(median) 
    answer_label.configure(text="median = " + str(median))

def find_mode():
    nums = sample.get()
    num_list = [float(i) for i in nums.split(', ')]
    mode = statistics.mode(num_list)
    print(mode) 
    answer_label.configure(text="mode = " + str(mode))



# UI stuff

# Top part of app
title_text = customtkinter.CTkLabel(master=frame_1, text="Welcome to Chemistry skipper.")
title_text.pack(pady=10, padx=10)

answer_title = customtkinter.CTkLabel(master=frame_1, text="Answer:")
answer_title.pack(padx=10)
answer_label = customtkinter.CTkLabel(master=frame_1, text="0.0")
answer_label.pack(padx=10)

# Tabs at the bottom
tabview = customtkinter.CTkTabview(master=frame_1, width=300, height=500)
tabview.pack(padx=10)
tabview.add("MVD")
tabview.add("Stats")



# Mass Volume and Density (MVD) tab
MVD_tab = customtkinter.CTkLabel(tabview.tab("MVD"), text="Welcome to MASS VOLUME AND DENSITY Helper.")
MVD_tab.pack(padx=10)

MVD_help = customtkinter.CTkLabel(tabview.tab("MVD"), text="Fill in what you know and then click the button you want to know:")
MVD_help.pack(padx=10)

mass_button = customtkinter.CTkButton(tabview.tab("MVD"), text="Mass", command=find_mass)
mass_button.pack(pady=20)
mass = customtkinter.CTkEntry(tabview.tab("MVD"))
mass.pack()

volume_button = customtkinter.CTkButton(tabview.tab("MVD"), text="Volume", command=find_volume)
volume_button.pack(pady=20)
volume = customtkinter.CTkEntry(tabview.tab("MVD"))
volume.pack()

density_button = customtkinter.CTkButton(tabview.tab("MVD"), text="Density", command=find_density)
density_button.pack(pady=20)
density = customtkinter.CTkEntry(tabview.tab("MVD"))
density.pack()


# stats tab
stats_tab = customtkinter.CTkLabel(tabview.tab("Stats"), text="Welcome to STATS Helper.")
stats_tab.pack(padx=10)

stats_help = customtkinter.CTkLabel(tabview.tab("Stats"), text="Fill in sample data seperated with a comma and a single space e.g. \n1, 2, 3, ...\nThen click button to solve for what you want.")
stats_help.pack(padx=10)

sample = customtkinter.CTkEntry(tabview.tab("Stats"))
sample.pack(pady=10)
stdev_sample_button = customtkinter.CTkButton(tabview.tab("Stats"), text="Sample standard deviation", command= find_stdev)
stdev_sample_button.pack(pady=15)
mean_button = customtkinter.CTkButton(tabview.tab("Stats"), text="Mean(average)", command= find_mean)
mean_button.pack(pady=5)
median_button = customtkinter.CTkButton(tabview.tab("Stats"), text="Median(middle)", command= find_median)
median_button.pack(pady=5)
mode_button = customtkinter.CTkButton(tabview.tab("Stats"), text="Mode(most common)", command= find_mode)
mode_button.pack(pady=5)




app.mainloop()

