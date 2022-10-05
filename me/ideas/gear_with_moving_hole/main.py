"""
cd me

python.exe -m ideas.gear_with_moving_hole.main
"""

print("hello")

for a in range(1, 3):
    for b in range(a+1, a+3):
        for c in range(b+1, b+1+3):
            print(f"S={{a,b,c}} : S={{{a}, {b}, {c}}}")

            print(f"    a+b+c={a+b+c:3}")  # a.b.c
            print(f"    a+b-c={a+b-c:3}")
            print(f"    a-b+c={a-b+c:3}")
            print(f"    a-b-c={a-b-c:3}")
            print(f"    a+c+b={a+c+b:3}")  # a.c.b
            print(f"    a+c-b={a+c-b:3}")
            print(f"    a-c+b={a-c+b:3}")
            print(f"    a-c-b={a-c-b:3}")
            print(f"    b+a+c={b+a+c:3}")  # b.a.c
            print(f"    b+a-c={b+a-c:3}")
            print(f"    b-a+c={b-a+c:3}")
            print(f"    b-a-c={b-a-c:3}")
            print(f"    b+c+a={b+c+a:3}")  # b.c.a
            print(f"    b+c-a={b+c-a:3}")
            print(f"    b-c+a={b-c+a:3}")
            print(f"    b-c-a={b-c-a:3}")
            print(f"    c+a+b={c+a+b:3}")  # c.a.b
            print(f"    c+a-b={c+a-b:3}")
            print(f"    c-a+b={c-a+b:3}")
            print(f"    c-a-b={c-a-b:3}")
            print(f"    c+b+a={c+b+a:3}")  # c.b.a
            print(f"    c+b-a={c+b-a:3}")
            print(f"    c-b+a={c-b+a:3}")
            print(f"    c-b-a={c-b-a:3}")
