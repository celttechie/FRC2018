from robotpy_ext.autonomous import StatefulAutonomous, timed_state
                    
class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Drive Forward'
    DEFAULT = True

    def initialize(self):
        
        # This allows you to tune the variable via the SmartDashboard over
        # networktables
        #self.register_sd_var('drive_speed', 1)
        pass

    @timed_state(duration=0.5, next_state='drive_forward1', first=True)
    def drive_wait(self):
        pass

    @timed_state(duration=6)
    def drive_forward1(self):
        self.drive.arcadeWithRPM(.5, 0, 2800)
        
    @timed_state(duration=4, next_state='drive_forward2')
    def drive_back1(self):
        self.drive.arcadeWithRPM(-.5, 0, 2800)
        
    @timed_state(duration=4, next_state='drive_back2')
    def drive_forward2(self):
        self.drive.arcadeWithRPM(.5, 0, 2800)
        
    @timed_state(duration=4)
    def drive_back2(self):
        self.drive.arcadeWithRPM(-.5, 0, 2800)        