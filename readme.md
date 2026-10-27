# Customer Behaviour Analysis Dashboard

An interactive Power BI dashboard that turns customer shopping data into clear answers about **who buys, what they buy, and how much they spend**. It is designed to be simple, readable and ready for business users.

![Dashboard Preview](screenshots\customer_behaviour_dashboard_simple.jpg)

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Business Questions](#business-questions)
3. [Key Metrics](#key-metrics)
4. [Dashboard Features](#dashboard-features)
5. [Key Insights](#key-insights)
6. [Data Model](#data-model)
7. [DAX Measures](#dax-measures)
8. [Getting Started](#getting-started)
9. [Project Structure](#project-structure)
10. [Design Guidelines](#design-guidelines)
11. [Future Enhancements](#future-enhancements)
12. [Author](#author)

---

## Project Overview

This project analyses customer purchasing behaviour across product categories, age groups and subscription status. It gives decision-makers a single page to monitor performance and spot opportunities without needing technical skills.

**Tools used:** Power BI Desktop, DAX, Power Query

---

## Business Questions

- Which product categories generate the most revenue and sales?
- Which age groups contribute the most to revenue and sales?
- How many customers are subscribed, and how large is the opportunity to grow subscriptions?
- How satisfied are customers, and what does the average purchase look like?

---

## Key Metrics

| Metric | Value |
|---|---|
| Total Customers | 3.90K |
| Average Rating | 3.75 / 5 |
| Average Purchase Amount | $59.76 |
| Total Revenue | ~$233K |
| Subscribed Customers | 27% |
| Non-Subscribed Customers | 73% |

---

## Dashboard Features

| Section | Description |
|---|---|
| **Filters** | Gender, Subscription Status, Category and Shipping Type slicers that update every visual |
| **KPI Cards** | Total Customers, Average Rating and Average Purchase Amount |
| **Revenue by Category** | Ranked bar chart showing which categories earn the most |
| **Sales by Category** | Ranked bar chart showing which categories sell the most |
| **Revenue by Age Group** | Column chart comparing revenue across Young, Adult, Middle-aged and Senior customers |
| **Sales by Age Group** | Column chart comparing sales across the same age groups |
| **Subscribed Customers** | Donut chart showing the Yes / No subscription split |

---

## Key Insights

| Finding | Detail |
|---|---|
| **Clothing leads** | $104K revenue, about 45% of the total, and the highest sales volume |
| **Top two categories dominate** | Clothing and Accessories together make up roughly 76% of revenue |
| **Young customers lead revenue** | $62K, the highest among age groups |
| **Seniors lead sales volume** | 79K, the highest among age groups |
| **Subscription gap** | Only 27% of customers are subscribed, which is a clear growth opportunity |
| **Moderate satisfaction** | An average rating of 3.75 leaves room to improve the customer experience |

---

## Data Model

The dashboard follows a **star schema** for performance and clarity.

```
Dim_Customer ──┐
Dim_AgeGroup ──┤
Dim_Category ──┼──< Fact_Purchases
Dim_Shipping ──┘
```

| Table | Key Columns |
|---|---|
| `Fact_Purchases` | Customer ID, Category, Item, Purchase Amount, Review Rating, Shipping Type |
| `Dim_Customer` | Customer ID, Age, Gender, Subscription Status |
| `Dim_AgeGroup` | Age Group, Sort Order |
| `Dim_Category` | Category |
| `Dim_Shipping` | Shipping Type |

**Age groups:** Young, Adult, Middle-aged, Senior. Sort order is set with a helper column so charts always display in logical order.

> **Note:** Confirm how the "Sales" metric is defined in your source data (for example, units or items sold) and label it consistently across all visuals.

---

## DAX Measures

```dax
Total Customers = DISTINCTCOUNT ( Fact_Purchases[Customer ID] )

Total Revenue = SUM ( Fact_Purchases[Purchase Amount] )

Average Purchase Amount = AVERAGE ( Fact_Purchases[Purchase Amount] )

Average Rating = AVERAGE ( Fact_Purchases[Review Rating] )

Subscribed % =
DIVIDE (
    CALCULATE ( [Total Customers], Dim_Customer[Subscription Status] = "Yes" ),
    [Total Customers]
)

Revenue % of Total =
DIVIDE ( [Total Revenue], CALCULATE ( [Total Revenue], ALL ( Fact_Purchases ) ) )

Age Group =
SWITCH (
    TRUE (),
    Dim_Customer[Age] < 25, "Young",
    Dim_Customer[Age] < 40, "Adult",
    Dim_Customer[Age] < 60, "Middle-aged",
    "Senior"
)
```

> Adjust the age thresholds to match your own grouping rules.

---

## Getting Started

### Prerequisites
- Power BI Desktop (latest version)
- The customer shopping dataset (CSV or Excel)

### Setup

1. **Clone or download** this repository.
2. Open Power BI Desktop and select **Get Data** and load your dataset.
3. In **Power Query**, clean the data:
   - Fix spelling (for example, "Senoir" to "Senior").
   - Set correct data types for amounts and ratings.
   - Create the age group column.
4. Build the relationships as shown in the [Data Model](#data-model).
5. Add the [DAX measures](#dax-measures).
6. Import the theme: **View > Themes > Browse for themes** and select `CustomerBehaviour_Theme.json`.
7. Build the visuals listed in [Dashboard Features](#dashboard-features), using the preview image as the layout guide.
8. Publish to the Power BI Service and schedule a data refresh if required.

---

## Project Structure

```
customer-behaviour-dashboard/
├── README.md
├── customer_behaviour_dashboard_simple.jpg   # Dashboard preview / layout reference
├── CustomerBehaviour_Theme.json              # Power BI theme file
├── data/
│   └── customer_data.csv                     # Source dataset (add your own)
└── CustomerBehaviour.pbix                    # Power BI report file
```

---

## Design Guidelines

- **One accent colour** (rust `#B4532A`) with a lighter tint for supporting data, so the most important value always stands out.
- **Ranked charts**: bars are sorted so the highest value is first and highlighted.
- **Plain-language subtitles** on every chart explain what the visual answers.
- **Consistent layout**: filters on top, headline KPIs next, then category and age-group detail.
- **Logical ordering**: age groups always run Young, Adult, Middle-aged, Senior.

---

## Future Enhancements

- Add a time trend once a purchase date field is available
- Add season, payment method and discount analysis
- Add drill-through pages for category detail
- Add row-level security for restricted audiences
- Create a mobile layout for phone viewing

---
