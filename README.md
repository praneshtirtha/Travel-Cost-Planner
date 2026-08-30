# Travel Cost Planner and Option Comparator

**Course:** CSE101 — Introduction to Python Programming  
**Institution:** North South University  
**Section:** 2  
**Semester:** Summer 2026  
**Group Number:** 04  
**Faculty:** Silvia Ahmed (SvA)  

---

## 👥 Group Members

| Name | Student ID |
|---|---|
| Ananto Shariar | 2211431042 |
| Pranesh Majumder Tirtha | 2222899042 |
| Md. Nasim Taif | 2212601042 |

---

## 📌 Project Overview

The **Travel Cost Planner and Option Comparator** is a console-based Python application designed to help families, student groups, and small teams estimate and compare travel expenses.

Planning a group trip may involve several expenses such as transportation, accommodation, food, activities, and other costs. Calculating these expenses manually can be confusing, especially when multiple travel options need to be compared.

The program allows users to create different travel plans, calculate their estimated costs, check whether they fit within a given budget, apply a group discount, and compare multiple options.

---

## 🎯 Project Objective

The main objective of this project is to develop a simple Python-based travel planning system that can:

- Calculate different travel expenses
- Estimate the total cost of a trip
- Calculate cost per person
- Apply a predefined group discount
- Check whether a plan fits within the available budget
- Compare multiple travel options
- Save and load travel plans using a CSV file

---

## ✨ Main Features

- Create a travel option
- Enter destination and traveller information
- Calculate transportation cost
- Calculate accommodation cost
- Calculate food cost
- Calculate activity cost
- Include additional travel expenses
- Calculate subtotal and final cost
- Apply group discount
- Calculate cost per person
- Check budget status
- Compare two or more travel options
- Provide a basic recommendation
- Save travel plans to CSV
- Load previously saved plans
- Handle invalid user input
- Handle missing or empty files safely

---

## 🧾 Travel Information

Each travel option may contain:

- Option name
- Destination
- Number of travellers
- Transport type
- Fixed transport cost
- Transport cost per person
- Number of nights
- Room capacity
- Room cost per night
- Food cost per person per day
- Activity cost per person
- Other costs
- Available budget
- Comfort rating
- Estimated travel time

---

## 🧮 Cost Calculation

### Transportation Cost

```text
Transport Cost =
Fixed Transport Cost
+ (Transport Cost Per Person × Number of Travellers)
