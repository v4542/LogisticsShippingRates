# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calcualte the shipping cost
shipping_cost = weight * rate

print(f"Shipping Cost: {shipping_cost} USD")
