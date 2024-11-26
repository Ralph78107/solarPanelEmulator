import tkinter as tk

class SolarPanelSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Solar Panel Energy Simulator with Weather and Battery")

        # Canvas for visuals
        self.canvas = tk.Canvas(self, width=400, height=200, bg="sky blue")
        self.canvas.pack()

        # Draw sun and solar panel
        self.sun = self.canvas.create_oval(50, 50, 150, 150, fill="gray")  
        self.panel = self.canvas.create_rectangle(200, 150, 300, 170, fill="black")  

        # Variables for energy generation, battery, and conditions
        self.energy_generated = 0
        self.battery_level = 0  # Battery in kWh
        self.sun_intensity = "Off"  # Initialize sun intensity

        # Energy display
        self.energy_label = tk.Label(self, text=f"Energy Generated: {self.energy_generated:.2f} kWh")
        self.energy_label.pack(pady=5)

        # Battery display
        self.battery_label = tk.Label(self, text=f"Battery Level: {self.battery_level:.2f} kWh")
        self.battery_label.pack(pady=5)

        # Sun intensity selection
        self.intensity_var = tk.StringVar(self)
        self.intensity_var.set("Off")
        self.intensity_menu = tk.OptionMenu(self, self.intensity_var, "Off", "Low", "Medium", "High", command=self.update_intensity)
        self.intensity_menu.pack(pady=5)

        # Weather condition selection
        self.weather_var = tk.StringVar(self)
        self.weather_var.set("Sunny")
        self.weather_menu = tk.OptionMenu(self, self.weather_var, "Sunny", "Cloudy", "Rainy", command=self.update_weather)
        self.weather_menu.pack(pady=5)

        # Initialize weather impact and call update function
        self.weather_impact = 1.0
        self.update_energy()

    def update_intensity(self, intensity):
        """Update sun intensity and appearance based on selection."""
        self.sun_intensity = intensity  # Set the sun intensity
        # Update sun color
        colors = {"Off": "gray", "Low": "light yellow", "Medium": "yellow", "High": "goldenrod"}
        self.canvas.itemconfig(self.sun, fill=colors[intensity])

    def update_weather(self, weather):
        """Adjust weather impact on energy generation."""
        if weather == "Sunny":
            self.weather_impact = 1.0
        elif weather == "Cloudy":
            self.weather_impact = 0.5
        elif weather == "Rainy":
            self.weather_impact = 0.1

    def update_energy(self):
        """Update energy generation and battery based on conditions."""
        # Energy generation based on intensity and weather
        intensity_factors = {"Off": 0, "Low": 1, "Medium": 2, "High": 3}
        energy_rate = intensity_factors[self.sun_intensity] * self.weather_impact
        self.energy_generated += energy_rate
        self.battery_level = min(self.battery_level + energy_rate, 100)  # Max battery capacity at 100 kWh

        # Update displays
        self.energy_label.config(text=f"Energy Generated: {self.energy_generated:.2f} kWh")
        self.battery_label.config(text=f"Battery Level: {self.battery_level:.2f} kWh")

        # Simulate battery discharge when sun is off
        if self.sun_intensity == "Off" and self.battery_level > 0:
            self.battery_level -= 0.5  # Discharge rate
            self.battery_label.config(text=f"Battery Level: {self.battery_level:.2f} kWh")

        # Call this function again after 1 second
        self.after(1000, self.update_energy)

# Main function to run the simulator
def main():
    app = SolarPanelSimulator()
    app.mainloop()

if __name__ == "__main__":
    main()
