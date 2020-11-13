#TO-DO: 
# 1.Read comments and count how yellow, white etc solves i have.
# 2.Make one csv for all sessions and split the columns for each session. Diladi tha uparxei to kathe session to ena dipla sto allo kai oi xronoi gia to kathena tha vriskontai apo katw tous.

#Author: Konstantinos Gialantzis (enolic)

#importing the module
import json
import csv
#opening json file
with open('Time_List.txt') as cs_txt_file:
	data = json.load(cs_txt_file)

	# Print the type of data variable
	print("Type:", type(data))


##thelw na diabasw to posa einai ola ta sessions kratwntas mono ton arithmo apo kathe arxiko stoixeio tis kathe listas... diladi session5 --> 5 k.o.k.
cie_cnt = 0 #check if it is Empty Counter

for x in data.items(): #gia kathe prwto stixeio se kathe lista ( x[0] ) diavaze to 7 gramma tis leksis.. x[0][7]
	if (x[0][7:]).isnumeric():   #elegxei an ta strings pou uparxoun meta ti thesi 7 stin ekastote leksi mporei na einai arithmos i grammata
		print(x[0], "->", x[0][7:]) # an einai arithmos ton ektupwnei

	else:
		break  #an oxi, stamataei tin for loop

	print(type(x[0][7:]))


	if data['session' + str(cie_cnt+1)] == []:
	 	print("true")
	 	break
	else: 
		print("false")
		
	cie_cnt += 1 #tha einai iso me ton arithmo tou session pou einai prin to keno session


	#TO-DO: an kapoios exei gemata ta session 1, 2, 3 ... adeia ta 4, 5 ,6 kai epeita exei kapoio allo gemato to programma mas
	#tha stamatisei sto 3. prepei na ftiaxw na ginetai oloklirwmenos elegxos

print(cie_cnt)




sum = 0  #initialise sum

allTimes = [] #initialise the list which will contain all of the times

cnt = 0  #initialise counter


for j in range(0, cie_cnt, 1): #tha stamatisei otan ftasei to noumero pou einai iso me cie_cnt
	print("!----------------Session" + str(j+1) + "---------------------!")

	for i in data['session' + str(j+1)]: #dipla sto session kollaei kathe fora to noumero cnt+1, afou cnt ksekinaei apo 0 kai den uparxei session0

		print("\n\n\n")
		print("______________________________________________________________")

		if cnt == 0: #1st solution
			print(cnt+1, "st solution:\n")
			print("______________________________________________________________")
		elif cnt == 1: #2nd solution
			print(cnt+1, "nd solution:\n")
			print("______________________________________________________________")
		elif cnt == 2: #3rd Solution
			print(cnt+1, "rd solution:\n")
			print("______________________________________________________________")
		else: #any other solutions after 3
			print(cnt+1, "th solution:\n")
			print("______________________________________________________________")

	##Solution Coding Line
		#Print the data of dictionary
		print("\nCoding Line:\n", data['session'+str(j+1)][cnt])

		print("\n\n")

	##Solution Penalty
		penalty = data['session'+str(j+1)][cnt][0][0]
		print("\nSolution Penalties: ")
		if penalty == -1:
			print("Penalty is DNF")
		elif penalty == 2000:
			print("Penalty is 2.0s")
			data['session'+str(j+1)][cnt][0][1] += 2000 #prosthetai to penalty ston xrono.
		else:
			print("There is no penalty for this solution")

	##Solution Time
		#to parakatw time2solve krataei ton prwto xrono tis prwtis lusis kai to diairei dia 1000 wste na ginoun ta deuterolepta pou proekupsan stin ekastote lusi
		time2solve = data['session'+str(j+1)][cnt][0][1]/1000 #"<- auto twra tha to diairesw dia 1000"
		print("\nTime for this solution is: ")
		if time2solve < 60.0:
			if penalty  == 2000:
				print(time2solve, "s+")
			else:
				print(time2solve, "s")
		else: #an to time2solve einai parapanw apo 60deuterolepta
			minutes = 0.0 #initialise minutes and seconds
			seconds = 0.0
			if (data['session1'][cnt][0][1]/1000)/60 < 2.0: # diladi o xronos einai katw apo 2 lepta. diladi den exoun prolavei na gemisoun 2 fores ta 60 deuterolepta
				minutes = 1.0 #tote kseroume oti einai mono 1 lepto..
				#TO-DO: na dw gia periptwsei megaluteri tou 1 leptou
				seconds = ((data['session1'][cnt][0][1]/1000)%60)/100.0
				time2solve = minutes + seconds
			print(time2solve,"m") 

	##Solution Scramble
		scramble = data['session'+str(j+1)][cnt][1]
		print("\nThe scramble is:\n",scramble)

	##Solution Comment
		comment = data['session'+str(j+1)][cnt][2]
		print("\nComment: ")
		if comment == "":
			print("There is no comment for this solution")
		else:
			print("Comment for this solution:", comment, "\n\n\n")
		allTimes.append(data['session'+str(j+1)][cnt][0][1]/1000) #prosthetei kathe fora ton xrono lusis stin lista allTimes pou periexontai oloi oi xronoi lushs tou kuvou
		#print(data['session1'][cnt][0][1]/1000)  #krataei mono tous xronous kai tous diairei dia 1000
		sum += data['session'+str(j+1)][cnt][0][1]/1000 

		cnt += 1
		avg = sum / cnt #declare avg

		#print(cnt)
		# print("total solutions: ", len(allTimes))
		# print(allTimes)
		# print("Best Time is: ", )
		# print("Worst Time is: ", )	
		# print("\n\n\n\n")
		# print("The average from all solutions of Session", (j+1), " = ", avg) 
		#an valw to avg print pou einai mesa stin mikri tin for loop na kanei print sto output.txt tote de tha vgainei swsto optiko apotelesma.... giati??????
		
	print("total solutions: ", len(allTimes))
	print(allTimes)
	print("The average from all solutions of Session", (j+1), " = ", avg)
	print("Best Time is: ", )
	print("Worst Time is: ", )	
	print("\n\n\n\n")
	#print to output.txt
	print(allTimes, file=open("output.txt", "a"))
	print("\n", file=open("output.txt", "a"))
	print("The average from all solutions of Session" + str(j+1) + " = ", avg,  file=open("output.txt", "a"))
	print("\n\n", file=open("output.txt", "a"))

	#ftiaxnei csv file #kathe fora tha ftiaxnei ena arxeio analogos to session pou vrisketai
	with open('session_' + str(j+1) + '.csv', 'w') as csvfile:
	    writer = csv.DictWriter(csvfile, fieldnames=allTimes)
	    writer.writeheader()

	with open('session_' + str(j+1) + '.csv',newline='') as f:
	    reader = csv.reader(f)
	    line = next(reader) # Read the one long line of items included in list and..

	# pairnei ena ena stoixeio kai to topothetei to ena katw apto allo
	with open('session_' + str(j+1) + '.csv', 'w', newline='') as csvfile:
	    writer = csv.writer(csvfile)
	    for i in range(0,len(line),1): # step one by one.
	        writer.writerow(line[i:i+1]) #me to 1 ta vazei ola to ena katw apto allo


	#kathe fora pou erxete sto telos tis i megali i for midenizetai to cnt, to sum kai adeiazei i lista tis allTimes wste na ksekinisei na metraei swsta gia tin epomeni session
	cnt = 0 
	sum = 0
	allTimes = []


print("Total solutions are: ", cnt)












print("\n\n\n")






	