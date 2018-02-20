from robotpy_ext.autonomous import StatefulAutonomous, timed_state
                    
class DriveReverse(StatefulAutonomous):

    MODE_NAME = 'Drive Reverse'

    def initialize(self):
        
        # This allows you to tune the variable via the SmartDashboard over
        # networktables
        #self.register_sd_var('drive_speed', 1)
        pass
        

    @timed_state(duration=0.5, next_state='drive_reverse', first=True)
    def drive_wait(self):
        pass

    @timed_state(duration=5)
    def drive_reverse(self):
        self.drive.moveToPosition(0)