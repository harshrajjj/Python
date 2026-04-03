users = [
    {"id": 1, "total": 100, "coupon": "p10"},
    {"id": 2, "total": 200, "coupon": "p10"},
    {"id": 3, "total": 300, "coupon": "f10"},
    {"id": 4, "total": 400, "coupon": "f50"},
    {"id": 5, "total": 500, "coupon": "p20"},
]

discount  = {
    "p10": (0.1, 0),
    "p20": (0.2, 0),
    "f10": (0, 10),
    "f50": (0, 50),
}
for user in users:
    percent, fixed = discount.get(user["coupon"], (0, 0))
    dicount  = user["total"] * percent + fixed
    print(f"{user['id']} paid {user['total']} and got a discount for next visit of rupees {dicount} ")