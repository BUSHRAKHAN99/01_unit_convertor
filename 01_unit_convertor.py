import streamlit as st

st.set_page_config(page_title="Advanced Unit Converter", layout="centered")
st.title("🔄 Advanced Unit Converter")

conversion_type = st.selectbox("Select conversion type", [
    "Length", "Weight", "Temperature", "Time", "Speed", "Area", "Volume"
])

# Units dictionaries
length_units = {
    "Meters": 1,
    "Kilometers": 1000,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Feet": 0.3048,
    "Inches": 0.0254,
}

weight_units = {
    "Grams": 1,
    "Kilograms": 1000,
    "Milligrams": 0.001,
    "Pounds": 453.592,
    "Ounces": 28.3495,
}

time_units = {
    "Seconds": 1,
    "Minutes": 60,
    "Hours": 3600,
    "Days": 86400,
}

speed_units = {
    "Meters per second (m/s)": 1,
    "Kilometers per hour (km/h)": 1 / 3.6,
    "Miles per hour (mph)": 1 / 2.23694,
}

area_units = {
    "Square meters": 1,
    "Square kilometers": 1e6,
    "Square feet": 0.092903,
    "Square yards": 0.836127,
    "Acres": 4046.86,
    "Hectares": 10000,
}

volume_units = {
    "Liters": 1,
    "Milliliters": 0.001,
    "Cubic meters": 1000,
    "Gallons (US)": 3.78541,
    "Cups (US)": 0.236588,
}

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

input_value = st.number_input("Enter the value to convert", value=0.0)

# Conversion logic
def convert_temperature(value, from_u, to_u):
    if from_u == to_u:
        return value
    if from_u == "Celsius":
        return value + 273.15 if to_u == "Kelvin" else (value * 9/5) + 32
    if from_u == "Fahrenheit":
        return (value - 32) * 5/9 if to_u == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_u == "Kelvin":
        return value - 273.15 if to_u == "Celsius" else (value - 273.15) * 9/5 + 32

# Select units
if conversion_type == "Length":
    from_unit = st.selectbox("From", list(length_units.keys()))
    to_unit = st.selectbox("To", list(length_units.keys()))
    result = input_value * length_units[from_unit] / length_units[to_unit]

elif conversion_type == "Weight":
    from_unit = st.selectbox("From", list(weight_units.keys()))
    to_unit = st.selectbox("To", list(weight_units.keys()))
    result = input_value * weight_units[from_unit] / weight_units[to_unit]

elif conversion_type == "Time":
    from_unit = st.selectbox("From", list(time_units.keys()))
    to_unit = st.selectbox("To", list(time_units.keys()))
    result = input_value * time_units[from_unit] / time_units[to_unit]

elif conversion_type == "Speed":
    from_unit = st.selectbox("From", list(speed_units.keys()))
    to_unit = st.selectbox("To", list(speed_units.keys()))
    result = input_value * speed_units[from_unit] / speed_units[to_unit]

elif conversion_type == "Area":
    from_unit = st.selectbox("From", list(area_units.keys()))
    to_unit = st.selectbox("To", list(area_units.keys()))
    result = input_value * area_units[from_unit] / area_units[to_unit]

elif conversion_type == "Volume":
    from_unit = st.selectbox("From", list(volume_units.keys()))
    to_unit = st.selectbox("To", list(volume_units.keys()))
    result = input_value * volume_units[from_unit] / volume_units[to_unit]

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)
    result = convert_temperature(input_value, from_unit, to_unit)

# Display result
if conversion_type != "Temperature":
    st.success(f"{input_value} {from_unit} = {result:.4f} {to_unit}")
else:
    st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")
