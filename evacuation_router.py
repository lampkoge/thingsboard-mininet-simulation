class EvacuationRouter:
    def __init__(self):
        self.ap_locations = {
            "ap1": (10, 20),
            "ap2": (30, 20),
        }
        self.exit_points = {
            "Exit A": (5, 5),
            "Exit B": (40, 5),
        }
    
    def nearest_exit(self, ap_name):
        ap_position = self.ap_locations.get(ap_name)
        nearest = None
        min_distance = float("inf")
        
        for exit_name, exit_pos in self.exit_points.items():
            dist = ((ap_position[0] - exit_pos[0]) ** 2 + (ap_position[1] - exit_pos[1]) ** 2) ** 0.5
            if dist < min_distance:
                nearest = exit_name
                min_distance = dist
        
        return nearest

# Example usage
router = EvacuationRouter()
current_ap = "ap1"
print(f"User near {current_ap} should exit through {router.nearest_exit(current_ap)}")
