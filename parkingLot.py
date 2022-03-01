import VehicleTypes


class Parking:
    def __init__(self):
        self.volume = 0
        self.ticketid = 0
        self.allotedSlots = 0

    def getEmptySlot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i
				

    def createParkingSpace(self, volume):
        self.slots = [-1] * volume
        self.volume = volume 
        return self.volume

    def park(self, regno, color, veh):
        if self.allotedSlots < self.volume:
            ticketid = self.getEmptySlot()
            if veh == 'car':
                self.slots[ticketid] = VehicleTypes.Car(regno, color, 'car')
            elif veh == 'bike':
                self.slots[ticketid] = VehicleTypes.Bike(regno, color, 'bike')
            elif veh == 'truck':
                self.slots[ticketid] = VehicleTypes.Bike(regno, color, 'truck')

            self.ticketid = self.ticketid+1
            self.allotedSlots = self.allotedSlots + 1
            return ticketid+1
        else:
            return -1

    def leave(self, ticketid):

        if self.allotedSlots > 0 and self.slots[ticketid-1] != -1:
            self.slots[ticketid-1] = -1
            self.allotedSlots = self.allotedSlots - 1
            return True
        else:
            return False

    def overview(self):
        print("---------------------------------------------------------------------------------\n|Ticket No.\tVehicle Type\t\tColour\t\tVehicle Registration No.|\n---------------------------------------------------------------------------------")


        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1) + "\t\t" + str(self.slots[i].vehicleType) + "\t\t\t" + str(
                    self.slots[i].color)+"\t\t"+str(self.slots[i].regno)+"\n")
            else:
                continue

    def slotnumFromRegNo(self, regno):

        for i in range(len(self.slots)):
            if self.slots[i].regno == regno:
                return i+1
            else:
                continue
        return -1

    def slotnumFromColor(self, color):

        slotnums = []

        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnums.append(str(i+1))
        return slotnums







    def display(self, line):
        if line.startswith('Create-Parking-Lot'): 
            n = int(line.split(' ')[1]) # it will create a list with elements [create-parking-lot , 5 ,slots] and fetch the data from index 1 which is 5
            res = self.createParkingSpace(n)  #at line 16
            print('\nWelcome!🎊 \n')
            print('Created a parking lot with '+str(res)+' slots \n')

        elif line.startswith('park'):  #at line 21
            regno = line.split(' ')[1]
            color = line.split(' ')[2]
            veh = line.split(' ')[3]
            res = self.park(regno, color, veh)
            if res == -1:
                print("Sorry, The lot is full...Please wait.")
            else:
                print('Allocated slot number: '+str(res) + "\n")

        elif line.startswith('leave'): #at line 37
            leave_ticketid = int(line.split(' ')[1])
            overview = self.leave(leave_ticketid)
            if overview:
                print("Thank you ❤️ \nVisit Again 🙂")
                print('Slot number '+str(leave_ticketid)+' is vacant')

        elif line.startswith('overview'): #at line 46
            self.overview()


        elif line.startswith('get_slotnum_by_colour'): #at line 66
            color = line.split(' ')[1]
            slotnums = self.slotnumFromColor(color)
            print(', '.join(slotnums))

        # elif line.startswith('getregistration_number_by_colour'):
        #     color = line.split(' ')[1]
        #     regnos = self.getRegNoFromColor(color)
        #     print(', '.join(regnos))


        elif line.startswith('get_slotnum_by_regNo'): #at line 47
            regno = line.split(' ')[1]
            slotnum = self.slotnumFromRegNo(regno)
            if slotnum == -1:
                print("Not found")
            else:
                print(slotnum)

        elif line.startswith('exit'): 
            print("\n-- Service Closed!! --")
	
            exit(0)
        else:
            print("Please enter an appropriate command !!")


parking = Parking()
while True:
	line = input("=====> ")
	parking.display(line)


