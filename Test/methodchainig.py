class car():
    def turnon(self):
        print("Start")
        return self
    
    def drive(self):
        print("drive")
        return self
    
    def stop(self):
        print("stop")
        return self
    
    def exit(self):
        print("exit")
        return self
    
c1=car()

# c1.drive()    
# c1.stop()
    
print()
    
c1.turnon().drive().stop().exit()    
    