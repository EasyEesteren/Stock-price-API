import Tkinter as tk
import requests
from PIL import Image, ImageTk
import datetime

HEIGHT = 600
WIDTH = 900

#Uses requests to connect to alpha_vantage's stock market API to get the latest quote for a security 
def getStock(entry):
	try:
		now = datetime.datetime.now()
		API_KEY = "V65JYO9S7UT30ESV"
		r = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + entry + '&apikey=' + API_KEY)
		res = r.json()
		company = "Company: " + res['Global Quote']["01. symbol"]
		price = "Stock price: " + res['Global Quote']["05. price"]
		date = "Date: "+ str(now.year) + "-" + str(now.month) +"-"+ str(now.day)
		time = "Time: " + str(now.hour)+":"+ str(now.minute)+" & " + str(now.second) + " seconds"
		label["text"] =  company + "\n" + price + "\n" + date + "\n" + time
	except:
		label["text"] = "There was a problem retrieving this information. Please ensure valid ticker."

#Starts the use of Tkinter
root = tk.Tk()
#The canvas is the background which the rest of the GUI is placed in
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#The frame encloses the entry box "entry" 
frame = tk.Frame(root, bg = "#001a33", bd = 10)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n") 

#Entry allows for users to input their querry
entry = tk.Entry(frame, bg="white", font = 40)
entry.place(relwidth = 0.75, relheight = 1)

#The search button
button = tk.Button(frame, text = "Search", bg='red', fg="red", command = lambda: getStock(entry.get()))
button.place(relx = 0.8, rely = 0.05, relheight = 0.9, relwidth = 0.2)

#Lower frame 
lower_frame = tk.Frame(root, bg = "#001a33", bd = 20)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

#label in the lower frame
label = tk.Label(lower_frame)
label.place(relwidth = 1, relheight = 1)

root.mainloop()

