class Print:
    def __init__(self):
        self.printingTasks = []

    def addPrintTaskToSchedule(self,printTask):
        self.printingTasks.append(printTask)
        print(f"Added task : {printTask}")

    def printingTheTask(self):
        if len(self.printingTasks) == 0:
            print("No Tasks")
            return
        else:
            while self.printingTasks:
                printTask = self.printingTasks.pop(0)
                print(f"printing: {printTask}")


printScheduler = Print()

# printScheduler.addPrintTaskToSchedule("Sravya's resume")
# printScheduler.addPrintTaskToSchedule("Krishna's wiki page for telengana tourism")
# printScheduler.addPrintTaskToSchedule("Bindu's Mahesh Babu poster")

printScheduler.printingTheTask()

    
