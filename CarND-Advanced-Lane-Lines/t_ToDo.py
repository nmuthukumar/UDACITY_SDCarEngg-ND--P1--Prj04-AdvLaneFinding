### Define a Class `Line` To Receive & Store the Characteristics Of Each Line Detection
class Line():
    def __init__(self):
        # Keep a Count of the Frame Number
        self.frame_number = 0
        # Was the Line Detected in the Last Iteration?
        self.line_detected = False
        # x Values for Detected Line Pixels
        self.line_pixels_allx = None
        # y Values for Detected Line Pixels
        self.line_pixels_ally = None
        # Polynomial Co-efficients for the Most Recent Fit
        self.line_fit_current = [np.array([False])]
        # x Values of the Last n Fits of the Line
        self.line_nlast_fit_x = []
        # Average x Values of the Fitted Line over the Last n Iterations
        self.line_nlast_fit_x_avg = None
        # Polynomial Coefficients Averaged Over the Last n Iterations
        self.line_nlast_fit_avg = None
        # Difference in Fit Coefficients Between Last and New Fits
        self.line_last_fit_diffs = np.array([0,0,0], dtype='float')
        # Radius Of Curvature of the Line in meters
        self.line_curve_rad = None
        # Distance in meters of Vehicle Center from Lane Center
        self.line_vehicle_offset = None

###
LeftLane  = Line()
RightLane = Line()
