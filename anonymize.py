import pandas as pd
import os

os.makedirs("output", exist_ok=True)

# -----------------------------
# Global mapping dictionaries
# -----------------------------
society_map = {}
area_map = {}
customer_map = {}
shipping_address_map = {}
customer_address_map = {}
delivery_area_map = {}

# -----------------------------
# Helper function
# -----------------------------
def anonymize_column(df, column, mapping, prefix):

    if column not in df.columns:
        return

    for value in df[column].dropna().unique():
        if value not in mapping:
            mapping[value] = f"{prefix}_{len(mapping)+1:03d}"

    df[column] = df[column].map(mapping)


# =====================================================
# 1. AMUL ORDERS
# =====================================================

orders = pd.read_excel(
    "data/Amul_Orders_Cleaned.xlsx",
    sheet_name="Cleaned Orders Data"
)

# Mobile
import numpy as np

if "Shipping Mobile" in orders.columns:
    orders["Shipping Mobile"] = np.nan

anonymize_column(
    orders,
    "Shipping Address",
    shipping_address_map,
    "Address"
)

anonymize_column(
    orders,
    "Customer Address",
    customer_address_map,
    "Customer_Address"
)

anonymize_column(
    orders,
    "Delivery Area (derived)",
    delivery_area_map,
    "Delivery_Area"
)



with pd.ExcelWriter(
    "output/Amul_Orders_Anonymized.xlsx",
    engine="openpyxl"
) as writer:

    orders.to_excel(
        writer,
        sheet_name="Cleaned Orders Data",
        index=False
    )

print("✅ Amul Orders Done")


# =====================================================
# 2. SHIPPING ADDRESS FILE
# =====================================================

shipping = pd.read_excel(
    "data/shipping address claened.xlsx",
    sheet_name="Cleaned Orders Data"
)

anonymize_column(
    shipping,
    "Customer Name",
    customer_map,
    "Customer"
)

anonymize_column(
    shipping,
    "Shipping Address",
    shipping_address_map,
    "Address"
)

anonymize_column(
    shipping,
    "Society",
    society_map,
    "Society"
)

anonymize_column(
    shipping,
    "Area",
    area_map,
    "Area"
)



with pd.ExcelWriter(
    "output/Shipping_Address_Anonymized.xlsx",
    engine="openpyxl"
) as writer:

    shipping.to_excel(
        writer,
        sheet_name="Cleaned Orders Data",
        index=False
    )

print("✅ Shipping Address Done")


# =====================================================
# 3. DELIVERY AREA MASTER
# =====================================================

mapping = pd.read_excel(
    "data/Delivery_Area_Mapping_Master.xlsx",
    sheet_name="Sheet"
)

anonymize_column(
    mapping,
    "Original Delivery Area",
    delivery_area_map,
    "Delivery_Area"
)

anonymize_column(
    mapping,
    "Standard Area",
    area_map,
    "Area"
)

with pd.ExcelWriter(
    "output/Delivery_Area_Mapping_Anonymized.xlsx",
    engine="openpyxl"
) as writer:

    mapping.to_excel(
        writer,
        sheet_name="Sheet",
        index=False
    )

print("✅ Delivery Mapping Done")

print("\n🎉 All files anonymized successfully!")