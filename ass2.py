def main():
	Gizzard = "Gizzard 100 naira "
	gizzard  = "Gizzard 50 naira"
	Rice = "Rice 200 naira "
	Moimoi = "Moi-moi 50 naira "
	Beans = "Beans 100 naira "
	Bread = "Bread 30 naira per roll"
	Drinks = "Soda drinks, Each for 100 naira and Chivita Juice for 300 naira "
	Salad = "Salad 100 naira "
	Plantain = "PLantain 10 naira each "
	Semo = "Semo 100 naira for a wrap "
	poundo = "Pounded yam 100 naira for a wrap"

	print("Welcome to Cafeteria One! \n")
	print("These are our various restaurants: Bashan, Oliveyard, Hepzibah, Sharon, Rehobooth")

	Restaurant = input("Please select a restaurant:\n")
	Restaurant = Restaurant.lower()
	print ("\n")
	if Restaurant == "bashan":
		print("At Bashan we Have \n" + Plantain + "\n" + Rice + "\n" + Beans + "\n"  + Salad )
	
	elif Restaurant == "oliveyard":
		print ("At Oliveyard we have \n" + Semo + "\n" + poundo + "\n" + "soup for free")

	elif Restaurant == "hepzibah" :
		print("At Hepzibah we have \n" + Rice +  "\n" + gizzard + "\n" + Bread + "\n" + Plantain)

	elif Restaurant == "sharon":
		print("At Sharon we have \n" + Rice + "\n" + Salad + "\n" + Moimoi + "\n" + Plantain)
	
	elif Restaurant == "rehobooth":
		print("At Rehobooth we have \n " + Drinks + "\n" + "Chi exotic 350 naira"
			+ "Ice tea 100 naira")
	else:
		print("At Cafeteria One there is no restaurant named " + Restaurant.upper())



main()
